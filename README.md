# Converse AI

Converse AI is a novelty application that enables users to engage in spoken conversations with an AI assistant. It 
leverages the power of the [OpenAI API](https://beta.openai.com/) to generate intelligent responses to user queries and 
employs the [ElevenLabs API](https://www.eleven-labs.com/) to convert these responses into speech.

Once installed, a conversation can be initiated with a single command, `converse-ai`. The assistant will then greet, starting
your first spoken conversation with an artificial intelligence.

## Prerequisites

To utilize Converse AI, you must possess valid API keys for both OpenAI and ElevenLabs. You can acquire the OpenAI API 
key from the [OpenAI website](https://beta.openai.com/signup/), and the ElevenLabs API key from the [ElevenLabs website](https://www.eleven-labs.com/).

## Installation

### From Repository

1. Clone the repository:

    ```bash
    git clone git@github.com:johnsosoka/converse-ai.git
   ```
2. Navigate to the root directory of the project in your terminal.
3. Execute the following command:

    ```bash
    python3 setup.py install
    ```

### Configuration

During the installation process, a `.converse-ai` directory will be created in your home directory, containing a `config.yml` file. You must edit this file and add your API keys before you can use Converse AI.

**Example:**
```yaml
openAI:
  api_key: YOUR_OPENAI_API_KEY
  engine: text-davinci-003
  max_tokens: 50
  temperature: 0.7
elevenLabs:
  api_key: YOUR_ELEVENLABS_API_KEY
  voice: Adam
  model: eleven_monolingual_v1
log_level: INFO
```

The `log_level` can be set to any valid logging level from the Python `logging` module, such as `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. The default value is `INFO`.

## Usage

After installing and configuring Converse AI, you can start it with the following command:

```bash
converse-ai
```

The assistant will initiate the conversation with "Hello, I am your assistant. How can I help you?". It will then listen for your input and respond audibly to your question. This process will continue until you exit the program.

## Development

To set up a development environment for Converse AI, follow these steps:

1. Clone the repository:

    ```bash
    git clone git@github.com:johnsosoka/converse-ai.git
    ```
2. Navigate to the root directory of the project in your terminal.
3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Make your changes to the code. Remember to follow the existing code style and add comments where necessary.
5. Test your changes (see the Testing section below).
6. Submit a pull request with your changes.

## Testing

Converse AI includes a suite of unit tests to ensure its functionality. You can run these tests with the following command:

```bash
python -m unittest discover
```

This command will discover and run all test cases in the project.

## Contributing

Contributions to Converse AI are always welcome. If you're interested in contributing, please fork the repository and submit a pull request with your changes.

## License

Converse AI is licensed under the GPL-2.0 license. For more details, please see the `LICENSE` file.

## Contact

For any queries or further information, please [contact]( https://johnsosoka.com/contact) the author:
