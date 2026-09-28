from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="auto"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain RAG in simple Hinglish."
        }
    ],
    max_tokens=256,
    temperature=0.7,
)

print(response.choices[0].message.content)