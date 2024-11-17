from Repulojegy_foglalasi_rendszer.Classes.TicketBooking import TicketBooking
from Repulojegy_foglalasi_rendszer.Classes.Flights import DomesticFlight, InternationalFlight
from Repulojegy_foglalasi_rendszer.Classes.Airline import Airline
from datetime import datetime


def main():
    airline = populate_with_data()

    while True:
        print("\n*** Menu ***")
        print("1. Ticket booking")
        print("2. Cancel booking")
        print("3. Bookings")
        print("4. Exit the program")

        selected = input("Choose an option: ")

        if selected == "1":
            print("\n*** Ticket booking ***")
            print("Available flights:")
            for flight in airline.flights:
                if flight.__class__ == DomesticFlight:
                    print("Flight number: " + flight.flight_number + " Destination: Inland Ticket price: " + str(flight.ticket_price) + " HUF")
                else:
                    print("Flight number: " + flight.flight_number + " Destination: " + flight.destination_country + " Ticket price: " + str(flight.ticket_price) + " HUF")

            flight_number = input("Selected flight number: ")
            date = input("Selected date: ")
            seat_number = input("Selected seat number: ")

            flight_number_valid = validate_flight_number(flight_number, airline.flights)
            date_valid = validate_date(date)

            if not flight_number_valid:
                print("Invalid flight number!")
            elif not date_valid:
                print("Invalid date, date should be formated as YYYY.MM.DD")
            else:
                #A foglalas felvetelekor is ellenorizve van a jarat szam
                booking = airline.booking(flight_number, date, seat_number)
                if booking:
                    print("Your booking was successful!")
                    print("\nHere are the details:")
                    print("Booking id: " +  str(booking.ticket_id))
                    print("Date: " + booking.date)
                    print("Seat number: " + str(booking.seat))
                    print("Ticket price: " + str(booking.ticket_price) + " HUF")
                elif booking == 0:
                    print("Your booking was not successful!")


        elif selected == "2":
            print("\n*** Cancel booking ***")
            print("Your bookings: ")
            for your_bookings in airline.bookings:
                print("Booking id: " + str(your_bookings.ticket_id) + " Flight date: " + str(your_bookings.date) + " Flight destination: " + str(your_bookings.destination_country))
            id_to_cancel = input("Enter id to cancel: ")
            cancel_finished = airline.cancel_booking(id_to_cancel)
            print(str(cancel_finished))


        elif selected == "3":
            print("\n*** List bookings ***")
            print("Your bookings: ")
            for your_bookings in airline.bookings:
                print("Booking id: " + str(your_bookings.ticket_id) + " Flight date: " + str(
                    your_bookings.date) + " Flight destination: " + str(your_bookings.destination_country))


        elif selected == "4":
            print("\n")
            print("Stopping the program...")
            break

        else:
            print("Invalid selection!")


def populate_with_data():
    wizzair = Airline("WizzAir")

    wizz_domestic_1 = DomesticFlight("W111", "Debrecen", 30000)
    wizz_international_1 = InternationalFlight("W115", "London", 100000, "United Kingdom")
    wizz_international_2 = InternationalFlight("W118", "Rome", 70000, "Italy")
    wizzair.add_flight(wizz_domestic_1)
    wizzair.add_flight(wizz_international_1)
    wizzair.add_flight(wizz_international_2)

    booked_ticket_1 = TicketBooking(wizz_domestic_1, 51, "2024.11.20")
    booked_ticket_2 = TicketBooking(wizz_domestic_1, 52, "2024.11.20")
    booked_ticket_3 = TicketBooking(wizz_international_1, 32, "2024.11.22")
    booked_ticket_4 = TicketBooking(wizz_international_1, 34, "2024.11.22")
    booked_ticket_5 = TicketBooking(wizz_international_2, 32, "2024.11.26")
    booked_ticket_6 = TicketBooking(wizz_international_2, 34, "2024.11.26")

    wizzair.add_booking(booked_ticket_1)
    wizzair.add_booking(booked_ticket_2)
    wizzair.add_booking(booked_ticket_3)
    wizzair.add_booking(booked_ticket_4)
    wizzair.add_booking(booked_ticket_5)
    wizzair.add_booking(booked_ticket_6)

    return wizzair


def validate_date(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y.%m.%d").strftime('%Y.%m.%d'):
            raise ValueError
        return True
    except ValueError:
        return False


def validate_flight_number(flight_number, airlines):
    for flight in airlines:
        if flight.flight_number == flight_number:
            return True
    else:
        return False


main()