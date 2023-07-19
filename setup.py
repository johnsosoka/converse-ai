"""
setup.py

This module provides the setup configuration for the Converse AI application.
It includes a custom setup command to create a .converse-ai directory and copy a starter config.yml file.
The setup configuration also includes the application's metadata and dependencies.

Author: John Sosoka
Date: 2023-07-18
Email: code@johnsosoka.com
"""


import os
import shutil
from setuptools import setup, find_packages, Command
from setuptools.command.install import install

class SetupConfigCommand(Command):
    description = 'create a .converse-ai directory and copy a starter config.yml'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        home_dir = os.path.expanduser("~")
        converse_dir = os.path.join(home_dir, '.converse-ai')
        os.makedirs(converse_dir, exist_ok=True)

        config_file = os.path.join(converse_dir, 'config.yml')
        if not os.path.exists(config_file):
            shutil.copyfile('./template/config_template.yml', config_file)
        print("A new config file has been created at {}. Please update the keys in this file.".format(config_file))

class InstallCommand(install):
    def run(self):
        self.run_command('setup_config')
        super().run()

setup(
    name='converse-ai',
    version='0.1',
    description='Have a voice conversation with chatGPT.',
    author='John Sosoka',
    author_email='code@johnsosoka.com',
    url='https://github.com/johnsosoka/converse-ai',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'SpeechRecognition',
        'openai',
        'elevenlabs'
    ],
    entry_points={
        'console_scripts': [
            'converse-ai=converse_ai.main:main_loop',
        ],
    },
    cmdclass={
        'setup_config': SetupConfigCommand,
        'install': InstallCommand,
    },
)
