def load_openai_key(openai_key):
    import os

    os.environ["OPENAI_API_KEY"] = openai_key


def load_promptlayer_key(promptlayer_key):
    import os

    os.environ["PROMPTLAYER_API_KEY"] = promptlayer_key
