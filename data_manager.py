import pprint
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, bearer: str, url: str):
        self.url = url
        self.header = {
            "Authorization": f'Bearer {bearer}',
            "Content-Type": 'application/json'
        }
        self.result = self.return_sheety_result()

    def return_sheety_result(self) -> dict:
        response = requests.get(self.url, headers=self.header)
        print(response.text)
        self.result = response.json()
        return self.result

    def post_to_query(self, parameter: dict):
        response = requests.post(self.url, json=parameter, headers=self.header)
        print(response.text)


# email = DataManager('itsmeyared', 'https://api.sheety.co/6df0a8cb3491ee21315b48dff783f802/flightDeals/users')
# pprint.pprint(email.result)
# parameter = {
#     'user': {
#         'fName': 'Leul',
#         'lName': 'Mengiste',
#         'email': 'stoicyared@gmail.com'
#     }
# }
# email.post_to_query(parameter)

