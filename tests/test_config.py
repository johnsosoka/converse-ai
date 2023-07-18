import unittest
from unittest.mock import patch, MagicMock
from converse_ai import config

class TestConfig(unittest.TestCase):
    @patch('builtins.open', new_callable=MagicMock)
    @patch('yaml.safe_load')
    def test_load_config(self, mock_safe_load, mock_open):
        mock_safe_load.return_value = {}
        self.assertIsNotNone(config.load_config())
        mock_open.assert_called_once_with('.converse-ai/config.yml', 'r')

    def test_setup_logging(self):
        logger = config.setup_logging('INFO')
        self.assertIsNotNone(logger)
