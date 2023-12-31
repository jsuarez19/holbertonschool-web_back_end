#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    Returns a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    indexes = (start_index, end_index)
    return indexes


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a specific page of the dataset
        """
        assert(type(page) == int and page > 0)
        assert(type(page_size) == int and page_size > 0)
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a Dictionary with some key value pairs
        """
        output = {}
        pages = self.dataset()
        number_pages = len(pages) / page_size
        number_pages = math.floor(number_pages)

        output["page_size"] = page_size
        output["page"] = page
        output["data"] = self.get_page(page, page_size)

        if number_pages == page:
            output["next_page"] = None
        else:
            output["next_page"] = page + 1

        if page > 1:
            output["prev_page"] = int(page - 1)
        else:
            output["prev_page"] = None
        output["total_pages"] = number_pages

        return output
