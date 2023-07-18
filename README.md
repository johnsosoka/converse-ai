# Converse AI

Converse AI allows you to have a spoken conversation with an AI assistant. It uses the [OpenAI API](https://beta.openai.com/) 
to generate responses to your questions, and the [ElevenLabs API](https://www.eleven-labs.com/) to convert the responses to speech.

## Pre-requisites

You must have valid API keys for both OpenAI and ElevenLabs. You can get the OpenAI API key from the 
[OpenAI website](https://beta.openai.com/signup/), and the ElevenLabs API key from the [ElevenLabs website](https://www.eleven-labs.com/).

## Installation

To install Converse AI, you need to have Python 3.6 or later. You can install the project with pip:

```bash
pip install -r requirements.txt
```

This command will install the project and its dependencies, and it will create a `.converse-ai` directory in your home directory with a `config.yml` file.

## Configuration

Before you can use Converse AI, you need to configure it. Open the `config.yml` file in the `.converse-ai` directory and replace the placeholders with your actual API keys and preferences:

```yaml
openAI:
  api_key: YOUR_OPENAI_API_KEY
  engine: text-davinci-003
  max_tokens: 50
  temperature: 0.7
elevenLabs:
  api_key: YOUR_ELEVENLABS_API_KEY
  voice: YOUR_PREFERRED_VOICE
  model: YOUR_PREFERRED_MODEL
log_level: INFO
```

You can get the OpenAI API key from the [OpenAI website](https://beta.openai.com/signup/), and the ElevenLabs API key from the [ElevenLabs website](https://www.eleven-labs.com/). The `voice` and `model` parameters are specific to ElevenLabs and you can find more information about them in the ElevenLabs documentation.

The `log_level` can be set to any valid logging level from the Python `logging` module, such as `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. The default value is `INFO`.

## Usage

After installing and configuring Converse AI, you can start it with the following command:

```bash
converse-ai
```

The assistant will start and greet you with "Hello, I am your assistant. How can I help you?". You can then start speaking to the assistant.

## Testing

Converse AI comes with a suite of unit tests. You can run them with the following command:

```bash
python -m unittest discover
```

This command will discover and run all test cases in the project.

## Contributing

If you want to contribute to Converse AI, feel free to fork the repository and submit a pull request.

## License

Converse AI is licensed under the GPL-2.0 license. See the `LICENSE` file for more details.
