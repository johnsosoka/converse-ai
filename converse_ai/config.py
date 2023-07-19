"""
config.py

This module provides functions to load and validate the configuration for the Converse AI application.

Author: John Sosoka
Date: 2023-07-18
Email: code@johnsosoka.com
"""
import os
import yaml
import sys
import logging


def check_config(config):
    """
    Validates the loaded configuration and checks if all necessary values are set.

    Args:
        config (dict): The loaded configuration dictionary.

    Raises:
        SystemExit: If a necessary value in the configuration is still set to its default value.
    """
    defaults = {
        'openAI': {
            'api_key': 'YOUR_OPENAI_API_KEY',
        },
        'elevenLabs': {
            'api_key': 'YOUR_ELEVENLABS_API_KEY',
        },
    }

    for section, values in defaults.items():
        for key, default_value in values.items():
            if config[section][key] == default_value:
                print("Please set a value for {} in the {} section of the config file.".format(key, section))
                sys.exit(1)


def load_config():
    """
    Loads the configuration from a YAML file in the user's home directory.

    Returns:
        dict: The loaded configuration dictionary.

    Raises:
        SystemExit: If the configuration file does not exist.
    """
    config_path = os.path.expanduser('~/.converse-ai/config.yml')
    if not os.path.exists(config_path):
        print("The config file does not exist at: {}".format(config_path))
        sys.exit(1)
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
        # Validate before returning.
        check_config(config)
        return config


def setup_logging(log_level):
    """
    Sets up a logger with a specified log level.

    Args:
        log_level (str): The log level to set for the logger.

    Returns:
        logging.Logger: The set up logger.
    """
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
