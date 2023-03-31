def load_openai_key(openai_key):
    import os

    os.environ["OPENAI_API_KEY"] = openai_key


def load_promptlayer_key(promptlayer_key):
    import os

    os.environ["PROMPTLAYER_API_KEY"] = promptlayer_key


import os

os.environ[
    "OPENAI_API_KEY"
] = "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"
os.environ["PROMPTLAYER_API_KEY"] = "pl_6be92c4ee88f99a5d4957882598e6a58"
