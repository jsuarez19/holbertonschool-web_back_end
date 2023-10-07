#!/usr/bin/env python3
"""
To list all documents in a collection
"""
import pymongo

def list_all(mongo_collection):
    """
    Find all documents in the collection and convert the cursor to a list
    """
    if mongo_collection == None:
        empty_list = []
        return empty_list
    else:
        return list(mongo_collection.find())

