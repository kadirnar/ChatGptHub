def output_parser(text):
    from langchain.chat_models import ChatOpenAI
    from langchain.output_parsers import CommaSeparatedListOutputParser
    from langchain.prompts import PromptTemplate

    output_parser = CommaSeparatedListOutputParser()

    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template="List five {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions},
    )

    model = ChatOpenAI(
        temperature=0.0,
        model_name="gpt-3.5-turbo",
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    _input = prompt.format(subject=text)
    output = model(_input)
    output = output_parser.parse(output)

    return output
