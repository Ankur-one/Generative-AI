from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Explain Generative AI in simple Hinglish.")

print(response.content)