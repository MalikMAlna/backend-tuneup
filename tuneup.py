#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Help from Ybrayym A."

import cProfile as prof
import pstats
# import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def inner_func(*args, **kwargs):
        pr = prof.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).strip_dirs().sort_stats("cumulative")
        ps.print_stats()  # defaults to top 10
        return retval
    return inner_func


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [m_1 for m_1, m_2 in zip(
        movies[:-1], movies[1:]) if m_1 == m_2]
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    result = min(t.repeat(repeat=7, number=3)) / float(3)
    print(f"Best time across 7 repeats of 3 runs per repeat: {result} sec")


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
