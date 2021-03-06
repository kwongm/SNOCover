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

SNOMED_FILE = "snomed_03012021_snapshot_description.txt"

# Find all non-ascii terms within a .txt file containing a list of SNOMED CT terms.
# Outputs a list of all non-ascii characters found in the SNOMED CT file. The User
# will need to go through this list an assign replacement values for each one.  

    # grab all the non-ascii characters within the terms list.
def createListOfNonAsciiCharacters():

   file = loadFile(SNOMED_FILE)

   # === Isolate terms and concept Ids columns into 2 lists === #
   filtered_file = filterConceptIDAndTerm(file)
   terms = filterTerms(file)
   concept_ids = filterConceptIds(file)
   non_ascii_chars = findNonAsciiCharacters(terms)

   for i in range(len(non_ascii_chars)):
      print(non_ascii_chars[i] + ':')

   print(len(non_ascii_chars))