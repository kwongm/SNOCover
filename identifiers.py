from SNOCover_methods import *
from SNOCover_preprocessing import *
from KwongmGeneralMethods import askUser

snapshot_desc_file = "snomed_03012021_snapshot_description.txt"
file = loadFile(snapshot_desc_file)


filtered_file = filterConceptIDAndTerm(file)
terms = filterTerms(file)
concept_ids = filterConceptIds(file)

# get list of identifiers

identifiers = findIdentifiers(terms)

identifiers = list(set(identifiers))

print(len(identifiers))

for i in range(len(identifiers)):
    print(identifiers[i])