from vehicle import Vehicle
class Car(Vehicle):
    def __init__ (self, brand, rent_price, seats, fuel):
        super().__init__(brand, rent_price, fuel)
        self.seats = seats
    
    @property
    def seats(self):
        return self._seats
    @seats.setter
    def seats(self, value):
        if value < 1:
            print("Seats number must be greater then 0")
            self._seats=5
        elif value > 9:
            print("Seat numbers cant be more then 9")
            self._seats=5
        else:
            self._seats = value

    def display_info(self):
        print(f"Ez egy {self.brand} személyautó, {self.seats} férőhellyel. Napi díj: {self.rent_price} Ft.")