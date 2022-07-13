# -*- coding: UTF-8 -*-
'''
key = [personAgent, mood]
order: (ind (Independent), con (Conjunct), imp (Imperative))
tense: (present (prs), past (pst), future intentional (fti), future definite (ftd), ka-infinitive (kin), ta-infinitive (tin), future conditional (ftc), immediate (imm), delayed (del))
person: 1, 2, 3, 3', X, 1p, 21, 2p, 3p
'''

from pprint import pprint as pp
import morphophon

# nested dict with order-tense-person layers
conjugations = {
    "ind": {
        "prs": {"1": "ni-S-n", "2": "ki-S-n", "3": "S-wa", "3'": "S-eyi-wa-h",  "X": "S-niwiw",
                "1p": "ni-S-enân", "21": "ki-S-enaw", "2p": "ki-S-enâwâw", "3p": "S-wa-k"},
        "pst": {"1": "nikî!S-n", "2": "kikî!S-n", "3": "kî!S-wa", "3'": "kî!S-eyi-wa-h",
                "1p": "nikî!S-enân", "21": "kikî!S-enaw", "2p": "kikî!S-enâwâw", "3p": "kî!S-wa-k"},
        "fti": {"1": "niwî!S-n", "2": "kiwî!S-n", "3": "wî!S-wa", "3'": "wî!S-eyi-wa-h",
                "1p": "niwî!S-enân", "21": "kiwî!S-enaw", "2p": "kiwî!S-enâwâw", "3p": "wî!S-wa-k"},
        "ftd": {"1": "nika!S-n", "2": "kika!S-n", "3": "ka!S-wa", "3'": "ka!S-eyi-wa-h",
                "1p": "nika!S-enân", "21": "kika!S-enaw", "2p": "kika!S-enâwâw", "3p": "ka!S-wa-k"},
        "ftc": {"1": "S-yân-ih", "2": "S-yan-ih", "3": "S-t-ih", "3'": "S-eyi-t-ih",
                "1p": "S-yâhk-ih", "21": "S-yahkw-ih", "2p": "S-yêkw-ih", "3p": "S-t-wâw-ih"},
    },
    "con": {
        "prs": {"1": "ê!S-yân", "2": "ê!S-yan", "3": "ê!S-t", "3'": "ê!S-eyi-t",  "X": "ê!S-hk",
                "1p": "ê!S-yâhk", "21": "ê!S-yahkw", "2p": "ê!S-yêkw", "3p": "ê!S-t-k"},
        "pst": {"1": "ê!kî!S-yân", "2": "ê!kî!S-yan", "3": "ê!kî!S-t", "3'": "ê!kî!S-eyi-t",
                "1p": "ê!kî!S-yâhk", "21": "ê!kî!S-yahkw", "2p": "ê!kî!S-yêkw", "3p": "ê!kî!S-t-k"},
        "fti": {"1": "ê!wî!S-yân", "2": "ê!wî!S-yan", "3": "ê!wî!S-t", "3'": "ê!wî!S-eyi-t",
                "1p": "ê!wî!S-yâhk", "21": "ê!wî!S-yahkw", "2p": "ê!wî!S-yêkw", "3p": "ê!wî!S-t-k"},
        "kin": {"1": "ka!S-yân", "2": "ka!S-yan", "3": "ka!S-t", "3'": "ka!S-eyi-t",
                "1p": "ka!S-yâhk", "21": "ka!S-yahkw", "2p": "ka!S-yêkw", "3p": "ka!S-t-k"},
        "tin": {"1": "ta!S-yân", "2": "ta!S-yan", "3": "ta!S-t", "3'": "ta!S-eyi-t",
                "1p": "ta!S-yâhk", "21": "ta!S-yahkw", "2p": "ta!S-yêkw", "3p": "ta!S-t-k"},
    },
    "imp": {
        "del": {"2": "S-h", "21": "S-tân", "2p": "S-k"},
        "imm": {"2": "S-hk-an", "21": "S-hk-ahkw", "2p": "S-hk-êkw"},
    },
}

#full names of the features
full_names = {"ind": "independent", "con": "conjunct", "prs": "present", "pst": "past", "fti": "future intentional",
              "ftd": "future definite", "ftc": "future conditional", "kin": "ka-infinitive", "tin": "ta-infinitive",
              "imp": "imperative", "del": "delayed", "imm": "immediate", "1": "first person singular",
              "2": "second person singular", "3": "third person singular proximate", "3'": "third person singular proximate",
              "X": "unknown actor", "1p": "first person plural", "21": "first person plural inclusive",
              "2p": "second person plural exclusive", "3p": "third person plural"}

#default or dictionary form
default = ["ind", "prs", "3"]

# conjugate a stem given a conjugation value as a list (in the form order, tense, person)
def conjugate(stem, conjugation=default):
    order, tense, person = conjugation[0], conjugation[1], conjugation[2]
    #checking that the tense/order combination is valid
    if tense not in conjugations[order].keys(): return None
    if person not in conjugations[order][tense].keys(): return None
    # get the appropriate conjugation's morphemes
    morphemes = conjugations[order][tense][person]
    # if there's an n-t- sequence, the t becomes a k
    morphemes = morphemes.replace("n-t-", "n-k-")
    return morphophon.apply_rules(morphemes.replace("S", stem))

# get every conjugation of a stem
def conjugate_ALL(stem):
    """conjugated = conjugations.copy()
    for order in conjugated:
        for tense in conjugated[order]:
            for person in conjugated[order][tense]:
                conjugated[order][tense][person] = conjugate(stem, [order, tense, person], extra)
    return conjugated"""

    conjugated = {}
    for order in conjugations:
        for tense in conjugations[order]:
            for person in conjugations[order][tense]:
                form = conjugate(stem, [order, tense, person])
                if form is not None: conjugated[(order, tense, person)] = form
    return conjugated

if __name__ == '__main__':
    pp(conjugate_ALL("nipâ"))