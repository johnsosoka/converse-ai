from .config import load_config, setup_logging
from .speech import recognize_speech, text_to_speech
from .openai_chat import fetch_openai_response
import speech_recognition as sr
from elevenlabs import set_api_key
import openai
import logging

def main_loop():
    # Load config from the YAML file
    config = load_config()
    openai_config = config.get('openAI', {})
    elevenlabs_config = config.get('elevenLabs', {})

    # Set API keys
    set_api_key(elevenlabs_config.get('api_key'))
    openai.api_key = openai_config.get('api_key')

    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Define the conversation history
    conversation = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Who won the world series in 2020?'},
        {'role': 'assistant', 'content': 'The Los Angeles Dodgers won the World Series in 2020.'}
    ]

    # Set up logging
    logger = setup_logging(config.get('log_level', logging.INFO))

    logger.info("Starting the assistant...")
    text_to_speech("Hello, I am your assistant. How can I help you?", elevenlabs_config)

    while True:
        logger.debug("Listening for speech...")
        prompt = recognize_speech(r, openai_config, logger)
        logger.debug("identified speech: " + prompt)
        if prompt is None or prompt == "":
            logger.debug("No text, skipping AI call.")
            continue
        open_ai_response = fetch_openai_response(prompt, openai_config, conversation, logger)
        text_to_speech(open_ai_response, elevenlabs_config)

if __name__ == "__main__":
    main_loop()
