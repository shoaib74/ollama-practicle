#Method2:  Ollama module
#pip install ollama -  to install ollama module

import ollama
model = "qwen3:4b"
myprompt = "Tell me top richest country in the world"
mymsg =  [ {
            "role": "user",
            "content": myprompt
        }
         ]      
response = ollama.chat(model=model, messages=mymsg)
print(response)
