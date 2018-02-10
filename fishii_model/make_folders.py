import os 
import re 

f = open('Fishackathon_SpeciesData.csv', "r")
next(f)

fish = []
dirs = []
for line in f:
    line = line.split(',')
    species_id = line[0]
    species = line[1].strip("\n").strip("\r")

    fish.append(species)
    
    species = species.replace(" ", "_")
    folder_name = (species_id + "-" + species)

    # if not os.path.exists(folder_name):
    #     dirs.append(folder_name)

# for directory in dirs:
#     os.mkdir(directory))

fish_set_1 = str(fish[0:10]).replace("'", "")

# fish_set_1 = fish_set[0:50]
# fish_set_2 = fish_set[50:100]

print(fish_set_1)


# http://www.fishbase.org/ComNames/CommonNameSearchList.php?CommonName=Aligator+Gar
    