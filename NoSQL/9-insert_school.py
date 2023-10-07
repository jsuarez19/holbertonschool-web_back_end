#!/usr/bin/env python3
"""
To insert a new document in a collection based on kwargs
"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection using kwargs
    """
    new_collection = mongo_collection.insert_one(kwargs)
    return new_collection.inserted_id
