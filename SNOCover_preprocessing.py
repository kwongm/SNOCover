"""
=======================////// SNOCover //////=============================
   NAME: SNOCoer_preprocessing.py

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

from SNOCover_methods import *
from KwongmGeneralMethods import askUser


def preprocessSnomedFile():

    snapshot_desc_file = "snomed_03012021_snapshot_description.txt"
    file = loadFile(snapshot_desc_file)
    filtered_file = filterConceptIDAndTerm(file)
    terms = filterTerms(file)
    concept_ids = filterConceptIds(file)

    # NOTE: variables are passed by REFERENCE, not by value when passed as an argument for a function.
    # In order to preserve the previous list, we must copy the list to another variable instead.
    t = terms[:]

    # grab all the non-ascii characters within the terms list.
    non_ascii_chars = findNonAsciiCharacters(t)

    # build a dictionary that holds non-ascii keys with ascii replacement values.
    non_ascii_dict = stopWordDictCreation("input/non_ascii_characters_and_replacements.txt")

    # remove non-ascii characters from list of terms.
    terms_nonascii_removed = replaceNonAsciiChars(t, non_ascii_dict)
    t1 = terms_nonascii_removed[:]

    # remove stop words from list of terms.

    terms_preprocessed = removeStopWords(t1)

    # merge the preprocessed terms list with the concept ids list into tuples, so that we can then
    # sort the merged list by concept ids. This will set us up for analysis of the # terms per concept id, which
    # we can then look at the different terms/values associated with each concept id. The hope is that these values/terms
    # will assist in the decision-making for how to use each concept id's terms set to correctly map raw text to each. 
    
    merged_list_preprocessed_terms_and_concept_ids = tuple(zip(terms_preprocessed, concept_ids))

    #print(merged_list_preprocessed_terms_and_concept_ids[1])
    #print(merged_list_preprocessed_terms_and_concept_ids[2])

    # Now that the preprocessed terms and concept ids are merged into a list of tuples, we will sort the list by concept id,
    # grouping the terms with the same concept id together for easier analysis. 

    sorted_list_preprocessed_terms_and_concept_ids = sorted(merged_list_preprocessed_terms_and_concept_ids, key=lambda x: x[1])

    #print(sorted_list_preprocessed_terms_and_concept_ids[1])
    #print(min(concept_ids))

    outputSortedTermsAndConceptsTuples(sorted_list_preprocessed_terms_and_concept_ids)

