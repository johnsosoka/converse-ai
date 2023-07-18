import speech_recognition as sr
from elevenlabs import generate, play, set_api_key

def recognize_speech(r, openai_config, logger):
    with sr.Microphone() as source:
        logger.info("Say something!")
        audio = r.listen(source)
        try:
            result = r.recognize_whisper_api(audio, api_key=openai_config.get('api_key'))
            logger.info(f"Whisper API thinks you said {result}")
            return result
        except sr.RequestError as e:
            logger.error("Could not request results from Whisper API")

def text_to_speech(text, elevenlabs_config):
    audio = generate(
        text=text,
        voice=elevenlabs_config.get('voice'),
        model=elevenlabs_config.get('model')
    )
    play(audio)



