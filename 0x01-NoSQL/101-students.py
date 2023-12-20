#!/usr/bin/env/ python3
"""
This Module contains a Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    students = list(mongo_collection.find())
    for doc in students:
        score = 0
        for topic in doc["topics"]:
            score += topic["score"]
        doc["averageScore"] = score / len(doc["topics"])
    sorted_students = sorted(students, key=lambda x: x["averageScore"], reverse=True)

    return sorted_students
