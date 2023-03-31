def promptlayer_chatgpt(text):
    from langchain.chat_models import PromptLayerChatOpenAI
    from langchain.schema import HumanMessage

    chat = PromptLayerChatOpenAI(
        pl_tags=["langchain"], model_name="gpt-3.5-turbo"
    )
    chat_completion = chat([HumanMessage(content=text)]).content

    return chat_completion
