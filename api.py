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

        ##print("\n\n[|> data <|]\n\n")
        ##print(data)

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
        #print("\n\n[|> START JSON DUMP <|]\n\n")
        for dataRecords in data["records"] :
            
            #recuperer annee courante
            #if("2018" in dataRecords["record_timestamp"]) :
                #print("Condition complete \n")
                #Moyenne des donnees pour lannee courante

            ###########
            ### CO2 ###
            ###########
            if "c2"+specialKey in dataRecords["fields"] :
                if(dataRecords["fields"]["c2"+specialKey]) : 
                    #print(dataRecords["fields"])
                    moyCO2 = moyCO2 + dataRecords["fields"]["c2"+specialKey]
                    #if dataRecords["fields"]["c2"+specialKey] > 750:
                        #print("\tCO2 : ["+str(dataRecords["fields"]["c2"+specialKey])+"] [WARNING : High quantity of PM10]")
                    #if dataRecords["fields"]["c2"+specialKey] < 250:
                        #print("\tCO2 : ["+str(dataRecords["fields"]["c2"+specialKey])+"] [Very Good quantity detected]")
                    #if dataRecords["fields"]["c2"+specialKey] < 750 and dataRecords["fields"]["c2"+specialKey] > 250:
                        #print("\tCO2 : ["+str(dataRecords["fields"]["c2"+specialKey])+"] [Good quantity detected]")
            nbCO2 = nbCO2 + 1
            
            ###########
            ### PM10 ##
            ###########
            if "10"+specialKey in dataRecords["fields"] :
                moyPM10 = moyPM10 + dataRecords["fields"]["10"+specialKey]
                #if dataRecords["fields"]["10"+specialKey] > 199:
                    #print("\tPM10 : ["+str(dataRecords["fields"]["10"+specialKey])+"] [WARNING : High quantity of PM10]")
                #else :
                    #print("\tPM10 : ["+str(dataRecords["fields"]["10"+specialKey])+"] [Good quantity detected]")
            nbPM10 = nbPM10 + 1
            
            ###########
            ### NO² ###
            ###########
            if "n2"+specialKey in dataRecords["fields"] :
                moyNO2 = moyNO2 + dataRecords["fields"]["n2"+specialKey]
                #if dataRecords["fields"]["n2"+specialKey] <100:
                    #print("\tNO² : ["+str(dataRecords["fields"]["n2"+specialKey])+"] [Good quantity detected]")
                #if dataRecords["fields"]["n2"+specialKey] > 199:
                    #print("\tNO² : ["+str(dataRecords["fields"]["n2"+specialKey])+"] [WARNING : High quantity of NO2]")
                #if dataRecords["fields"]["n2"+specialKey] > 100 and dataRecords["fields"]["n2"+specialKey] <199:
                    #print("\tNO² : ["+str(dataRecords["fields"]["n2"+specialKey])+"]")
            nbNO2 = nbNO2 + 1 

            ##########
            ### NO ###
            ##########
            if "no"+specialKey in dataRecords["fields"] :
                moyNO = moyNO + dataRecords["fields"]["no"+specialKey]
                #if dataRecords["fields"]["no"+specialKey] <100:
                    #print("\tNO : ["+str(dataRecords["fields"]["no"+specialKey])+"] [Good quantity detected]")
                #if dataRecords["fields"]["no"+specialKey] > 199:
                    #print("\tNO : ["+str(dataRecords["fields"]["no"+specialKey])+"] [WARNING : High quantity of NO]")
                #if dataRecords["fields"]["no"+specialKey] > 100 and dataRecords["fields"]["no"+specialKey] <199:
                    #print("\tNO : ["+str(dataRecords["fields"]["no"+specialKey])+"]")
            nbNO = nbNO + 1 

            i=i+1

        #print("\n\n\t[|> ____________________________________________________________________________ <|]\n\n")

        ###########
        ### CO2 ###
        ###########
        #print("\n\n\t[|> START CO2 ANALYSE <|]\n\n")
        moyPM10 = moyPM10/nbPM10
        #print("\n\tmoyCO2 = ["+str(moyCO2)+"]\n\tBased on "+str(nbCO2)+" sample CO2\n\tResult : [No state defined]")
        #print("\n\n\t[|> END PM10 ANALYSE <|]\n\n")

        ###########
        ### PM10 ##
        ###########
        #print("\n\n\t[|> START PM10 ANALYSE <|]\n\n")
        moyPM10 = moyPM10/nbPM10
        #print("\n\tmoyPM10 = ["+str(moyPM10)+"]\n\tBased on "+str(nbPM10)+" sample PM10\n\tResult : [No state defined]")
        #print("\n\n\t[|> END PM10 ANALYSE <|]\n\n")

        ###########
        ### NO² ###
        ###########
        ##print("\n\n\t[|> START NO2 ANALYSE <|]\n\n")
        moyNO2 = moyNO2/nbNO2
        #if moyNO2 < 100 :
            #print("\tmoyNO2 = ["+str(moyNO2)+"]\n\tBased on "+str(nbNO2)+" sample NO2\n\tResult : [Very Good quantity]")
        #if moyNO2 < 199 and moyNO2 > 99 :
            #print("\tmoyNO2 = ["+str(moyNO2)+"]\n\tBased on "+str(nbNO2)+" sample NO2\n\tResult : [Good quantity]")
        #if moyNO2 > 199 :
            #print("\tmoyNO2 = ["+str(moyNO2)+"]\n\tBased on "+str(nbNO2)+" sample NO2\n\tResult : [WARNING : High quantity]")
        #print("\n\n\t[|> END NO2 ANALYSE <|]\n\n")

        ##########
        ### NO ###
        ##########
        #print("\n\n\t[|> START NO ANALYSE <|]\n\n")
        moyNO = moyNO/nbNO
        #if moyNO < 100 :
            #print("\tmoyNO = ["+str(moyNO)+"]\n\tBased on "+str(nbNO)+" sample NO\n\tResult : [Very Good quantity]")
        #if moyNO < 199 and moyNO2 > 99 :
            #print("\tmoyNO = ["+str(moyNO)+"]\n\tBased on "+str(nbNO)+" sample NO\n\tResult : [Good quantity]")
        #if moyNO > 199 :
            #print("\tmoyNO = ["+str(moyNO)+"]\n\tBased on "+str(nbNO)+" sample NO\n\tResult : [WARNING : High quantity]")
        #print("\n\n\t[|> END NO ANALYSE <|]\n\n")

        #print("\n\n\t[|> END JSON DUMP <|]\n\n")
        #print("\n\n\t[|> ____________________________________________________________________________ <|]\n\n")
        return {"resNO2": moyNO2, "resPM10": moyPM10, "resCO2": moyCO2, "resNO": moyNO}


    def graduateAirQuality(self, dict) :
	    return((dict["resNO"]/30)+(dict["resNO2"]/200)+(dict["resPM10"]/80)+(dict["resCO2"]/1000))/4

    def graduateAireQualityByIndice(self, dict) :
        return({"NO" : round((dict["resNO"]/300)*5), "NO2" : round((dict["resNO2"]/200)*5), "PM10" : round((dict["resPM10"]/40)*5), "CO2" : round((dict["resCO2"]/10000)*5)})

    def dictToList(self, dict):
        resList = list()
        for elm in dict.values():
            resList.append(elm)
        return resList