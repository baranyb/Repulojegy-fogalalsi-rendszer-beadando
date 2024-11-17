from Repulojegy_foglalasi_rendszer.Classes.TicketBooking import TicketBooking


class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []
        self.bookings = []

    def add_flight(self, flight):
        self.flights.append(flight)


    def cancel_booking(self, id_to_cancel):
        for booking in self.bookings:
            #Validacio
            if  int(id_to_cancel) == booking.ticket_id:
                self.bookings.remove(booking)
                return "The booking has been cancelled"
        return "No booking found with the given ID!"


    def add_booking(self, booked_ticket):
        self.bookings.append(booked_ticket)


    def booking(self, flight_number, date, seat):
        for flight in self.flights:
            #Validacio
            if flight.flight_number == flight_number:
                booked_ticket = TicketBooking(flight, seat, date)
                self.add_booking(booked_ticket)
                return booked_ticket
        return 0