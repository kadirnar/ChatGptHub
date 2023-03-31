from chatgpthub import load_openai_key, load_promptlayer_key, translate_chatgpt


def load_key(openai_key: str = None, promptlayer_key: str = None):
    """
    This function loads the OpenAI and PromptLayer keys.
    Args:
        openai_key: The OpenAI key to use. Defaults to None.
        promptlayer_key: The PromptLayer key to use. Defaults to None.
    """
    if openai_key is not None:
        load_openai_key(openai_key)
    if promptlayer_key is not None:
        load_promptlayer_key(promptlayer_key)


class ChatGptHubDemo:
    def __init__(self, openai_key: str = None, promptlayer_key: str = None):
        """
        This class is a demo for the chatgpthub library.
        Args:
            openai_key: The OpenAI key to use. Defaults to None.
            promptlayer_key: The PromptLayer key to use. Defaults to None.
        """
        load_key(openai_key, promptlayer_key)

    def translate(
        self,
        model_name: str = "gpt-3.5-turbo",
        input_language: str = "English",
        output_language: str = "Turkish",
        text: str = "Hello, how are you?",
        temperature: float = 0.0,
    ):
        """
        This function is a demo for the translate_chatgpt function.
        Args:
            model_name: The name of the model to use. Defaults to "gpt-3.5-turbo".
            input_language: The language to translate from. Defaults to "English".
            output_language: The language to translate to. Defaults to "Turkish".
            text: The text to translate. Defaults to "Hello, how are you?".
            temperature: The temperature to use for the model. Defaults to 0.0.
        Returns:
            The translated text.
        """
        output = translate_chatgpt(
            model_name=model_name,
            input_language=input_language,
            output_language=output_language,
            text=text,
            temperature=temperature,
        )

        return output


if __name__ == "__main__":
    demo = ChatGptHubDemo()
    output = demo.translate(
        model_name="gpt-3.5-turbo",
        input_language="English",
        output_language="Turkish",
        text="Hello, how are you?",
        temperature=0.0,
    )

    print(output)
