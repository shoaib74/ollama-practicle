## Method 3 using openai module
# pip install openai - to install openai module

from openai import OpenAI
model_name = "qwen3:4b"
model = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
myprompt = "Tell me top richest country in the world"
mymsg =  [ {
            "role": "user",
            "content": myprompt
        }
         ] 
response = model.chat.completions.create(model=model_name, messages=mymsg)
print(response)
