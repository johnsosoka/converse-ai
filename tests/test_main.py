import unittest
from unittest.mock import patch, MagicMock
from converse_ai import main
import logging
import speech_recognition as sr
class TestMain(unittest.TestCase):

    @unittest.skip
    @patch('converse_ai.main.load_config')
    @patch('converse_ai.main.setup_logging')
    @patch('converse_ai.main.set_api_key')
    @patch('converse_ai.main.sr.Recognizer')
    @patch('converse_ai.main.recognize_speech')
    @patch('converse_ai.main.fetch_openai_response')
    @patch('converse_ai.main.text_to_speech')
    def test_main_loop(self, mock_text_to_speech, mock_fetch_openai_response, mock_recognize_speech, mock_recognizer, mock_set_api_key, mock_setup_logging, mock_load_config):
        # Mock the dependencies
        mock_load_config.return_value = {
            'openAI': {'api_key': 'openai_key'},
            'elevenLabs': {'api_key': 'elevenlabs_key'},
            'log_level': 'INFO'
        }
        mock_setup_logging.return_value = MagicMock(spec=logging.Logger)
        mock_recognizer.return_value = MagicMock(spec=sr.Recognizer)
        mock_recognize_speech.return_value = 'prompt'
        mock_fetch_openai_response.return_value = 'response'

        # We need to break the infinite loop for testing, so we'll stop after one iteration
        mock_text_to_speech.side_effect = lambda x, y: exit(0)

        # Run the function in a try/except block because we're expecting it to exit
        try:
            main.main_loop()
        except SystemExit:
            pass

        # Check if the mocks were called as expected
        mock_load_config.assert_called_once()
        mock_setup_logging.assert_called_once_with('INFO')
        mock_set_api_key.assert_called_once_with('elevenlabs_key')
        mock_recognizer.assert_called_once()
        mock_recognize_speech.assert_called_once()
        mock_fetch_openai_response.assert_called_once_with('prompt', {'api_key': 'openai_key'}, [], mock_setup_logging.return_value)
        mock_text_to_speech.assert_called_once_with('response', {'api_key': 'elevenlabs_key'})

if __name__ == '__main__':
    unittest.main()
