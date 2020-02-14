# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

# In `cityreader`, use Python's built-in "csv" module to read and import into a City instance. 
# Return a list with all the City instances.
# Google "python 3 csv" for references and use your Google-fu for examples.#
# Store the instances in the "cities" list, below.
# Note that the first line of the CSVshould not be loaded into a City object.

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __repr__(self):
    return f'<{self.name}, {self.lat}, {self.lon}>\n'

  def __str__(self):
    return f'{self.name}, {self.lat}, {self.lon}\n'

import csv


def cityreader(cities=[]):  
  all_city_data = []
  path = 'src\cityreader\cities.csv'

  with open(path) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
      r = row
      all_city_data.append(r)
    for row in all_city_data:
      lat_lon = City(row[0], row[3], row[4])
      cities.append(lat_lon)
    
      cities.remove(cities[0])
  return cities

  print(cities)        

# cityreader(cities)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within
