# -*- coding: UTF-8 -*-

#convert short grammatical tags to whole phrases
def tags(tags, line = ["", "", "", ""]):
    label = f'{lengthen(tags[2])} {lengthen(tags[0])} {lengthen(tags[1])}'
    # removing redundancies
    label = label.replace("independent future conditional", "future conditional")
    label = label.replace("independent future definite", "future definite")
    label = label.replace("conjunct ka-infinitive", "ka-infinitive")
    label = label.replace("conjunct ta-infinitive", "ta-infinitive")
    if line[2] == "VII" and "p" not in line[3]: label = label.replace("singular ", "")
    return label

def lengthen(tag):
    full_names = {"0": "singular proximate", "0p": "plural proximate", "0'": "singular obviate",
                  "0p'": "plural obviate", "1": "first person singular", "2": "second person singular",
                  "3": "third person singular proximate", "3'": "third person singular obviate",
                  "X": "unknown actor", "1p": "first person plural", "21": "first person plural inclusive",
                  "2p": "second person plural exclusive", "3p": "third person plural", "ind": "independent",
                  "con": "conjunct", "prs": "present", "pst": "past", "fti": "future intentional",
                  "ftd": "future definite", "ftc": "future conditional", "kin": "ka-infinitive", "tin": "ta-infinitive",
                  "imp": "imperative", "del": "delayed", "imm": "immediate"}
    if tag in full_names.keys(): return full_names[tag]
    else: return None

def shorten(phrase):
    short_names = {'singular proximate': '0', 'plural proximate': '0p', 'singular obviate': "0'", 'plural obviate': "0p'",
     'first person singular': '1', 'second person singular': '2', 'third person singular proximate': "3'",
     'unknown actor': 'X', 'first person plural': '1p', 'first person plural inclusive': '21',
     'second person plural exclusive': '2p', 'third person plural': '3p', 'independent': 'ind', 'conjunct': 'con',
     'present': 'prs', 'past': 'pst', 'future intentional': 'fti', 'future definite': 'ftd',
     'future conditional': 'ftc', 'ka-infinitive': 'kin', 'ta-infinitive': 'tin', 'imperative': 'imp', 'delayed': 'del',
     'immediate': 'imm'}

    if phrase in short_names: return short_names[phrase]
    else: return None

#currently can't enter long vowel characters in the input dialouge, so i'm changing them to double vowels
def LV(word):
    word = word.replace("ê", "ee")
    word = word.replace("â", "aa")
    word = word.replace("î", "ii")
    word = word.replace("ô", "oo")
    word = word.replace("ē", "ee")
    word = word.replace("ā", "aa")
    word = word.replace("ī", "ii")
    word = word.replace("ō", "oo")
    return word

if __name__ == '__main__':
    print(tags(("ind","prs","0")))