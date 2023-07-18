import openai

def fetch_openai_response(prompt, openai_config, conversation, logger):
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
