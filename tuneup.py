#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Shaquon"

import cProfile
import io
import pstats
from functools import wraps
import timeit


def profile_decorator(func):
    """A function that can be used as a decorator to measure performance"""
    @wraps(func)
    def wrapped(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats(10)
        return result
    return wrapped


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile_decorator
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies.sort()
    # duplicates = []
    # while movies:
    #     movie = movies.pop()
    #     if movie in movies:
    #         duplicates.append(movie)
    duplicates = [m1 for m1,m2 in zip(movies[1:], movies[:-1]) if m1 == m2]
    print(duplicates)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='main()', setup='text = "sample string"; char = "g"')
    result = t.repeat(repeat=3, number=3)
    avg_of_min = min([times/3 for times in result])
    print('Best time across 3 repeats of 3 runs per repeat:{} sec'.format(avg_of_min))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    # timeit_helper()


if __name__ == '__main__':
    main()
