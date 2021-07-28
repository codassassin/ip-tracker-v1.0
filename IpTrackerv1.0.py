from geolite2 import geolite2
import requests


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.GREEN + '<<< IP-TRACKER v1.0>>>')
    print(bColors.RED + r'''
  _
 | |
 | |___
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ |
           |___/
                                        _                                                         _
                                       | |                                                       (_)
                  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\   /    \   /  _  |  / _ | | / _____| / _____|  / _ | | / _____| / _____| | | | |   | \
                | |____  |  ()  | |  (_| | | (_|| | \______\ \______\ | (_|| | \______\ \______\ | | | |   | |
                 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
     ''')


def ipLocation(ipTrack):
    docReader = geolite2.reader()
    trackLocation = docReader.get(ipTrack)

    # Assigning specific values from GeoLiteCity.dat
    city = (trackLocation['city']['names']['en'])
    continent = (trackLocation['continent']['names']['en'])
    country = (trackLocation['country']['names']['en'])
    location = (trackLocation['location'])
    locationAccuracy = location['accuracy_radius']
    locationLatitude = location['latitude']
    locationLongitude = location['longitude']
    locationTimeZone = location['time_zone']
    postal = (trackLocation['postal'])
    postalCode = postal['code']
    registeredCountry = (trackLocation['registered_country']['names']['en'])
    subdivisions = (trackLocation['subdivisions'][0]['names']['en'])

    r = str(bColors.RED)
    g = str(bColors.GREEN)
    b = str(bColors.BLUE)
    y = str(bColors.YELLOW)

    print(r + '* ' + b + 'public_ip: ' + g + ip + r + '\n* ' + b + 'city: ' + g + city + r + '\n* ' + b + 'continent: ' + g +
          continent + r + '\n* ' + b + 'country: ' + g + country + r + '\n* ' + b + 'location: ' + r + '\n\t↪ ' + y +
          'accuracy_radius: ' + g + str(locationAccuracy) + r + '\n\t↪ ' + y + 'latitude: ' + g + str(locationLatitude)
          + r + '\n\t↪ ' + y + 'longitude: ' + g + str(locationLongitude) + r + '\n\t↪ ' + y + 'time_zone: ' + g +
          locationTimeZone + r + '\n\t↪ ' + y + 'map: ' + g +
          f'https://www.google.co.in/maps/@{locationLatitude},{locationLongitude},15z?hl=en' + r + '\n* ' + b +
          'postal_code: ' + g + str(postalCode) + r + '\n* ' + b + 'registered_country: ' + g + registeredCountry + r +
          '\n* ' + b + 'subdivisions: ' + g + subdivisions)


ip = requests.get('https://api.ipify.org').text

banner()
ipLocation(ip)

