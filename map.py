import folium
from geopy.geocoders import ArcGIS 
address = fromwebsite

arc = ArcGIS()
x = arc.geocode(address)
map = folium.Map(location = [x.latitude,x.longitude], zoom_start= 100, tiles = "Stamen Terrain")

map.add_child(folium.Marker(location = [x.latitude, x.longitude]))


map.save('map2.html')
