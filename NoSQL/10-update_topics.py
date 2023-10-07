#!/usr/bin/env python3
"""
To change all topics of a school document based on the name
"""
import pymongo

def update_topics(mongo_collection, name, topics):
    """
    Insert a new document into the collection using kwargs
    """
    new_collection = mongo_collection.update_many(
        { "name": name },
        { $set: { "topics": topics } }
        )
    return new_collection
