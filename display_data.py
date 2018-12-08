from matplotlib.ticker import FuncFormatter
import pylab
import numpy as np
import matplotlib.pyplot as plt
import random

class DisplayData:
    trafic = []
    stations = []
    quartiers = []

    dic_quartiers = dict()
    trafic_dic = dict()

    """
    retourne 3 lists contenant les noms des stations, le trafic et les quartiers

    Args:
        data: liste contenenat les informations à récupérer

    Returns:
        3 lists contenant les noms des stations, le trafic et les quartiers
    """
    def get_data_about_paris_district(self, data):
        try:
            for elem in data:
                self.stations.append(elem[1])
                self.trafic.append(int(elem[2]))
                self.quartiers.append(elem[4])
                return self.stations, self.trafic, self.quartiers
        except:
            print("data n'est pas une list !")


    """
    retourne un dictionnaire quartiers 

    Args:
        quartiers: liste des quartiers

    Returns:
        un dictionnaire quartiers 
    """
    def get_quartiers_dictionnary(self, quartiers):
        try:
            for elem in quartiers:
                if not not elem:
                    if elem not in self.dic_quartiers.keys():
                        self.dic_quartiers[elem] = 1
                    else:
                        self.dic_quartiers[elem] += 1
            return self.dic_quartiers
        except:
            print("quartiers n'est pas une list !")

    
    """
    retourne un dictionnaire de trafic 

    Args:
        data: liste contenenat les informations à récupérer 

    Returns:
        un dictionnaire de trafic
    """
    def get_trafic_dictionnary(self, data):
        try:
            for elem in data:
                if(elem[4]):
                    if (elem[4] not in self.trafic_dic.keys()):
                        self.trafic_dic[elem[4]] = int(elem[2])
                    else:
                        self.trafic_dic[elem[4]] += int(elem[2])
            return self.trafic_dic
        except:
            print("data n'est pas une list !")


    """
    retourne 2 lists trafic_keys et trafic_values

    Args:
        trafic_dictionnary: liste contenenat les informations à récupérer 

    Returns:
        2 lists trafic_keys et trafic_values
    """
    def get_trafic_keys_and_values_form_dictionnary(self, trafic_dictionnary):
        try:
            trafic_keys = list(int(key) for key in trafic_dictionnary.keys())
            trafic_values = list(trafic_dictionnary.values())
            return trafic_keys, trafic_values
        except:
            print("trafic_dictionnary n'est pas un dictionnaire !")

    
    """
    retourne des informations pour afficher des millions sur l'axe des coordonnées 

    Args:
        x: la valeur de base
        pos: position d'affichage

    Returns:
        es informations pour afficher des millions sur l'axe des coordonnées 
    """
    def millions(self, x, pos):
        return '%1.1fM' % (x * 1e-6)


    """
    Affiche un histogramme sur les information précises

    Args:
        x: la valeur de base
        pos: position d'affichage

    Returns:
        None
    """
    def print_data(self, trafic_keys, trafic_values):
        formatrer = FuncFormatter(self.millions)
        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatrer)

        plt.bar(trafic_keys, trafic_values, ec="black")
        plt.xlabel('Arrondissements')
        plt.ylabel('Taux trafics')
        plt.title('Histogramme trafic entrant dnas les gares de Paris')
        plt.xticks(trafic_keys)
        plt.show()

