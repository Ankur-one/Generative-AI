from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

sentences = [
    "I love machine learning.",
    "Machine learning is my favorite field.",
    "The weather is very cold today."
]

vectors = embedding.embed_documents(sentences)

print("Number of sentences:", len(vectors))
print("Embedding dimensions:", len(vectors[0]))

for sentence, vector in zip(sentences, vectors):
    print("\nSentence:", sentence)
    print("First 10 values:", vector[:10])