"""
=======================////// SNOCover //////=============================
   NAME: SNOCover_methods.py

   Project:  SNOCover

   CREATED: Marcus Kwong

   FUNCTION: SNOCover methods list

   ENVIRONMENT: Python 3.8.6

   STATUS: Pre-release/Developmental

   VERSION: 0.1

   SYSTEM DEPENDENCIES:

   
=======================////// iMS //////=============================
"""

# ========== PACKAGES ========== #
from KwongmGeneralMethods import is_ascii

# ========== GLOBAL VARIABLES ========== #
STOP_WORDS = [' the ', ' or ', ' if ', ' of ', ' at ', ' on ', ' then ', ' after ', ' than ', ' in ', ' and ', ' that ', ' might ', ' have ', ' been ']
PUNCTUATION = ['-', '\\', '%', '!', '(', ')', '[', ']', '"', '.', ':', ';', ',']
STOPWORDS_AND_PUNCT = [' the ', ' or ', ' if ', ' of ', ' at ', ' on ', ' then ', ' after ', ' than ', ' in ', ' and ', ' that ', ' might ', ' have ', ' been ', 
                    '-', '\\', '%', '!', '(', ')', '[', ']', '"', '.', ':', ';', ',']

# ========== METHODS ========== #

# load a .txt file containing list of SNOMED terms and output as a 2d array
def testFunc():
    print("connected to SNOCover_methods.py!")

# === LOADING === #
# load the SNOMED CT description file and output contents as a 2D array. 
def loadFile(filename):
    array_2d = []

    # NOTE: without 'encoding="utf8"' included, this gives a Unicodedecodeerror
    with open(filename, 'r', encoding="utf8") as file:
            for line in file.readlines():
                array_2d.append(line.split('\t'))

    return array_2d

# === FILTERING COLUMNS === #

# grab both the terms and concept_ids columns from the SNOMED CT description file. 
def filterConceptIDAndTerm(file):
    concept_ids_and_terms = []
    for line in file:
        concept_ids_and_terms.append([line[4], line[7]])
    return concept_ids_and_terms

# grab the terms column from the SNOMED CT description file.
def filterTerms(file):
    terms = []
    for line in file:
        terms.append(line[7])
    return terms

# grab the concept_ids column from the SNOMED CT description file.
def filterConceptIds(file):
    concept_ids = []
    for line in file:
        concept_ids.append(line[4])
    return concept_ids

# === PREPROCESSING === #

# find all non-ascii characters (>128 and <32) from a given .txt file.
def findNonAsciiCharacters(file):

    non_ascii_set = []
    for line in file:
        for i in range(len(line)):
            if is_ascii(line[i]):
                continue
            else:
                if ord(line[i]) == 160:
                    line.replace(line[i], ' ')
                else:
                    if line[i] not in non_ascii_set:
                        non_ascii_set.append(line[i])
    return non_ascii_set

# build a non-ascii to ascii replacement char dictionary from a txt file.
def stopWordDictCreation(filename):
    non_ascii_characers = []
    ascii_replacements = []
    with open(filename, 'r', encoding="utf8") as file:
        for line in file.readlines():
            non = line.split(':')[0]
            rep = line.split(':')[1].rstrip()
            non_ascii_characers.append(non)
            ascii_replacements.append(rep)

    res = {non_ascii_characers[i]: ascii_replacements[i] for i in range(len(non_ascii_characers))}

    return res

# replace all non-ascii values in SNOMED CT description file terms list using a non-ascii to ascii replacement dictionary.

def replaceNonAsciiChars(file, dict):

    # num = 0
    # lines_changed = []

    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] in dict:
                #num += 1
                #lines_changed.append(i)

                t = dict[file[i][j]]
                # print("Changing: ", file[i])
                file[i] = file[i].replace(file[i][j], t)
                # print("Result: ", file[i])

    # print("total lines changed: ", num)
    return file

# remove stop words in SNOMED CT description file terms list from a list of stop words. 

def removeStopWords(list):
    c = 0

    for i in range(len(list)):
        #print("checking: ", list[i])
        for j in range(len(STOPWORDS_AND_PUNCT)):
            if STOPWORDS_AND_PUNCT[j] in list[i]:
                c = c + 1
                list[i] = list[i].replace(STOPWORDS_AND_PUNCT[j], '$')
        list[i] = list[i].replace('$', ' ')

    return list

# output the list of tuples (term, concept id) and output them to a .txt file for further analysis.

def outputSortedTermsAndConceptsTuples(list):
    file_object = open("sorted_snomed_terms_and_concepts_list.txt", "w")
    
    for i in range(len(list)):
        add_term = list[i][0].strip()
        add_concept_id = list[i][1].strip()
        file_object.write(list[i][0] + ':' + list[i][1] + '\n')

    file_object.close()

# find the identifiers that a snomed term may contain to be used for removal, as these may affect nlp stemming/tagging later on.
# ex. Esophageal injury (disorder) ---> want to extract (disorder).


# === PREPROCESSING OUT ONLY DIAGNOSES === #

def findIdentifiers(list):

    identifiers = []

    for i in range(len(list)):
        if ("(" in list[i]) and (")" in list[i]):
            to_add = list[i].split("(")

            to_add = "(" + to_add[-1]

            a = to_add.split(")")

            # if the subset of str after ')' is empty or only contains whitespace, we know this is an identifier.
            # Thus, we add it to the list. 
            # ex. 'CYP3A4 (cytochrome P450  member 4) high intermediate' --> subset after ')' is 'high intermediate', which is not empty nor whitespace.
            # ex. 'Peritoneal dialysis solution (qualifier value)' --> subset after ')' is nothing, so we add it. 

            if len(a) > 1:
                if (a[1].isspace()) or (not a[1]):
                    to_add = a[0] + ")"
                    identifiers.append(to_add)
    
    return identifiers