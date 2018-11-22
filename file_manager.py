#coding : utf-8
# pip install truc --update --user
import csv

from collections import namedtuple

# Positions les données
data_pos = [1, 2, 3, 9, 10]


###################################
#    Ouverture de fichier
###################################
with open('files/trafic-annuel-entrant-par-station-du-reseau-ferre-2016.csv', mode='r', encoding='utf8') as file:
    reader = csv.reader(file)
    list_file_content = list(reader)


###################################
# Première ligne de du fichier avec le délimiteur ';' -> str()
first_line = list_file_content[0][0]

# Liste du composant de la première ligne -> list()
first_line_componants = first_line.split(';')

# Les infomrations qui nous interéssent et prénsetent les entêtes -> list()
data_headers_to_use = [first_line_componants[i] for i in range(len(first_line_componants)) if i in data_pos]

# Liste continet les données du fichier, et chaque élément de la liste est une liste -> list()
file_content = list()

# Récupérantion de données
for i in range(1, len(list_file_content)):
    if not not list_file_content[i]:
        file_content.append(list_file_content[i])

# Liste contient les informations qui nous interéssent
informations = list()

# Traitement de données, élimination du délimiteur pour chaque ligne de données
for i in range(len(file_content)):
    for j in range(len(file_content[i])):
        informations.append(file_content[i][j].split(';'))

# Données du fihcier à utiliser
data_to_use = list()

# Récupération de données
for elem in informations:
    data_to_use.append([elem[i] for i in range(len(elem)) if i in data_pos])

# Création d'un tuple
TraficData = namedtuple('TraficData', ['reseau', 'station', 'trafic', 'ville', 'arrondissement_pour_paris'])

#td = TraficData(data_to_use[0][0], data_to_use[0][1], data_to_use[0][2], data_to_use[0][3], data_to_use[0][4])