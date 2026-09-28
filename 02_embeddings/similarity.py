from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# Sentences
sentences = [
    "I love machine learning.",
    "Machine learning is my favorite field.",
    "The weather is very cold today."
]


# Generate embeddings
embeddings = model.encode(sentences)


# Calculate cosine similarity
similarity_matrix = cosine_similarity(embeddings)


print("\nSimilarity Matrix:")
print(similarity_matrix)