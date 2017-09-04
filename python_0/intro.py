#!/usr/bin/env python3
#
# The first line allows to run this script as ./intro.py,
# for more details use google with keyword shebang

### Intro:
# Run: python3 <script_name>
# REPL: python3

## Primitive types
# Int, buit-in BigInt, 2 ** 65
# float, 1e-10, 3.1415926
# complex (real + img i), complex(0, 1) ** 2
# bool -- True, False
# Strings -- immutable:
# ' ', " ", """ """,
# a = '''
#        This is a multiline string,
#        So, you can put a poem inside
#        ...
#     '''

## Variables, assignments
# #comment
# indentation

## Conditionals
# see conditionals.py

## Cycles
# while cond:
#   pass
# break, continue
# see guess_number.py

### Functions
# def name(param, pampam):
#     """ Prints first parameter. """
#     print(param)

# Function call:
# print(..)
# input(prompt)
# Help: help(<function_name>)

## For loop
# see ranges.py

## Lists
# see lists.py

companies = ["apple", "google", "microsoft"]
print("Companies:", ", ".join(companies))
# separator.join(iterable)
print(" 1 2 3 1 ".find("1"))
print(" with spaces ".strip())
a = "hello"
# take substring (immutable)
a[:-2]
# multiply strings
"a" * 4 == "aaaa"
# iterate over strings
for char in "hello":
    pass

# files
# f = open("filename.txt")
# for line in f:
#     print(line)
# f.close()
