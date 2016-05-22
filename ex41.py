# python2.x

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/word.txt"
WORDS = []


PHRASES = {
    "class %%%(%%%):":
    " Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that taks self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a funciton named *** that takes self and @@@ parameters.",
    "*** = %%%()":"Set *** to an instance of class %%%",
    "***.***(@@@)":"from *** get the *** function, and call it with parameter self, @@@.",
    "***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "englist":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

