#!/bin/python3
n1 = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))
students = english.difference(french)
print (len(students))
