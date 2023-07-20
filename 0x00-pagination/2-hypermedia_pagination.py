#!/usr/bin/env python3
"""A simple pagination"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """Returns the page size needed and the index to start from"""
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)


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
        """Gets a page according to a specific index"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page > 0)
        ran = index_range(page, page_size)
        data = []
        try:
            x = self.dataset()
            y = ran[1]
            if y >= len(x):
                data = x[ran[0]:]
            else:
                data = x[ran[0]:y]
        except IndexError:
            pass
        finally:
            return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implements hypermedia pagination"""
        data = self.get_page(page, page_size)
        p_s = len(data)
        t_page = len(self.dataset()) / page_size
        t_page = math.ceil(t_page)
        n_page = page + 1
        p_page = page - 1
        if p_page < 1:
            p_page = None
        if n_page > t_page:
            n_page = None
        return {
            'page_size': p_s,
            'page': page,
            'data': data,
            'next_page': n_page,
            'prev_page': p_page,
            'total_pages': t_page
                }
