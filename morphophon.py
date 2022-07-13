# -*- coding: UTF-8 -*-

'''
NOTES:
    θ is never pronounced /θ/ as implied, but is pronounced the same as t, except for that they palatalize differently.
    nehiyawewin doesn't have a short e in pronunciation, but one's existence underlyingly can be observed via morphophonology.
    some roots have a surface t that can't palatalize at all, will need to represent this with a third character i guess.
    some things in the grammar say "only X values are attested", does this mean the other values are known not to work or its not clear?
    monosyllabic roots don't contract
    some disyllabic stems seem to have contracted and uncontracted forms?
    contraction sometimes but not always happens during derivation

'''

consonants = ['p', 't', 'c', 'k', 's', 'h', 'm', 'n', 'θ']
semivowels = ['w', 'y']
vowels = ['ê', 'e', 'i', 'o', 'a', 'î', 'ô', 'â']
palatalizing = ['i', 'î', 'y']
shortvowels = ['e', 'i', 'o', 'a']
longvowels = ['ê', 'î', 'ô', 'â']
lengthen = {'e': 'ê', 'i': 'î', 'o': 'ô', 'a': 'â', 'ê': 'ê', 'î': 'î', 'ô': 'ô', 'â': 'â'}
init_change = {'i': 'ê', 'e': 'ê', 'a': 'ê', 'o': 'wê', 'î': 'iyî', 'ê': 'iyê', 'â': 'iyâ', 'ô': 'iyô'}

def apply_rules(word): #word with morphemes separated by hyphens, including special symbols /θ/, /e/, and /L/
    # double w is shortened at morpheme boundries
    # w > Ø / w-_
    word = word.replace('w-w', 'w')

    # nasals turn to preaspiration before t and k at morpheme boundries
    # [m,n] > h / _-[t,k]
    word = word.replace('m-k', 'hk')
    word = word.replace('m-t', 'ht')
    word = word.replace('n-k', 'hk')
    word = word.replace('n-t', 'ht')

    # i epenthesized between consonants at morpheme boundaries
    # Ø > i / C-_C
    splits, tracker = splitinto(word, 3), [False] * len(word) # tracker marks which character to insert 'i' before
    for index in range(len(splits)):
        if (splits[index][0] in consonants) and (splits[index][1] == '-') and (splits[index][2] in consonants): tracker[index+2] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + 'i' + word[index:]

    # palatalization at morpheme boundaries
    # θ, t > s, c / _-[i, î, y]
    word = word.replace('θ-i', 'si')
    word = word.replace('θ-î', 'sî')
    word = word.replace('θ-y', 'sy')
    word = word.replace('t-i', 'ci')
    word = word.replace('t-î', 'cî')
    word = word.replace('t-y', 'cy')

    # epenthesis of 'y' between long vowels at morpheme boundaries
    # Ø > y / V[+long]_-V[+long]
    splits, tracker = splitinto(word, 3), [False] * len(word) # tracker marks which character (hyphen) to turn into a 'y'
    for index in range(len(splits)):
        if (splits[index][0] in longvowels) and (splits[index][1] == '-') and (splits[index][2] in longvowels): tracker[index+1] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + 'y' + word[index+1:]

    # deletion of short vowel before long vowel at morpheme boundaries
    # V[+short] > Ø / _-V[+long]
    splits, tracker = splitinto(word, 3), [False] * len(word)  # tracker marks which character (vowel) to delete
    for index in range(len(splits)):
        if (splits[index][0] in shortvowels) and (splits[index][1] == '-') and (splits[index][2] in longvowels): tracker[index] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + word[index + 2:]

    # deletion of short vowel after long vowel at morpheme boundaries
    # V[+short] > Ø / V[+long]-_
    splits, tracker = splitinto(word, 3), [False] * len(word)  # tracker marks which characters (hyphen+vowel) to delete
    for index in range(len(splits)):
        if (splits[index][0] in longvowels) and (splits[index][1] == '-') and (splits[index][2] in shortvowels): tracker[index+1] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + word[index+2:]



    #!!!!!!!!!!!!!!!!!!!!! does this need to only be with V-e?
    # deletion of short vowel after short vowel at morpheme boundaries
    # V[+short] > Ø / V[+short]-_
    splits, tracker = splitinto(word, 3), [False] * len(word)  # tracker marks which characters (hyphen+vowel) to delete
    for index in range(len(splits)):
        if (splits[index][0] in shortvowels) and (splits[index][1] == '-') and (splits[index][2] in shortvowels): tracker[index + 1] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + word[index + 2:]

    # lengthening of short vowels before lengthening morpheme
    # V[+short]-L > V[+long]
    splits, tracker = splitinto(word, 3), [False] * len(word)  # tracker marks which vowel to lengthen and delete the -L after
    for index in range(len(splits)):
        if (splits[index][0] in shortvowels) and (splits[index][1:3] == '-L'): tracker[index] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + lengthen[word[index]] + word[index + 3:]

    # o-w > ôw
    word = word.replace('o-w', 'ôw')

    # interconsonantally, we and wi at morpheme boundries become o
    # [w-e, w-i] > o / C_C
    splits, tracker = splitinto(word, 5), [False] * len(word)  # tracker marks the relevant w
    for index in range(len(splits)):
        if (splits[index][0] in consonants) and (splits[index][1:3] == 'w-') and (splits[index][3] in ['e', 'i']) and (splits[index][4] in consonants):
            tracker[index+1] = True
    for index in range(len(tracker)):
        if tracker[index]: word = word[:index] + 'o' + word[index + 3:]

    # !!!!! Should i make it only for /i, a, î, ê, â, ô/ for w and /i, a, o/ for y?
    # !!!!! somehow make it not contract monosyllabic roots
    # Vowel followed by a semivowel, morpheme boundary, and e lengthen and delete the rest
    # V > V[+long] / _[w, y]-e

    splits, tracker = splitinto(word, 4), [False] * len(word)  # tracker marks the vowel to lengthen
    for index in range(len(splits)):
        if (splits[index][0] in vowels) and (splits[index][1] in semivowels) and (splits[index][2:4] == '-e'):
            tracker[index] = True
    for index in range(len(tracker)):
        if tracker[index]:
            word = word[:index] + lengthen[word[index]] + word[index + 4:]

    #remove morpheme boundries, leftover length morphemes, and insert new hyphens
    word = word.replace("-", "")
    word = word.replace("!", "-")
    word = word.replace("L", "")

    # short vowels deleted word finally if the stem isn't monosyllabic (sometimes still if the vowels long, not sure what to do about that)
    # V[+short] > Ø / _#
    num_vowels = 0
    for character in word:
        if character in vowels: num_vowels += 1
    if word[-1] in shortvowels and num_vowels > 2: word = word[:-1]

    # w deleted word finally postconsonantally
    # w > Ø / C_#
    if (word[-1] == "w") and (word[-2] in consonants): word = word[:-1]
    # unpalatalized θ is realized as t
    # θ > t
    word = word.replace("θ", "t")

    # short e is realized as i
    # e > i
    word = word.replace("e", "i")

    # !!!!! should I remove word final h here?
    # word final h deleted
    # h > Ø / _#
    if word[-1] == "h": word = word[:-1]

    return word

