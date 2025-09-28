from huggingface_hub import InferenceClient


def generate_answer(context: str, question: str, hf_token: str) -> str:
    """
    Gera uma resposta baseada em um contexto e uma pergunta usando
    um modelo da Hugging Face.
    """
    try:
        client = InferenceClient(token=hf_token)

        prompt = f"Contexto:\n{context}\n\nPergunta: {question}\nResposta:"

        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        return completion.choices[0].message.content
    except Exception as e:
        return f"Erro ao processar resposta: {str(e)}"
