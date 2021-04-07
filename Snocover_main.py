"""
=======================////// SNOCover //////=============================
   NAME: Main.py

   Project:  SNOCover
   
   CREATED: Marcus Kwong

   FUNCTION: SNOCover main program

   ENVIRONMENT: Python 3.8.6

   STATUS: Pre-release/Developmental

   VERSION: 0.1

   EXTERNAL FILES USED: SNOMED CT March 03, 2021 US Edition

   SYSTEM DEPENDENCIES:
   
=======================////// iMS //////=============================
"""

# ========== Packages ========== #

from snocover_methods import *
from snocover_preprocessing import *
from KwongmGeneralMethods import askUser



# ========== MAIN ========== #
def main():
    preprocessSnomedFile()

if __name__ == "__main__":
    main()

