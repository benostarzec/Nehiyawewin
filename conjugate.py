# -*- coding: UTF-8 -*-
import VII, VAI

# conjugate a verb
def conjugate(verb, conjugation):
    if verb[2] == "VII":
        return VII.conjugate(verb[0], conjugation, verb[3])
    if verb[2] == "VAI":
        return VAI.conjugate(verb[0], conjugation)

# get all conjugations of a verb
def conjugate_ALL(verb):
    if verb[2] == "VII":
        return VII.conjugate_ALL(verb[0], verb[3])
    if verb[2] == "VAI":
        return VAI.conjugate_ALL(verb[0])

if __name__ == '__main__':
   print()