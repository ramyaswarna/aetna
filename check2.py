from database import connect_db

db = connect_db()

drug_name = "EPIDIOLEX"  # Change to the drug that is missing

drug_entry = db.collection.find_one({"content": {"$regex": drug_name, "$options": "i"}})

if drug_entry:
    print("✅ Drug Found in Database:", drug_entry)
else:
    print("❌ Drug NOT Found in Database.")
