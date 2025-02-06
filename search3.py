from numpy import dot
from numpy.linalg import norm

stored_vector = db.collection.find_one({"content": {"$regex": "EPIDIOLEX", "$options": "i"}})["title_embedding"]
query_vector = model.generate_embedding("EPIDIOLEX")

if stored_vector and query_vector:
    similarity = dot(stored_vector, query_vector) / (norm(stored_vector) * norm(query_vector))
    print(f"🔍 Cosine Similarity Between Query & Stored: {similarity:.4f}")
else:
    print("❌ One of the embeddings is missing!")
