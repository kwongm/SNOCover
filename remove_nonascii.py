"""
=======================////// SNOCover //////=============================
   NAME: Main.py

   Project:  SNOCover
   
   CREATED: Marcus Kwong

   FUNCTION: SNOCover preprocessing file : identification and replacement of non-ascii characters

   ENVIRONMENT: Python 3.8.6

   STATUS: Pre-release/Developmental

   VERSION: 0.1

   EXTERNAL FILES USED: SNOMED CT March 03, 2021 US Edition

   SYSTEM DEPENDENCIES: 
   
=======================////// iMS //////=============================
"""
from SNOCover_methods import *
from KwongmGeneralMethods import askUser

# PART I: Find all non-ascii terms within a .txt file containing a list of SNOMED CT terms.
# PART II: Take a .txt file containing a list of SNOMED CT terms, and replace all the non-ascii characters with ascii replacements. 