def diminuitive_palatalization(word): #the particular type of palatalization associated with diminuitive morphology, palatalizing all ts and θs
    word = word.replace("θ", "c")
    word = word.replace("t", "c")
    return word

def splitinto(word, size):
    splits = []
    for index in range(len(word)-(size-1)):
        splits.append(word[index:index+size])
    return splits

def verb_prefixes(word):
    #t inserted between end of person prefixes and stem vowel instead of vowel leveling as expected
    #are there occasions where anything could be prefixed to the verb before the person? think not
    if word[:3] in ['ni-', 'ki-', 'mi-']:
        if word[3] in vowels: word = word[:2] + 't' + word[3:]
        else: word = word[:2] + word[3:]
    if word[:2] == 'o-':
        if word[2] in vowels: word = word[:1] + 't' + word[2:]
        else: word = word[:1] + word[2:]
    return word

def noun_prefixes(word, reduced = True):
    # reduced is just in some vowel dependent stems, one consonant
    if reduced: #technically probably can get rid of the non-vowel inital parts
        if word[:3] in ['ni-', 'ki-', 'mi-']:
            if word[3] == 'o': word = word[:1] + 'ô' + word[4:]
            elif word[3] in vowels: word = word[:1] + word[3:]
            else: word = word[:2] + word[3:]
        if word[:2] == 'o-':
            if word[2] in ['o','ô']: word = "ô" + word[3:]
            elif word[2] in vowels: word = 'w' + word[2:]
            else: word = word[:1] + word[2:]
        return word
    else:
        if word[:3] in ['ni-', 'ki-', 'mi-']:
            if word[3] == 'o': word = word[:2] + 'tô' + word[4:]
            elif word[3] in vowels: word = word[:2] + 't' + word[3:]
            else: word = word[:2] + word[3:]
        if word[:2] == 'o-':
            if word[2] == 'o': word = 'otô' + word[3:]
            elif word[2] in vowels: word = 'ot' + word[2:]
            else: word = word[:1] + word[2:]
        return word

def initial_change(word):
    #find initial vowel
    first_vowel = -1
    for index in range(len(word)):
        if word[index] in vowels and first_vowel == -1: first_vowel=index
    return word[:first_vowel] + init_change[word[first_vowel]] + word[first_vowel+1:]


if __name__ == '__main__':
    print(apply_rules("ah"))
