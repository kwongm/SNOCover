import os.path

from snocover_identify_nonascii import *

#createListOfNonAsciiCharacters()

if os.path.isfile("nonascii_to_replace.txt"):
    print("exists")
else:
    print("does not exist.")

