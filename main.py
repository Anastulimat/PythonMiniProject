import file_manager
import display_data
import display_map

def main():
    fm = file_manager.FileManager()
    dd = display_data.DisplayData()
    dm = display_map.DisplayMap()


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
    Traitement histogramme
    """
    stations, trafic, quartiers = dd.get_data_about_paris_district(data_to_use)
    quartiers_dic = dd.get_quartiers_dictionnary(quartiers)
    traifc_dic = dd.get_trafic_dictionnary(data_to_use)
    trafic_keys, trafic_values = dd.get_trafic_keys_and_values_form_dictionnary(traifc_dic)

    """
    Génération de la carte et affichage histogramme
    """
    dm.create_map(trafic_values)
    dd.print_data(trafic_keys, trafic_values)



if __name__ == '__main__':
    main()
