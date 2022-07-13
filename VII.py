# -*- coding: UTF-8 -*-
"""
takes:
    order: (independent (ind), conjunct (con))
    tense: (present (prs), past (pst), future intentional (fti), future definite (ftd), ka-infinitive (kin), ta-infinitive (tin), future conditional (ftc))
    person: (0, 0p, 0', 0p')
    extra:
        n: if True, stem final n deleted before -k instead of turning to h
        p: if True, plural forms of this verb are grammatical, if not, not
"""

import morphophon
from pprint import pprint as pp

# nested dict with order-tense-person layers
conjugations = {
    "ind": {
        "prs": {"0": "S-wi", "0p": "S-wah", "0'": "S-eyi-wi", "0p'": "S-eyi-wah"},
        "pst": {"0": "kî!S-wi", "0p": "kî!S-wah", "0'": "kî!S-eyi-wi", "0p'": "kî!S-eyi-wah"},
        "fti": {"0": "wî!S-wi", "0p": "wî!S-wah", "0'": "wî!S-eyi-wi", "0p'": "wî!S-eyi-wah"},
        "ftd": {"0": "ka!S-wi", "0p": "ka!S-wah", "0'": "ka!S-eyi-wi", "0p'": "ka!S-eyi-wah"},
        "ftc": {"0": "S-k-ih", "0p": "S-k-wâw-ih", "0'": "S-eyi-k-ih", "0p'": "S-eyi-k-wâw-ih"},
    },
    "con": {
        "prs": {"0": "ê!S-k", "0p": "ê!S-k-ih", "0'": "ê!S-eyi-k", "0p'": "ê!S-eyi-k-ih"},
        "pst": {"0": "ê!kî!S-k", "0p": "ê!kî!S-k-ih", "0'": "ê!kî!S-eyi-k", "0p'": "ê!kî!S-eyi-k-ih"},
        "fti": {"0": "ê!wî!S-k", "0p": "ê!wî!S-k-ih", "0'": "ê!wî!S-eyi-k", "0p'": "ê!wî!S-eyi-k-ih"},
        "kin": {"0": "ka!S-k", "0p": "ka!S-k-ih", "0'": "ka!S-eyi-k", "0p'": "ka!S-eyi-k-ih"},
        "tin": {"0": "ta!S-k", "0p": "ta!S-k-ih", "0'": "ta!S-eyi-k", "0p'": "ta!S-eyi-k-ih"},
    }
}

#full names of the features
full_names = {"ind": "independent", "con": "conjunct", "prs": "present", "pst": "past", "fti": "future intentional",
              "ftd": "future definite", "ftc": "future conditional", "kin": "ka-infinitive", "tin": "ta-infinitive",
              "0": "singular proximate", "0p": "plural proximate", "0'": "singular obviate", "0p'": "plural obviate"}

# default conjugation, dictionary form
default = ["ind", "prs", "0"]

# conjugate a stem given a conjugation value as a list (in the form order, tense, person) and extras
def conjugate(stem, conjugation=default, extra=[]):
    order, tense, person = conjugation[0], conjugation[1], conjugation[2]
    # checking that the tense/order combination is valid
    if tense not in conjugations[order].keys(): return None
    if person not in conjugations[order][tense].keys(): return None
    # if the stem's not marked as pluralizable, it can't be pluralized
    if "p" not in extra and person in ["0p", "0p'"]: return None
    # get the appropriate conjugation's morphemes
    morphemes = conjugations[order][tense][person]
    # if the stem's marked as having an n that's deleted before k, the n is deleted
    if stem[-1] == "n" and "n" in extra and "S-k" in morphemes: stem = stem[:-1]
    # replace S with the stem and apply the morphophonological rules
    return morphophon.apply_rules(morphemes.replace("S", stem))

# get every conjugation of a stem given extras
def conjugate_ALL(stem, extra=[]):
    conjugated = {}
    for order in conjugations:
        for tense in conjugations[order]:
            for person in conjugations[order][tense]:
                form = conjugate(stem, [order, tense, person], extra)
                if form is not None: conjugated[(order, tense, person)] = form
    return conjugated


if __name__ == "__main__":
    conjugated = conjugate_ALL('miywâsin', extra=["n"])
    pp(conjugated)
