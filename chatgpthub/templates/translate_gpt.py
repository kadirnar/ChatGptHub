def translate_chatgpt(input_language, output_language, text):
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts.chat import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        SystemMessagePromptTemplate,
    )

    chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template
    )

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chat_completion = chat(
        chat_prompt.format_prompt(
            input_language=input_language,
            output_language=output_language,
            text=text,
        ).to_messages()
    )
    last_ai_message = chat_completion.content

    return last_ai_message
