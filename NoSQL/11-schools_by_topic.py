#!/usr/bin/env python3
"""
To return the list of school having a specific topic:
"""
import pymongo

def schools_by_topic(mongo_collection, topic):
    """
    Find documents in the collection where the
    "topics" field contains the specified topic
    """
    new_collection = mongo_collection.find({ "topics": topic })
    return list(new_collection)
