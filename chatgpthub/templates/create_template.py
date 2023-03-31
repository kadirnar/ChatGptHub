def prompt_template(template, input_variables, text):
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
