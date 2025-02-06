from database import Database

db = Database()
search_results = db.query_database("Xarelto")

print("🔍 VectorDB Output:", search_results)
