import unittest
from unittest.mock import patch, MagicMock
from converse_ai import speech
class TestSpeech(unittest.TestCase):
    @patch('speech_recognition.Microphone')
    @patch('speech_recognition.Recognizer')
    def test_recognize_speech(self, mock_recognizer, mock_microphone):
        mock_recognizer_instance = mock_recognizer.return_value
        mock_recognizer_instance.listen.return_value = 'audio'
        mock_recognizer_instance.recognize_whisper_api.return_value = 'result'
        logger = MagicMock()
        self.assertIsNotNone(speech.recognize_speech(mock_recognizer_instance, {'api_key': 'key'}, logger))

    @patch('elevenlabs.generate')
    @patch('elevenlabs.play')
    @unittest.skip
    def test_text_to_speech(self, mock_play, mock_generate):
        mock_generate.return_value = 'audio'
        self.assertIsNone(speech.text_to_speech('text', {'voice': 'voice', 'model': 'model'}))
