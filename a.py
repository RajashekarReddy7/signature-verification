from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection details
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

# Specify the database and collection
db = client["signatures_db"]
collection = db["2"]

# Array containing documents (updated with a new document)
P = [ {
    "image": {
        "path": "C:\\Users\\ragha\\OneDrive\\Desktop\\SignatureVerification\\backend\\uploads",
    }
}

]
# Insert documents in P1 with error handling for duplicate _id
for doc in P:
    try:
        result = collection.insert_one(doc)
        # Print the 'path' of the inserted document instead of the _id
        print({doc['image']['path']})
    except Exception as e:
        if "E11000 duplicate key error" in str(e):
            # Print the 'path' of the document causing the error
            print({doc['image']['path']})
        else:
            print(f"An error occurred: {e}")

# Close the connection
client.close()