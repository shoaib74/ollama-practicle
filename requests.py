#Method 1 using requests module
#pip install requests   - to install module

import requests
ollama_api_url = "http://localhost:11434/api/generate"
headers = { "content-Type": "application/json"}
model = "qwen3:4b"
myprompt = "Tell me top richest country in the world"
mymsg = {
            "role": "user",
            "content": myprompt
        }
payload = {
            "model": model,
            "messages": mymsg
          }
response = requests.post(ollama_api_url, json=payload, headers=headers)
print(response)
