import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

num = "+243979064470"

# touver le pays du numero
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")
# affichage de la localisation(pays)
print(localisation)

# trouver l'operateur du numero
operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))

# trouver la latitude et la longitude
clef = "61fe5867b0db4fde8f3bed0bc0e35137"
coord = OpenCageGeocode(clef)
requette = str(localisation)
reponse = coord.geocode(requette)
print(reponse)
# extraction de lat et de lng
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]

# on affiche seulement la lat et la lng
print(lat, lng)

# creation du mapview selon le coord de geo
monMap = folium.Map(location=[lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("map.html")
