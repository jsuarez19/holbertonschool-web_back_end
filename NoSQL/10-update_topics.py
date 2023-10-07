#!/usr/bin/env python3
"""
To change all topics of a school document based on the name
"""
import pymongo

def update_topics(mongo_collection, name, topics):
    """
    Update topics of school documents with a given name
    """
    new_collection = mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
        )
    return new_collection
