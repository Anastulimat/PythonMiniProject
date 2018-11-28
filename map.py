import folium, branca, geojson
import histogramme as his

STATIONS = ['ABBEVILLE', 'AJACCIO', 'ALENCON', 'BALE-MULHOUSE',
            'BELLE ILE-LE TALUT', 'BORDEAUX-MERIGNAC', 'BOURGES',
            'BREST-GUIPAVAS', 'CAEN-CARPIQUET', 'CAP CEPET',
            'CLERMONT-FD', 'DIJON-LONGVIC', 'EMBRUN', 'GOURDON',
            'LE PUY-LOUDES', 'LILLE-LESQUIN', 'LIMOGES-BELLEGARDE',
            'LYON-ST EXUPERY', 'MARIGNANE', 'MILLAU', 'MONT-DE-MARSAN',
            'MONTELIMAR', 'MONTPELLIER', 'NANCY-OCHEY',
            'NANTES-BOUGUENAIS', 'NICE', 'ORLY', 'PERPIGNAN',
            "PLOUMANAC'H", 'POITIERS-BIARD', 'PTE DE CHASSIRON',
            'PTE DE LA HAGUE', 'REIMS-PRUNAY', 'RENNES-ST JACQUES',
            'ROUEN-BOOS', 'ST GIRONS', 'STRASBOURG-ENTZHEIM',
            'TARBES-OSSUN', 'TOULOUSE-BLAGNAC', 'TOURS', 'TROYES-BARBEREY']

LATS = [48.86256270183605, 48.86827922252252, 48.86287238001689, 48.854341426272896,
        48.84444315053267, 48.84913035858519, 48.85617442877936, 48.87272083743446, 
        48.87716351732886, 48.876130036539124, 48.859059221342505, 48.83497438148051,
        48.828388031744694, 48.829244500489835, 48.84008537593817, 48.860392105415706, 
        48.88732652202582, 48.892569268005786, 48.887075996572506, 48.86346057889556]

LONGS = [2.3364433620533847, 2.3428025468913636, 2.3600009858976927, 2.357629620324993,
         2.350714609575257, 2.332897999053313, 2.312187691482009, 2.3125540224020638,
         2.3374575434825466, 2.36072848784745, 2.380058308197898, 2.421324900784681,
         2.3622724404209055, 2.3265420441989453, 2.2928258224249967, 2.2619707883645397, 
         2.3067769905744084, 2.34816051956204, 2.3848209601525143, 2.4011881292846864]

TEMPS = [7.6, 13.5, 7.6, 6.8, 10.5, 11.5, 8.5, 9.7, 8.6, 11.8, 9.1,
         7.2, 5.7, 9.2, 6.0, 7.2, 7.6, 8.4, 12.0, 6.1, 11.6, 9.6, 11.7,
         6.5, 10.0, 11.7, 8.1, 12.6, 9.9, 9.1, 10.8, 9.5, 7.4, 9.0,
         7.1, 10.3, 6.7, 10.8, 10.6, 8.4, 8.1]

SIZE = list()

for elem in his.trafic_values:
        if(elem >= 100000000):
                SIZE.append((elem/1000000)/2)
        else:
                SIZE.append((elem/1000000)/2)

coords = (48.864716,2.349014)
map = folium.Map(location=coords, tiles='OpenStreetMap')

cm = branca.colormap.LinearColormap(['blue', 'yellow', 'red'], vmin=min(his.trafic_values), vmax=max(his.trafic_values))
map.add_child(cm) # add this colormap on the display

f = folium.map.FeatureGroup() # create a group


for lat, lng, size, color in zip(LATS, LONGS, SIZE, his.trafic_values):
    print(lat, lng, size, color)
    f.add_child( # add iteratively a CircleMarker to this group
        folium.CircleMarker(
            location=[lat, lng],
            radius=size,
            color=None,
            fill=True,
            fill_color=cm(color),
            fill_opacity=0.6)
    )


map.add_child(f) # add the group to the map

map.save(outfile='map.html')
