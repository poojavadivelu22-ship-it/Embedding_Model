from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I like playing cricket.",
    "I enjoy playing football.",
    "The weather is very hot today.",
    "The sun is shining brightly.",
    "I am learning Python programming.",
    "Python is used for data science.",
    "My favorite food is pizza.",
    "I love eating cheese pizza."
]

embeddings = model.encode(sentences)

print("Total number of sentences:", len(sentences))
print("Embedding dimension:", len(embeddings[0]))

print("\n--- Embeddings ---")

for i, sentence in enumerate(sentences):
    print("\nSentence:", sentence)
    print("Embedding:", embeddings[i])

similarity = cosine_similarity(embeddings)

print("\n--- Semantic Similarity ---")

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        if similarity[i][j] > 0.5:
            print(
                f"\nSentence 1: {sentences[i]}"
                f"\nSentence 2: {sentences[j]}"
                f"\nSimilarity: {similarity[i][j]:.4f}"
            )