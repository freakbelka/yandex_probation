# -*- coding: utf-8 -*-
# doctest for email validation module 

from validation.email import emailcheck

if __name__ == "__main__":
	import doctest
	doctest.testfile("example.txt")