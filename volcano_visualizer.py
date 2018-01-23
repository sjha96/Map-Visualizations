import folium
import pandas
import json
map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles = "Mapbox Bright")
fg = folium.FeatureGroup(name = "Volcano Visualizer")
fg1 = folium.FeatureGroup(name = "Population Visualizer")
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])
location = list(data["LOCATION"])

def color_producer(elevation):
    if elevation < 1000:
        return  'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, nm, loc, elev in zip(lat,lon, name, location, elevation):
    fg.add_child(folium.CircleMarker(location = [lt,ln], radius = 6,
    popup=folium.Popup(str(nm + ", " + loc), parse_html=True),
    fill_color= color_producer(elev), color = 'grey', fill = 0.7, fill_opacity=1))

fg1.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = "utf-8-sig").read(),
style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("Map1.html")
