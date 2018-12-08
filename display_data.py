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
    def display_data_on_histogramme(self, trafic_keys, trafic_values, l1, l2, l3):
        formatrer = FuncFormatter(self.millions)
        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatrer)

        plt.figure(1)
        plt.bar(trafic_keys, trafic_values, ec="black")
        plt.xlabel('Arrondissements')
        plt.ylabel('Taux trafics')
        plt.title('Histogramme trafic entrant dnas les gares de Paris')
        plt.xticks(trafic_keys)

        plt.figure(2)

        # set width of bar
        barWidth = 0.125
        
        NO = []
        NO.append(l1[0])
        NO.append(l2[0])
        NO.append(l3[0])

        NO2 = []
        NO2.append(l1[1])
        NO2.append(l2[1])
        NO2.append(l3[1])

        PM10 = []
        PM10.append(l1[2])
        PM10.append(l2[2])
        PM10.append(l3[2])

        CO2 = []
        CO2.append(l1[3])
        CO2.append(l2[3])
        CO2.append(l3[3])

        # Set position of bar on X axis
        r1 = np.arange(len(NO))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        r4 = [x + barWidth for x in r3]
        
        # Make the plot
        plt.bar(r1, NO, color='#7f6d5f', width=barWidth, edgecolor='white', label='NO')
        plt.bar(r2, NO2, color='#557f2d', width=barWidth, edgecolor='white', label='NO2')
        plt.bar(r3, PM10, color='#2d7f5e', width=barWidth, edgecolor='white', label='PM10')
        plt.bar(r4, CO2, color='#2d725f', width=barWidth, edgecolor='white', label='CO2')
        
        # Add xticks on the middle of the group bars
        plt.ylabel("Indice de qualité de l'air")
        plt.xlabel('Emplacement')
        plt.title("Histogramme des notes des composants de l'air")
        plt.xticks([r + barWidth for r in range(len(NO))], ['Chatelet', 'Roosevelet', 'Auber'])
        plt.yticks([0, 1, 2, 3, 4, 5])
        
        # Create legend & Show graphic
        plt.legend()

        plt.show()

    

