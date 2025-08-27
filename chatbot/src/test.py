import requests
from config import HUGGINGFACE_API_KEY

# URL correta para modelos com tarefa "conversational"
url = "https://api-inference.huggingface.co/v1/chat/completions"

# Cabeçalhos com autenticação
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

# Corpo da requisição no formato de chat
payload = {
    "model": "mistralai/Mistral-7B-Instruct-v0.2",
    "messages": [
        {
            "role": "user",
            "content": "Qual é a capital da França?"
        }
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

# Requisição POST
response = requests.post(url, headers=headers, json=payload)

# Exibe a resposta
try:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
except Exception as e:
    print("Erro ao processar resposta:", e)
    print("Resposta completa:", response.text)