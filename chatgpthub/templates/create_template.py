def prompt_template(
    template: str = "You are a helpful assistant that English to Turkish and you are asked to translate the following text: {text}",
    input_variables: str = "text",
    text: str = "Hello, how are you?",
):
    from langchain.chains import LLMChain
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import PromptTemplate

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    prompt = PromptTemplate(
        input_variables=[input_variables], template=template
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(text)
    return output
