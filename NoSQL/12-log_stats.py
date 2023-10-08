#!/usr/bin/env python3
"""
To provide some stats about Nginx logs stored in MongoDB
"""
import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection_used = db.nginx

    count_logs = collection_used.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    status = collection_used.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print("{} logs".format(count_logs))
    print("Methods:")
    for method in methods:
        count = collection_used.count_documents({"method": method})
        print("\t method {}: {}".format(method, count))
    print("{} status check".format(status))
