import unittest
from unittest.mock import patch, MagicMock
from converse_ai import openai_chat

class TestOpenAIChat(unittest.TestCase):
    @patch('openai.Completion.create')
    def test_fetch_openai_response(self, mock_create):
        mock_create.return_value = MagicMock(choices=[MagicMock(text=' text ')])
        logger = MagicMock()
        self.assertEqual('text', openai_chat.fetch_openai_response('prompt', {}, [], logger))
