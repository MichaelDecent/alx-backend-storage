#!/usr/bin/env python3
"""
This Module contain a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_logs(nginx_collection):
    """
    provides some stats about Nginx logs stored in MongoDB:
    """
    print(f"{nginx_collection.estimated_document_count()} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        no_doc = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {no_doc}")

    get_path_docs = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{get_path_docs} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    nginx_logs(nginx_collection)
