#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test model"""

__author__ = 'Mr.Zhou'


def main():
    name = input("What's your name ?")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
    print(2**10)
