#!/usr/bin/env python3
"""
This Module contains  a Python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    mongo_collection.updateMany({"name": name}, {"$set": {"topics": topics}})
