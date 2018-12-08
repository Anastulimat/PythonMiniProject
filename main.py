import file_manager
import display_data
import display_map
import api
import webbrowser,os

def main():
    fm = file_manager.FileManager()
    dd = display_data.DisplayData()
    dm = display_map.DisplayMap()
    ap = api.Api()


    """
    Récupération et traitement de données
    """
    list_file_content = fm.get_list_file_content('files/trafic-annuel-entrant-par-station-du-reseau-ferre-2016.csv')
    first_line = fm.get_first_line(list_file_content)
    first_line_componants = fm.get_first_line_componants(first_line)
    data_headers_to_use = fm.get_data_headers_to_use(first_line_componants)
    file_content = fm.get_file_content(list_file_content)
    informations = fm.get_informations(file_content)
    data_to_use = fm.get_data_to_use(informations)

    list_arrondissements_content = fm.get_list_file_content('files/arrondissements.csv')
    arrondissements_file_content = fm.get_file_content(list_arrondissements_content)
    arrondissements_infos = fm.get_informations(arrondissements_file_content)
    dm.LATS, dm.LONGS = fm.get_lats_lngs(arrondissements_infos)

    """
    Récupération de données avec API
    """
    apiList = ["https://data.iledefrance.fr/api/records/1.0/search/?dataset=qualite-de-lair-mesuree-dans-la-station-chatelet&rows=20&start=8000&timezone=UTC","https://data.iledefrance.fr/api/records/1.0/search/?dataset=qualite-de-lair-mesuree-dans-la-station-franklin-d-roosevelt&rows=20&start=8000&timezone=UTC","https://data.iledefrance.fr/api/records/1.0/search/?dataset=qualite-de-lair-mesuree-dans-la-station-auber&rows=20"]
    resOpenDataChatelet = ap.OpenDataIDF(apiList[0])
    liste1 = ap.graduateAirQuality(resOpenDataChatelet)
    list1Byindex = ap.graduateAireQualityByIndice(resOpenDataChatelet)
    dict1 = ap.airQualityDataMap(apiList[0], liste1)
    l1 = ap.dictToList(list1Byindex)


    resOpenDataRoosevelt = ap.OpenDataIDF(apiList[1])
    liste2 = ap.graduateAirQuality(resOpenDataRoosevelt)
    list2Byindex = ap.graduateAireQualityByIndice(resOpenDataRoosevelt)
    dict2 = ap.airQualityDataMap(apiList[1], liste2)
    l2 = ap.dictToList(list2Byindex)

    resOpenDataAuber = ap.OpenDataIDF(apiList[2])
    liste3 = ap.graduateAirQuality(resOpenDataAuber)
    list3Byindex = ap.graduateAireQualityByIndice(resOpenDataAuber)
    dict3 = ap.airQualityDataMap(apiList[2], liste3)
    l3 = ap.dictToList(list3Byindex)

    air_Quality_Paris = [dict1, dict2, dict3]
    
    """
    Traitement histogramme
    """
    stations, trafic, quartiers = dd.get_data_about_paris_district(data_to_use)
    quartiers_dic = dd.get_quartiers_dictionnary(quartiers)
    traifc_dic = dd.get_trafic_dictionnary(data_to_use)
    trafic_keys, trafic_values = dd.get_trafic_keys_and_values_form_dictionnary(traifc_dic)

    """
    Génération de la carte et affichage histogramme
    """
    dm.create_map(trafic_values, air_Quality_Paris)
    dd.display_data_on_histogramme(trafic_keys, trafic_values, l1, l2, l3)

    webbrowser.open('file://'+str(os.path.realpath("map.html")))



if __name__ == '__main__':
    main()
