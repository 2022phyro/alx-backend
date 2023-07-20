#!/usr/bin/env [python3
"""Introduction into pagination"""


def index_range(page, page_size):
    """Returns the page size needed and the index to start from"""
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)
