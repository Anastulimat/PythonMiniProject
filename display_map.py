import folium, branca, geojson

class DisplayMap:
    center_coords = (48.864716,2.349014)
    SIZE = []

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


    """
    retourne liste de rayon des circles

    Args:
        trafic_values: liste des valeurs sur le trafic

    Returns:
        2liste de rayon des circles
    """
    def get_size_for_cirecle(self, trafic_values):
        for elem in trafic_values:
            if(elem >= 100000000):
                self.SIZE.append((elem/1000000)/2)
            else:
                self.SIZE.append((elem/1000000)/2)


    """
    génère un fichier html contenant les information affichées sur une carte

    Args:
        trafic_values: liste des valeurs sur le trafic

    Returns:
        génère un fichier html contenant les information affichées sur une carte
    """
    def create_map(self, trafic_values):
        map = folium.Map(location = self.center_coords, tiles = 'OpenStreetMap')
        cm = branca.colormap.LinearColormap(['blue', 'yellow', 'red'], vmin = min(trafic_values), vmax = max(trafic_values))
        map.add_child(cm) # add this colormap on the display

        
        self.get_size_for_cirecle(trafic_values)
        f = folium.map.FeatureGroup() # create a group
        for lat, lng, size, color in zip(self.LATS, self.LONGS, self.SIZE, trafic_values):
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


    

