import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("G_MAPS_API_KEY")
TIME_PRICE = 100  # price per hour of riding per person
FUEL_CONSUMPTION = 7  # per 100km
POINT_BETWEEN_TWO_VIOLINS_COORDS = '52.151308, 21.098135'

class NotFoundError(Exception):
  pass

def get_distance_time(place, postal_code):
  client = googlemaps.Client(key=API_KEY)

  dest = f'{postal_code}, {place}'
  request = {
      'origins': [POINT_BETWEEN_TWO_VIOLINS_COORDS],
      'destinations': [dest],
      'transit_mode': 'driving',
      'units': 'metric',
      'avoid': 'tolls',
    }

  ans = client.distance_matrix(**request)
  element = ans['rows'][0]['elements'][0]
  if element['status'] == 'NOT_FOUND':
    print('NotFoundError', dest)
    raise NotFoundError
  else:
    dist = element['distance']['value']
    time = element['duration']['value']
    return dist, time

def calculate_price(place, postal_code):
  try:
    dist, time = get_distance_time(place, postal_code)
  except NotFoundError:
    return 'Not found'

  dist_km = dist / 1000
  time_hours = time / 3600
  total_time_price = 2 * time_hours * TIME_PRICE
  petrol_price_per_liter = get_petrol_price_per_liter()
  total_petrol_price = 2 * dist_km / 100 * FUEL_CONSUMPTION * petrol_price_per_liter
  # return f"time price {total_time_price} fuel price {total_petrol_price}"
  total_price = total_petrol_price + total_time_price
  return f"{total_price:.2f}".replace('.', ',')

def get_petrol_price_per_liter():
  # TODO!!!
  return 6.24

if __name__ == '__main__':
  print(calculate_price('Zakopane', '34-500'))

# RESPONSE FORMAT
# {
#     'destination_addresses': ['Kraków, Poland'], 
#     'origin_addresses': ['Warsaw, Poland'], 
#     'rows': [{
#         'elements': [{
#             'distance': {'text': '295 km', 'value': 294813}, 
#             'duration': {'text': '3 hours 28 mins', 'value': 12494}, 
#             'status': 'OK'
#           }] 
#       }
#     ], 
#     'status': 'OK'
# }

