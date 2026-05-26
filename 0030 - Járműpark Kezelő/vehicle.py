class Vehicle:
    def __init__(self, brand, rent_price, fuel):
        self.brand = brand
        self.rent_price = rent_price
        self.fuel = fuel

    @property
    def rent_price(self):
        return self._rent_price

    @rent_price.setter
    def rent_price(self, value):
        if value <0:
            print("A bérleti díj nem lehet negatív!")
            self._rent_price = 0
        else:
            self._rent_price = value
    @property
    def brand(self):
        return self._brand.upper()
    @brand.setter
    def brand(self, value):
        if len(value)<2:
            print("Érvénytelen márkanév!")
            self._brand = "ISMERETLEN"
        else:
            self._brand=value
    @property
    def fuel(self):
        return self._fuel
    @fuel.setter
    def fuel(self,value):
        if len(value) <1:
            self._fuel="ismeretlen"
        else:
            self._fuel=value


    def display_info(self):
        print(f"Ez egy {self.brand}, a bérleti díja {self.rent_price} Ft/nap.")
