
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, header: dict, parameter:dict):
        self.header = header
        self.parameter = parameter
        self.api = 'https://api.tequila.kiwi.com/v2/search'
        self.result = self.return_query_result()

    def return_query_result(self) -> dict:
        response = requests.get(self.api, params=self.parameter, headers=self.header)
        print(response.text)
        return response.json()