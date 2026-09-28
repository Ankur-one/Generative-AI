from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# Sample sentences
sentences = [
    "I love machine learning.",
    "Machine learning is my favorite field.",
    "The weather is very cold today."
]


# Generate embeddings
embeddings = model.encode(sentences)


# Display results
for sentence, embedding in zip(sentences, embeddings):

    print("\nSentence:", sentence)

    print("Vector dimensions:", len(embedding))

    print("First 10 values:", embedding[:10])