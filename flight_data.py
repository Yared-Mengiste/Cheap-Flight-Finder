import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, iata_from:str, iata_to:str, date_from:str, date_to:str, max_price:float
                 , api_key:str):
        self.iata_from = iata_from
        self.iata_to = iata_to
        self.date_from = date_from
        self.date_to = date_to
        self.max_price = max_price
        self.api_key = api_key
        self.param_list = []
    def formatted_param(self) -> list:
        '''this method returns the api header and param part respectively
        as a list'''
        FLIGHT_HEADER = {
            'apikey': self.api_key,
            "Content-Type": "application/json",
        }
        self.param_list.append(FLIGHT_HEADER)
        FLIGHT_PARAMETER = {
            'fly_from': self.iata_from,
            'fly_to': self.iata_to,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'price_to': self.max_price,
        }
        self.param_list.append(FLIGHT_PARAMETER)
        return self.param_list



