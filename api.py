import requests
import json

import numpy
import matplotlib.pyplot as plt
import math

import folium


class Api:


    def OpenDataIDF(self, s):
        r = requests.get(s)
        data = r.json()
        if("franklin" in s) : 
            specialKey = "fra1"
        if("chatelet" in s) : 
            specialKey = "cha4"
        if("auber" in s) : 
            specialKey = "auba"

        ###########
        ### PM10 ##
        ###########
        #print("\n\n[|> CO2 ANALYSE INITIALIZATION <|]\n\n")
        moyCO2 = 0
        nbCO2 = 0

        ###########
        ### PM10 ##
        ###########
        #print("\n\n[|> PM10 ANALYSE INITIALIZATION <|]\n\n")
        moyPM10 = 0
        nbPM10 = 0

        ###########
        ### NO² ###
        ###########
        #print("\n\n[|> NO2 ANALYSE INITIALIZATION <|]\n\n")
        moyNO2 = 0
        nbNO2 = 0
        
        ##########
        ### NO ###
        ##########
        #print("\n\n[|> NO ANALYSE INITIALIZATION <|]\n\n")
        moyNO = 0
        nbNO = 0
        
        i=0
        for dataRecords in data["records"] :
            ###########
            ### CO2 ###
            ###########
            if "c2"+specialKey in dataRecords["fields"] :
                if(dataRecords["fields"]["c2"+specialKey]) : 
                    moyCO2 = moyCO2 + dataRecords["fields"]["c2"+specialKey]
            nbCO2 = nbCO2 + 1
            
            ###########
            ### PM10 ##
            ###########
            if "10"+specialKey in dataRecords["fields"] :
                moyPM10 = moyPM10 + dataRecords["fields"]["10"+specialKey]
            nbPM10 = nbPM10 + 1
            
            ###########
            ### NO² ###
            ###########
            if "n2"+specialKey in dataRecords["fields"] :
                moyNO2 = moyNO2 + dataRecords["fields"]["n2"+specialKey]
            nbNO2 = nbNO2 + 1 

            ##########
            ### NO ###
            ##########
            if "no"+specialKey in dataRecords["fields"] :
                moyNO = moyNO + dataRecords["fields"]["no"+specialKey]
            nbNO = nbNO + 1 

            i=i+1

        ###########
        ### CO2 ###
        ###########
        #print("\n\n\t[|> START CO2 ANALYSE <|]\n\n")
        moyPM10 = moyPM10/nbPM10

        ###########
        ### PM10 ##
        ###########
        #print("\n\n\t[|> START PM10 ANALYSE <|]\n\n")
        moyPM10 = moyPM10/nbPM10

        ###########
        ### NO² ###
        ###########
        ##print("\n\n\t[|> START NO2 ANALYSE <|]\n\n")
        moyNO2 = moyNO2/nbNO2

        ##########
        ### NO ###
        ##########
        #print("\n\n\t[|> START NO ANALYSE <|]\n\n")
        moyNO = moyNO/nbNO
        return {"resNO2": moyNO2, "resPM10": moyPM10, "resCO2": moyCO2, "resNO": moyNO}


    def graduateAirQuality(self, dict) :
	    return(round((dict["resNO"]/30)+(dict["resNO2"]/200)+(dict["resPM10"]/80)+(dict["resCO2"]/1000))/4)

    def graduateAireQualityByIndice(self, dict) :
        return({"NO" : round((dict["resNO"]/300)*5), "NO2" : round((dict["resNO2"]/200)*5), "PM10" : round((dict["resPM10"]/40)*5), "CO2" : round((dict["resCO2"]/10000)*5)})

    def dictToList(self, dict):
        resList = list()
        for elm in dict.values():
            resList.append(elm)
        return resList

    def airQualityDataMap(self,s, dict):
        if("franklin" in s) : 
            coords = (48.8692139,2.30941770000004)
        if("chatelet" in s) : 
            coords = (48.8577285,2.346310399999993)
        if("auber" in s) : 
            coords = (48.8724059 ,2.329933799999935)

        graduateData = dict
        res = {"coords": coords, "indice" : graduateData}
        return res

