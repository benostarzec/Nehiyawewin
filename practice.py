# -*- coding: UTF-8 -*-
import TSV, conjugate, formatting as f
from pprint import pprint
from random import choice

# practice conjugations of a verb stem, given that stem or its index (positive starting at 1, not 0) in the TSV
# stem prioritized over index
def get_verb_info(stem="", index=None):
    # try to get the line from the stem
    line = None
    if stem is not "":
        line = TSV.linefromstem(stem)
    if index is not None:
        line = TSV.linefromindex(index)
    if line is None: print('Unfortunately your input didn\'t correspond to a stem.')
    return line

def restart(method):
    method()

def choose_verb():
    randomStem = 0
    # figure out what verb they want to practice with
    while randomStem not in ["1", "2", "3"]:
        randomStem = input(
            "Please answer 1 if you know what stem you want to practice, 2 if you want a random stem from a certain verb type,\n "
            "or 3 if you want a totally random one. ").strip()
        if randomStem not in ["1", "2", "3"]: print("Sorry, that wasn't a valid answer")
    # get random stem
    if randomStem == "3":
        line = TSV.getRandom()
    # get random stem from category
    elif randomStem == "2":
        vtype = "a"
        while vtype.upper() not in ["VII", "VAI"]:
            vtype = input("What type do you want to practice? VII or VAI?\n").strip()
            if vtype.upper() == "VII":
                line = TSV.getRandom("VII")
            elif vtype.upper() == "VAI":
                line = TSV.getRandom("VAI")
            else:
                print("Sorry, that wasn't a valid verb type")
    # get stem from index or stem
    elif randomStem == "1":
        line = None
        while line == None:
            key = input(
                "Please enter the stem you want to practice with, or its index in the stems.tsv file (the first verb is at index 1). ").strip()
            try:
                line = get_verb_info(index=int(key))
            except ValueError:
                line = get_verb_info(stem=key)
    return line

def get_orders():
    # figure out what orders they want to practice
    orders, satisfied, ret = None, False, []
    valid = ["ind", "con"]
    valid_string = ""
    for order in valid:
        valid_string += f.lengthen(order) + ", "
    valid_string = valid_string[:-2]
    while not satisfied:
        print("The orders are as follows: " + valid_string)
        orders = input(
            "If you want to practice both orders, enter 'all', otherwise enter each order you want to practice seperated by a comma and space. ")\
            .lower().strip().split(", ")
        for index in range(len(orders)):
            orders[index] = orders[index].replace(",", "").strip()
        if "all" in orders:
            ret = valid
        else:
            for order in orders:
                if order in valid and order not in ret: ret.append(order)
                else:
                    short = f.shorten(order)
                    if short in valid and short not in ret: ret.append(short)
        if ret == []:
            print('That input wasn\'t valid. Please enter "all", "conjunct", or "independent"')
            satisfied = False
        else: satisfied = True
    return ret

def get_tenses():
    # figure out what orders they want to practice
    tenses, satisfied, ret = None, False, []
    valid = ['prs', 'pst', 'fti', 'ftd', 'ftc', 'fti', 'tin', 'kin']
    valid_string = ""
    for tense in valid:
        valid_string += f.lengthen(tense) + ", "
    valid_string = valid_string[:-2]
    while not satisfied:
        print("The tenses are as follows: " + valid_string)
        tenses = input(
            "If you want to practice all tenses, enter 'all', otherwise enter each tense you want to practice seperated by a comma and space. ")\
            .lower().strip().split(", ")
        for index in range(len(tenses)):
            tenses[index] = tenses[index].replace(",","").strip()
        if "all" in tenses:
            ret = valid
        else:
            for tense in tenses:
                if tense in valid and tense not in ret: ret.append(tense)
                else:
                    short = f.shorten(tense)
                    if short in valid and short not in ret: ret.append(short)
        if ret == []:
            print('That input wasn\'t valid. Please enter "all", "conjunct", or "independent"')
            satisfied = False
        else: satisfied = True
    return ret

def get_persons(line):
    # figure out what orders they want to practice
    tenses, satisfied, ret = None, False, []
    if line[2] == "VII" and "p" in line[3]: valid = ["0", "0p", "0'", "0p'"]
    elif line[2] == "VII": valid = ["0", "0'"]
    elif line[2] == "VAI": valid = ["1", "2", "3", "3'", "X", "1p", "21", "2p", "3p"]
    valid_string = ""
    for person in valid:
        valid_string += f.lengthen(person) + ", "
    valid_string = valid_string[:-2]
    while not satisfied:
        print("The persons are as follows: " + valid_string)
        persons = input(
            "If you want to practice all persons, enter 'all', otherwise enter each person you want to practice seperated by a comma and space. ")\
            .lower().strip().split(", ")
        for index in range(len(persons)):
            persons[index] = persons[index].replace(",", "").strip()
        if "all" in persons:
            ret = valid
        else:
            for person in persons:
                if person in valid and person not in ret: ret.append(person)
                else:
                    short = f.shorten(person)
                    if short in valid and short not in ret: ret.append(short)
        if ret == []:
            print('That input wasn\'t valid. Please enter "all", "conjunct", or "independent"')
            satisfied = False
        else: satisfied = True
    return ret

def get_answermode():
    answerIn = "0"
    while answerIn not in ["1", "2"]:
        answerIn = input("Enter 1 if you want to answer in Cree (romanized), or enter 2 for Linguistic Labels. ")
        if answerIn not in ["1", "2"]: print("That input was invalid, try again")
    return answerIn

def get_conjugations(line, orders, tenses, persons):
    # get all conjugations
    conjugated = []
    conjugated_dict = conjugate.conjugate_ALL(line)
    for key in conjugated_dict:
        if key[0] in orders:
            if key[1] in tenses:
                if key[2] in persons:
                    conjugated.append((key, f.LV(conjugated_dict[key])))
    return conjugated

def practice_loop(answerIn, conjugated, line):
    # till all forms have been practiced
    if answerIn == "1": print(
        "You will be prompted with the grammatical information and need to answer with the Cree word. To skip, enter skip.")
    if answerIn == "2": print(
        "You will be prompted with the Cree word and need to answer with the grammatical information. To skip, enter skip.")
    while len(conjugated) > 0:
        # get random form
        form = choice(conjugated)
        conjugated.remove(form)
        if answerIn == "1":
            answer = ""
            while answer not in [form[1], "skip"]:
                answer = input(f.tags(form[0], line) + ": ").lower().strip()
                if answer == "skip":
                    print("the correct form was: " + f.LV(form[1]) + ".")
                elif f.LV(answer) != form[1]:
                    print('That was wrong, try again.')
                elif f.LV(answer) == form[1]:
                    print('Good job, that was right!')

        elif answerIn == "2":
            answer = ""
            while answer not in [f.tags(form[0], line), "skip"]:
                answer = input(form[1] + ": ").lower().strip()
                if answer == "skip":
                    print("the correct answer was: " + f.tags(form[0], line) + ".")
                elif answer != form[1]:
                    print('That was wrong, try again.')
                elif answer == form[1]:
                    print('Good job, that was right!')

    print("Good job! That was all the forms.")

def practice_verb():
    line = choose_verb()
    print("you're practicing with the stem " + line[0] + ", which is of type " + line[2] + " and has the primary definition of \"to " + line[1][0] + '"')

    # get answering mode
    answerIn = get_answermode()

    orders = get_orders()
    tenses = get_tenses()
    persons = get_persons(line)

    conjugated = get_conjugations(line, orders, tenses, persons)
    practice_loop(answerIn, conjugated, line)

if __name__ == '__main__':
    practice_verb()