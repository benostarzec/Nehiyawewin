This is a tool developed to help practice the conjugations of 2 of the 4 verb types of Plains Cree. To use the program, call practice.py.
Constituent files:
| File Name | Purpose |
| ---------|---------- |
| grammarnotes.txt: | Notes about Cree grammar, definitions of all the terms needed for verb conjugation. Reccomended to read before use.|
| Morphophon.py: Methods involved with applying Cree's complex morphophonological rules (not all of which are used in the verb practice yet).|
| VII.py: | Methods involving conjugating VII (inanimate intransitive) verbs.|
| VAI.py: | Methods involving conjugating VAI (animate intransitive) verbs.|
| conjugate.py: | A more general set of methods for conjugating verbs, which calls methods from the appropriate file (VII.py or VAI.py) depending on the verb's type|
| stems.tsv: | A file filled with some example stems in the format (stem, meanings, type, extra (unused for VAI, in VII marks whether stem final n dissapears in some conjugations, and whether the verb can pluralize))|
| TSV.py: | Methods for using the TSV file and its information|
| formatting.py: | Methods for formatting things as needed in practice.py|
| practice.py: | Methods used inside of practice_verb(), which is the method that you call to use the whole program, and that method itself.|
| scriptswitch.py: | A yet unused method that can change text from CAS (Canadian Aboriginal Syllabics) to latin script.|
