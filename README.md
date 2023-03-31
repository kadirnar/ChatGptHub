<div align="center">
<h2>
     ChatGptHub: Gpt Chatbot Library with LangChain Support 
</h2>
<div>
    <a href="https://badge.fury.io/py/chatgpthub"><img src="https://badge.fury.io/py/chatgpthub.svg" alt="pypi version"></a>
</div>
</div>

This repo is a implementation of the paper ChatGPT Models with [LangChain](https://github.com/hwchase17/langchain) support.

### Installation
```bash
pip install chatgpthub
```

### Usage
```python
from chatgpthub import load_openai_key, load_promptlayer_key, translate_chatgpt

# load openai key
load_openai_key("openai_key")

# translate chatgpt model
translate_chatgpt(
    model_name="gpt-3.5-turbo",
    input_language="English",
    output_language="Turkish",
    temperature=0.0,
    text="Hello World!",
)
```

