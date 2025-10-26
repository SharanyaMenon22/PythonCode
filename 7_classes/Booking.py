'''
Train booking system.

User POV
- Availability of trains 
- search for the train 
- Date at which the train is available.
- get the availability of tickets ✅
- Book a ticket ( Confirmed, Waiting_list ) ✅
- status = [ Confirmed. Waiting_list]  ✅
- Way to cancel the ticket ✅


Admin POV 

- Add the train to the system. ✅
- Delete the train from the system. ✅
- Feature of the train
   - Name of the train
   - ID of the train
   - Source <> Destination ⛔
   - Capacity
   - Passenger Info
'''

'''
1st booking - 1, Confirmation
2nd Booking - 2, Confirmation
'''

CONFIRMATION = 'Confirmation'
WAITING_LIST = 'Waiting List'
CANCELED = 'Canceled'
MALE = 'M'
FEMALE = 'F'
OTHERS = 'O'

class Person:

    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f"Passenger Details({self.name}, {self.age}, {self.gender})"

class Booking:
    BOOKING_ID = 0

    def __init__(self, person, status):
        self.status = status
        Booking.BOOKING_ID +=1 
        self.id = Booking.BOOKING_ID
        self.person = person        

class Train:
    ID = 0

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        Train.ID += 1
        self.bookings = []

    def availability(self):
        '''
           capacity - (no of tickets in confirmation )

        '''

        total_confirmations = 0
        for booking in self.bookings:
            if booking.status == CONFIRMATION:
                total_confirmations += 1
        
        return self.capacity - total_confirmations

    def book(self, person):
        '''
            if there are enough seats available, book the ticket and status is confirmed else book the ticket, status is waiting list.
        '''
        # if self.availability() > 0:
        #     booking = Booking(CONFIRMATION)
        #     self.bookings.append(booking)
        # else:
        #     booking = Booking(WAITING_LIST)
        #     self.bookings.append(booking)

        status = CONFIRMATION if self.availability() > 0 else WAITING_LIST
        booking = Booking(person, status)
        self.bookings.append(booking)
        print(f"Booked with status: {status}")


    def try_confirm_waiting_list(self):
            availability = self.availability()
            if availability <= 0:
                return            

            for booking in self.bookings:
                if availability <= 0:
                    break

                if booking.status == WAITING_LIST:
                    booking.status = CONFIRMATION
                    availability -= 1

    def cancel(self, id):
        for booking in self.bookings:
            if booking.id == id:
                booking.status = CANCELED
                self.try_confirm_waiting_list()



    def get_bookings(self):
        return self.bookings


class BookingSystem:
    def __init__(self, train):
        self.trains = []
        self.trains.append(train)
    
    def search(self, name):
        for train in self.trains:
            if train.name == name:
                return train
        
        return None
    

    def add_train(self, train):
        self.trains.append(train)


    def book_ticket(self, person, train):
        for train_l in self.trains:
            if train_l.name == train.name:
                train.book(person)

    def cancel_ticket(self, train, id):
         for train_l in self.trains:
            if train_l.name == train.name:
                train.cancel(id)
    
    def show_bookings(self):
        for train in self.trains:
            print(f"Train: {train.name}")

            for booking in train.get_bookings():
                print(f"{booking.id} : {booking.status} , {booking.person}")

    
def main():
    vb = Train("Vande Bharat", 5)

    booking_system = BookingSystem(vb)


    '''
        For now, the passenger details are hard-coded.
        To make it more realistic...
        1. Ask user to input .. ie using input()
        2. If you want to go crazy with automation, then randomly generate name ( predefined set) , age ( 1 - 100), Gender (randomized of Male, Female and Others)
    '''
    for _ in range(1, 15):        
        booking_system.book_ticket( Person("xyz", 25, MALE), vb)
    
    booking_system.show_bookings()

    booking_system.cancel_ticket(vb, 3)

    booking_system.show_bookings()

    booking_system.cancel_ticket(vb, 4)
    booking_system.show_bookings()



if __name__ == '__main__':
    main()

