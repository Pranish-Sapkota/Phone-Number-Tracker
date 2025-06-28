import phonenumbers
from phonenumbers import geocoder
from number import number
import folium

Key = "ae14aef439f64d64991c316cea234fc1"

#This shows the country name of the number
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)

#This shows the company name of the phone number
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

#This section use OpenCageGeocode to convert the location into geogrophic coordinates
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

#This show the map in html file
map_location = folium.Map(location = [lat, lng],zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")