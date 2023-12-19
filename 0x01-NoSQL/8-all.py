"""
This Module contains a a Python function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    lists all documents in a collection:
    """
    return mongo_collection.find() if mongo_collection else []
