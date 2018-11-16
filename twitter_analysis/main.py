from twitter_analysis import display_analysis as da
from ast import literal_eval


with open("../CandidateData/candidates.txt") as candidates:
    names_str= candidates.read() # récupération des noms des candidats
    names_dict = literal_eval(names_str)
    ids=[]
for id in names_dict:
    ids.append(id)

da.display(ids)
