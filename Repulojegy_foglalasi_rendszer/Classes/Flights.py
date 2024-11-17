from abc import ABC, abstractmethod


class Flight(ABC):
    def __init__(self, flight_number, destination, ticket_price):
        self.flight_number = flight_number
        self.destination = destination
        self.ticket_price = ticket_price


class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, ticket_price):
        super().__init__(flight_number, destination, ticket_price)


class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, ticket_price, destination_country):
        super().__init__(flight_number, destination, ticket_price)
        self.destination_country = destination_country

