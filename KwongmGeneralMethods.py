
"""
=======================////// SNOCover //////=============================
   NAME: KwongmGeneralMethods.py

   Project:  SNOCover

   FUNCTION: General methods for usage

   ENVIRONMENT: Python 3.8.6

   STATUS: Pre-release/Developmental

   CREATED: Marcus Kwong

   VERSION: 0.1

   SYSTEM DEPENDENCIES:

   
=======================////// iMS //////=============================
"""


def askUser(question):
    answer = input(question)
    return answer

def is_ascii(s):
    return all(ord(c) < 128 and ord(c) > 31 for c in s)
