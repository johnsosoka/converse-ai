import yaml
import logging

def load_config():
    with open('.converse-ai/config.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)
        return config

def setup_logging(log_level):
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
