from database import Database

db = Database()
drug_name = "EPIDIOLEX"  # Change this to the drug you want to check

# Find if the drug exists in stored content
drug_entry = db.collection.find_one({"content": {"$regex": drug_name, "$options": "i"}})

if drug_entry:
    print(f"✅ Drug '{drug_name}' found in MongoDB!")
    print("Stored Entry:", drug_entry)
else:
    print(f"❌ Drug '{drug_name}' NOT found in MongoDB. It was never stored.")
