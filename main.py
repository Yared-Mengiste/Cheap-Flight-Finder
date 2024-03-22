import datetime
import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from email_connercton import SendEmail
import os

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
DATE_FROM = datetime.date.today().strftime('%d/%m/%Y')
DATE_TO = (datetime.date.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

# todo using data manager get spreedsheet info from sheety.co put it in some dic and select the values needed
SHEETY_BEARER = 'itsmeyared'
IATA_FROM = 'LON'
KIWI_API_KEY = 'AJrag0ykr2HiMSVG1O3tGCbYDkGeZUDo'
URL = 'https://api.sheety.co/6df0a8cb3491ee21315b48dff783f802/flightDeals/prices'
SHEETY_USER_URL = 'https://api.sheety.co/6df0a8cb3491ee21315b48dff783f802/flightDeals/users'
sheety_info = DataManager(SHEETY_BEARER, URL)
SENDER = 'stoicyared@gmail.com'
PASSWORD = os.environ.get('EMAIL_PASSWORD')

country_info = []
for country in sheety_info.result['prices']:
    temp_dict = {'iataCode': country['iataCode'], 'lowestPrice': country['lowestPrice']}
    country_info.append(temp_dict)

# todo change the sheety result to the correct parameter to kiwi api
header_parameter_list = []
for city in country_info:
    temp_format = FlightData(IATA_FROM, city['iataCode'], DATE_FROM, DATE_TO, city['lowestPrice'], KIWI_API_KEY)
    header_parameter_list.append(temp_format.formatted_param())

# todo get the results from kiwi for the given header_parameter_lists
# if the result['_results'] = 0 continue
# else using for loop get result['data'] get cityFrom, cityTo, utc_departure, utc_arrival, availability['seats'],price
ticket_opportunity = []
for flights in header_parameter_list:
    temp_flight_search = FlightSearch(flights[0], flights[1])
    result = temp_flight_search.result
    if result['_results'] == 0:
        print(f'no flight for {flights[1]}')
        continue
    else:
        for flight in result['data']:
            if flight['availability']['seats'] is None:
                continue
            temp_dic = {
                'City From ': flight['cityFrom'],
                'City To': flight['cityTo'],
                'Departure Time UTC': flight['utc_departure'],
                'Arrival Time UTC': flight['utc_arrival'],
                'Available Seats': flight['availability']['seats'],
                'Price': flight['price']
            }
            ticket_opportunity.append(temp_dic)
if len(ticket_opportunity) == 0:
    print("no flight")
else:
    message = ''
    counter = 0
    for flight_opportunity in ticket_opportunity:
        for key, value in flight_opportunity.items():
            message += f'{key:<18} : {value}\n'
        counter += 1
        if counter > 2:
            break
        message += '\n'

    user_file = DataManager(bearer=SHEETY_BEARER, url=SHEETY_USER_URL)
    user_info = user_file.result['users']
    pprint.pprint(user_info)
    for user in user_info:
        fullName = f"{user['fName']} {user['lName']}"
        email = user['email']
        mod_message = f'Dear {fullName} there is\n\n{message} \n Enjoy the flight you want!!'

        send_email = SendEmail(SENDER, PASSWORD)
        send_email.send_email(mod_message, email)
        print(fullName, ' ', email)

