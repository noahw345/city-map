import folium
import pandas

#read csv file containing data about major world cities
data = pandas.read_csv("worldcities.csv")

#create lists containing data
lat = list(data["lat"])
lon = list(data["lng"])
names = list(data["city"])
population = list(data["population"]) 

#create map and feature group
map = folium.Map(tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")


def get_rad(pop):
    return pop / 1000000 
    #since the populations passed to this method will range between 10m t0 40m, 
    #they can be divided by 1m and the radius will be proportionate to each city's population

#loops through data and adds a marker containing the name and population, and sizes the marker relative to the population
for lt, ln, name, pop in zip(lat, lon, names, population):
    if pop > 10000000:
            fg.add_child(folium.CircleMarker(location=[lt,ln], radius=get_rad(pop),popup= "%s \n Population %s" % (name, "{:,}".format(pop)),fill_color="red",color="grey",fill_opacity="0.7"))
            map.add_child(fg)

#saves new map to html file
map.save("Map1.html")