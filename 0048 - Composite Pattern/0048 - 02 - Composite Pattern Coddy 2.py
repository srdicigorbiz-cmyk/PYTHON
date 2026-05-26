class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    
    def show(self):
        return f"{self.name}: ${self.price}"


class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def get_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
    
    def show(self):
        result = f"{self.name} Menu:"
        for item in self.items:
            result += f"\n  {item.show()}"
        return result


combo = Menu("Combo")
combo.add(MenuItem("Burger", 8))
combo.add(MenuItem("Fries", 3))
combo.add(MenuItem("Drink", 2))


print(f"Combo price: ${combo.get_price()}")
print(combo.show())
