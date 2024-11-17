from Repulojegy_foglalasi_rendszer.Classes.Flights import InternationalFlight


class TicketBooking:
    ticket_id = 1

    def __init__(self, flight, seat, date):
        self.ticket_id = TicketBooking.ticket_id
        self.flight = flight
        self.seat = seat
        self.date = date
        self.ticket_price = flight.ticket_price
        if flight.__class__ == InternationalFlight:
            self.destination_country = flight.destination_country
        else:
            self.destination_country = "Inland"
        TicketBooking.ticket_id += 1