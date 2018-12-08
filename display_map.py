import folium, branca, geojson
import api

class DisplayMap:
    center_coords = (48.864716,2.349014)
    SIZE = []
    LATS = []
    LONGS = []


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
    def create_map(self, trafic_values, air_quality):
        map = folium.Map(location = self.center_coords, tiles = 'Stamen Terrain', zoom_start=13)
        cmAir = branca.colormap.LinearColormap(['green', 'blue', 'yellow', 'orange', 'red', 'black'], vmin = 0, vmax = 6)
        cm = branca.colormap.LinearColormap(['blue', 'yellow', 'red'], vmin = min(trafic_values), vmax = max(trafic_values))
        map.add_child(cm, name="Traffic Legend") # add this colormap on the display
        map.add_child(cmAir)
        
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

        for current_air_quality in air_quality :
            folium.CircleMarker(
                location = current_air_quality["coords"],
                radius = current_air_quality["indice"]*40,
                color = "green",
                fill = True,
                fill_color = cmAir(current_air_quality["indice"])
            ).add_to(map)

        map.add_child(f) # add the group to the map
        map.save(outfile='map.html')


    

