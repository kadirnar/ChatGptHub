<div align="center">
<h2>
     ChatGptHub: Gpt Chatbot Library with LangChain Support 
</h2>
<div>
    <a href="https://badge.fury.io/py/chatgpthub"><img src="https://badge.fury.io/py/chatgpthub.svg" alt="pypi version"></a>
</div>
</div>

This repo is a implementation of the ChatGPT Models with [LangChain](https://github.com/hwchase17/langchain) support.

### Installation
```bash
pip install chatgpthub
```

### Usage
```python
from chatgpthub import (
    load_openai_key,
    load_promptlayer_key,
    prompt_template,
    translate_chatgpt,
    promptlayer_chatgpt,
)

# translate chatgpt model
from chatgpthub.demo import ChatGptHubDemo

demo = ChatGptHubDemo(
    openai_key="openai_key",
    promptlayer_key="promptlayer_key", #optional
)

# translate chatgpt model
demo.translate(
    model_name: str = "gpt-3.5-turbo",
    input_language: str = "English",
    output_language: str = "Turkish",
    text: str = "Hello, how are you?",
    temperature: float = 0.0,
)

# promptlayer chatgpt model
demo.promptlayer(
    model_name: str = "gpt-3.5-turbo",
    text: str = "Hello, how are you?",
    temperature: float = 0.0,
)

# custom template chatgpt model
template = """
Englist words explanation:
    - {text}
Turkish words explanation:
    - {translation}
"""

template = "You are a helpful assistant that python to c++ and you are asked to translate the following text: {text}"
text = "print('Hello, world!')"
output = demo.custom_template(
    model_name="gpt-3.5-turbo",
    template=template,
    input_variables="text",
    text=text,
    temperature=0.0,
)

```
