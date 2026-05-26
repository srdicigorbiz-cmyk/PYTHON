from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, rent_price, max_load, fuel):
        super().__init__(brand,rent_price, fuel)
        self.max_load = max_load
        
    @property
    def max_load(self):
        return self._max_load
    @max_load.setter
    def max_load(self, value):
        if value < 0:
            print("Rakomány nem lehet negatív!")
            self._max_load = 0
        elif value > 20:
            print("Rakomány nem lehet több 20-nál!")
            self._max_load = 20
        else:
            self._max_load = value
    
    def display_info(self):
        print(f"FIGYELEM: {self.brand} tehergépjármű érkezik! Teherbírás: {self.max_load} tonna. Napi díj: {self.rent_price} Ft.")