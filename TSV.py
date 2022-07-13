# -*- coding: UTF-8 -*-
import csv
from random import choice

#unpack the stems.tsv file into a list and process the columns with multiple values into lists
def unpack():
    tsv = []
    with open("stems.tsv") as file:
        reader_obj = csv.reader(file, delimiter='\t')
        for line in reader_obj:
            if len(line) == 4:
                line[1] = line[1].split(", ")
                if line[3].split(", ") == ['']: line[3]=[]
                else: line[3] = line[3].split(", ")
                tsv.append(line)
        return tsv

# get the line (including definition, verb type, and extras) from the stem
def linefromstem(stem):
    tsv = unpack()
    for line in tsv:
        if line[0] == stem: return line
    return None

# get the line from the index (starting at 1 if positive to be more intuitive for general audiences)
def linefromindex(index):
    tsv = unpack()
    if index == 0: return None
    if index > 0:
        #adjust positive index from starting at 1 to 0
        index-=1
        if len(tsv)-1 < index: return None
    if index < 0:
        if len(tsv)-1 < index * -1: return None
    return tsv[index]

def getRandom(type=None):
    tsv = unpack()
    if type is None: return choice(tsv)
    if type is "VII":
        tsv_VII = []
        for line in tsv:
            if line[2] == "VII": tsv_VII.append(line)
        return choice(tsv_VII)
    if type is "VAI":
        tsv_VAI = []
        for line in tsv:
            if line[2] == "VAI": tsv_VAI. append(line)
        return choice(tsv_VAI)

if __name__ == '__main__':
    for i in range(20):
        x = getRandom("VII")
        print(x[0], x[2]=="VII")
