#!/usr/bin/python3
"""Module with lookup function"""


def lookup(obj):
    """Returns a list of available attributes and methods of
    an object"""
    return dir(obj)
