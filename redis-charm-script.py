import redis
import numpy as np
import random

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=False)

# Function to calculate cosine similarity
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Clear previous data
r.flushall()

# Function to generate random vector
def generate_random_vector():
    return np.array([random.uniform(0.1, 0.9) for _ in range(4)], dtype=np.float32)

# Charm data
charms = {
    "Explorer": np.array([0.1, 0.8, 0.3, 0.6], dtype=np.float32),
    "Alpha": np.array([0.5, 0.2, 0.3, 0.3], dtype=np.float32),
    "Yoda": np.array([0.8, 0.1, 0.1, 0.4], dtype=np.float32),
    "Panda": generate_random_vector(),
    "Sheila": generate_random_vector(),
    "Pepperjack": generate_random_vector()
}

# Add charms
for charm_name, vector in charms.items():
    r.set(f"charm:{charm_name}", vector.tobytes())
    print(f"Added charm: {charm_name} with vector: {vector}")

# Query vector
query_vector = np.array([0.15, 0.75, 0.35, 0.55], dtype=np.float32)
print(f"\nQuery Vector: {query_vector}")

# Manual similarity search
results = []
for charm_name in charms.keys():
    stored_vector = np.frombuffer(r.get(f"charm:{charm_name}"), dtype=np.float32)
    similarity = cosine_similarity(query_vector, stored_vector)
    results.append((charm_name, similarity))

# Sort and display results
results.sort(key=lambda x: x[1], reverse=True)
print("\nSimilarity Search Results:")
for charm_name, similarity in results:
    print(f"Charm: {charm_name}, Similarity: {similarity:.4f}")