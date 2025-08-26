import requests


def generate_answer(context: str, question: str, hf_token: str) -> str:
    prompt = f"Contexto:\n{context}\n\nPergunta: {question}\nResposta:"
    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
            headers={"Authorization": f"Bearer {hf_token}"},
            json={"inputs": prompt}
        )

        if response.status_code != 200:
            return f"Erro HTTP {response.status_code}: {response.text}"

        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif "error" in result:
            return f"Erro da API Hugging Face: {result['error']}"
        else:
            return "Resposta inesperada da API."
    except Exception as e:
        return f"Erro ao processar resposta: {str(e)}"