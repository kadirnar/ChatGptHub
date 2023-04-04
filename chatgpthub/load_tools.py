from typing import Optional

from chatgpthub import load_openai_key, load_promptlayer_key
from chatgpthub.tools import load_csv_agent


def load_key(
    openai_key: Optional[str] = None, promptlayer_key: Optional[str] = None
):
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


class ChatGptTools:
    def __init__(
        self,
        openai_key: Optional[str] = None,
        promptlayer_key: Optional[str] = None,
    ):
        """
        This class is a demo for the chatgpthub library.
        Args:
            openai_key: The OpenAI key to use. Defaults to None.
            promptlayer_key: The PromptLayer key to use. Defaults to None.
        """
        load_key(openai_key=openai_key)

        self.promptlayer_key = promptlayer_key

    def load_key(
        self,
        openai_key: Optional[str] = None,
        promptlayer_key: Optional[str] = None,
    ):
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

    def load_csv_agent(self, csv_file: str, agent_name: str):
        """
        This function loads a CSV agent.
        Args:
            csv_file: The CSV file to load.
            agent_name: The name of the agent.
        """
        output = load_csv_agent(csv_file, agent_name)
        return output
