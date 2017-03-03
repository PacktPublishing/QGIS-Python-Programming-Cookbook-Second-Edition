# Geocoding Addresses

# Requires the QGIS Python Geocoding Plugin

from GeoCoding import GeoCoding
init = GeoCoding.GeoCoding(iface)
from geopy.geocoders import Nominatim
geocoder = Nominatim()
location = geocoder.geocode("The Ugly Pirate, Bay Saint Louis, MS 39520")
print location

