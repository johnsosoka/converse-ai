#!/usr/bin/env python3
import yaml
import logging
import speech_recognition as sr
from elevenlabs import generate, play, set_api_key, voices
import openai

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config():
    with open('config.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)
        return config

# Load config from the YAML file
config = load_config()
openai_config = config.get('openAI', {})
elevenlabs_config = config.get('elevenLabs', {})

# Set API keys
set_api_key(elevenlabs_config.get('api_key'))
openai.api_key = openai_config.get('api_key')

# Initialize the speech recognizer
r = sr.Recognizer()

# Get available voices
voices = voices()

# Define the conversation history
conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Who won the world series in 2020?'},
    {'role': 'assistant', 'content': 'The Los Angeles Dodgers won the World Series in 2020.'}
]

def recognize_speech():
    with sr.Microphone() as source:
        logger.info("Say something!")
        audio = r.listen(source)
        try:
            result = r.recognize_whisper_api(audio, api_key=openai_config.get('api_key'))
            logger.info(f"Whisper API thinks you said {result}")
            return result
        except sr.RequestError as e:
            logger.error("Could not request results from Whisper API")

def text_to_speech(text):
    audio = generate(
        text=text,
        voice=elevenlabs_config.get('voice'),
        model=elevenlabs_config.get('model')
    )
    play(audio)

def fetch_openai_response(prompt):
    logger.info("Fetching response for: " + prompt)
    conversation.append({'role': 'user', 'content': prompt})
    logger.info(conversation)

    # Build the prompt string
    prompt_text = '\n'.join([f"{msg['role']}: {msg['content']}" for msg in conversation])

    # Send the prompt string to the Chat API
    response = openai.Completion.create(
        engine=openai_config.get('engine', 'text-davinci-003'),
        prompt=prompt_text,
        max_tokens=openai_config.get('max_tokens', 50),
        temperature=openai_config.get('temperature', 0.7),
        n=1,
        stop=None,
    )

    # Extract the assistant's reply from the response
    reply = response.choices[0].text.strip()
    reply = reply.removeprefix("Assistant:")
    reply = reply.removeprefix("assistant:")
    logger.info(reply)
    return reply

def main_loop():
    logger.info("Listening for speech...")
    prompt = recognize_speech()
    logger.info("identified speech: " + prompt)
    if prompt is None or prompt == "":
        logger.info("No text, skipping AI call.")
        main_loop()
    open_ai_response = fetch_openai_response(prompt)
    text_to_speech(open_ai_response)
    main_loop()

if __name__ == "__main__":
    # Set up logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("Starting the assistant...")
    text_to_speech("Hello, I am your assistant. How can I help you?")
    main_loop()
