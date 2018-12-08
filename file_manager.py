#coding : utf-8
# pip install truc --update --user
import csv
from collections import namedtuple

class FileManager:

    def __init__(self):
        self.data_pos = [1, 2, 3, 9, 10]

    """
    retourne une list des informations lues dans le ficheir

    Args:
        filename: un fichier au format csv contenant une liste de stations météo

    Returns:
        list des informations dans le fichier
    """
    def get_list_file_content(self, filename):
        try:
            with open(filename, mode='r', encoding='utf8') as file:
                reader = csv.reader(file)
                return list(reader)
        except:
            print("Le fichier n'a pas été trouvé")


    """
    retourne la première ligne de du fichier avec le délimiteur ';' -> str()

    Args:
        list_file_content: list avec le contenu du ficheir

    Returns:
        première ligne de du fichier avec le délimiteur ';' -> str()
    """
    def get_first_line(self, list_file_content):
        try:
            return list_file_content[0][0]
        except:
            print("list_file_content n'est pas une list !")


    """
    retourne la liste du composant de la première ligne -> list()

    Args:
        first_line: la première ligne du ficheir

    Returns:
        la liste du composant de la première ligne -> list()
    """
    def get_first_line_componants(self, first_line):
        try:
            return first_line.split(';')
        except:
            print("list_file_content n'est pas un string !")

    """
    retourne les infomrations qui nous interéssent et prénsetent les entêtes -> list()

    Args:
        first_line_componants: la liste du composant de la première ligne

    Returns:
        les infomrations qui nous interéssent et prénsetent les entêtes
    """
    def get_data_headers_to_use(self, first_line_componants):
        try:
            data_headers_to_use = [first_line_componants[i] for i in range(len(first_line_componants)) if i in self.data_pos]
            return data_headers_to_use
        except:
            print("first_line_componants n'est pas une list !")



    """
    retourne une liste continet les données du fichier, et chaque élément de la liste est une liste -> list()

    Args:
        list_file_content: list avec le contenu du ficheir

    Returns:
        une liste continet les données du fichier, et chaque élément de la liste est une liste
    """
    def get_file_content(self, list_file_content):
        try:
            file_content = []
            for i in range(1, len(list_file_content)):
                if not not list_file_content[i]:
                    file_content.append(list_file_content[i])
            return file_content
        except:
            print("list_file_content n'est pas une list !")



    """
    retourne une liste contient les informations qui nous interéssent

    Args:
        file_content: une liste continet les données du fichier, et chaque élément de la liste est une liste

    Returns:
        une liste contient les informations qui nous interéssent
    """
    def get_informations(self, file_content):
        try:
            informations = []
            for i in range(len(file_content)):
                for j in range(len(file_content[i])):
                    informations.append(file_content[i][j].split(';'))
            return informations
        except:
            print("file_content n'est pas une list !")


        
    """
    retourne une liste des données du fihcier à utiliser

    Args:
        informations: une liste contient les informations qui nous interéssent

    Returns:
        une liste des données du fihcier à utiliser
    """
    def get_data_to_use(self, informations):
        try:
            data_to_use = []
            for elem in informations:
                data_to_use.append([elem[i] for i in range(len(elem)) if i in self.data_pos])
            return data_to_use
        except:
            print("informations n'est pas une list !")


    """
    retourne un tuple TraficData

    Args:
        
    Returns:
        un tuple TraficData
    """
    def get_trafic_data_tuple(self):
        TraficData = namedtuple('TraficData', ['reseau', 'station', 'trafic', 'ville', 'arrondissement_pour_paris'])
        return TraficData


        

    
