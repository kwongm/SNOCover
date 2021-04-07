"""
=======================////// SNOCover //////=============================
   NAME: snocover_identify_nonascii.py

   Project:  SNOCover
   
   CREATED: Marcus Kwong

   FUNCTION: SNOCover preprocessing file : identification of non-ascii characters.
   
   INPUT: SNOMED CT snapshot description .txt file

   OUTPUT: list of non-ascii characters that need to be replaced by user.

   ENVIRONMENT: Python 3.8.6

   STATUS: Pre-release/Developmental

   VERSION: 0.1

   EXTERNAL FILES USED: SNOMED CT March 03, 2021 US Edition

   SYSTEM DEPENDENCIES: 
   
=======================////// iMS //////=============================
"""
from snocover_methods import *
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

   ord_values = []

   for i in range(len(non_ascii_chars)):
      ord_values.append(str(ord(non_ascii_chars[i])))

   print(len(non_ascii_chars))

   print(len(ord_values))

   file_object = open("nonascii_to_replace.txt", "w", encoding="utf-8")
    
   for i in range(len(non_ascii_chars)):

      file_object.write(non_ascii_chars[i] + ':' + ord_values[i] + '\n')

   file_object.close()