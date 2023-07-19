"""
openai_chat.py

This module provides a function to fetch a response from OpenAI's GPT-3 model.

Author: John Sosoka
Date: 2023-07-18
Email: code@johnsosoka.com
"""

import openai

def fetch_openai_response(prompt, openai_config, conversation, logger):
    """
    Fetches a response from OpenAI's GPT-3 model based on a given prompt and conversation history.

    Args:
        prompt (str): The prompt to send to the GPT-3 model.
        openai_config (dict): The configuration for the OpenAI API.
        conversation (list): The conversation history.
        logger (logging.Logger): The logger to use for logging information.

    Returns:
        str: The response from the GPT-3 model.
    """
    logger.info("Fetching response for: " + prompt)
    conversation.append({'role': 'user', 'content': prompt})
    logger.info(conversation)

    # Build the prompt string
    prompt_text = '\n'.join([f"{msg['role']}: {msg['content']}" for msg in conversation])

    # Send the prompt string to the Chat API
    response = openai.Completion.create(
        engine=openai_config.get('engine', 'text-davinci-003'),
        prompt=prompt_text,
        max_tokens=openai_config.get('max_tokens', 50),
        temperature=openai_config.get('temperature', 0.7),
        n=1,
        stop=None,
    )

    # Extract the assistant's reply from the response
    reply = response.choices[0].text.strip()
    reply = reply.removeprefix("Assistant:")
    reply = reply.removeprefix("assistant:")
    logger.info(reply)
    return reply
