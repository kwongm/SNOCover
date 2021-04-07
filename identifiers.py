from SNOCover_methods import *
from SNOCover_preprocessing import *
from KwongmGeneralMethods import askUser

snapshot_desc_file = "snomed_03012021_snapshot_description.txt"
file = loadFile(snapshot_desc_file)


filtered_file = filterConceptIDAndTerm(file)
terms = filterTerms(file)
concept_ids = filterConceptIds(file)

"""# get list of identifiers

identifiers = findIdentifiers(terms)

identifiers = list(set(identifiers))

print(len(identifiers))

#for i in range(len(identifiers)):
#    print(identifiers[i])

print(type(identifiers))

print(type(identifiers[0]))
print(identifiers[0])"""

tuples = []

merged_list = [(concept_ids[i], terms[i]) for i in range(0, len(terms))]

sorted_list = sorted(merged_list, key=lambda x: x[0])

for i in range(len(sorted_list)):
    print(sorted_list[i])

#file_object.close()