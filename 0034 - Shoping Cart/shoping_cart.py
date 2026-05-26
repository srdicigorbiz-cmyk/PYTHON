class Item:
    def __init__(self,name, price):
        self.name = name
        self.price = price
    def __str__(self): Ft"

class ShoppingCart:
    def __init__(self):
        self.items=[]
    def __add__(self, new_item):
        # TODO: Ellenőrizd, hogy az new_item tényleg egy Item objektum-e!
        # TODO: Add hozzá a self.items listához.
        # TODO: Add vissza a self-et (hogy láncolható legyen: kosar + t1 + t2).
        if isinstance (new_item, Item):
            self.items.append(new_item)
        return self
        
    def __len__(self):
        return len(self.items)
    def __str__(self):
        # TODO: Számold ki az árak összegét a listában lévő Itemekből.
        # TODO: Add vissza a kért szöveget.
        sum=0
        darab = len(self.items)
        for item in self.items:
            sum += item.price
        return f"A kosár tartalma {darab} tétel, összesen {sum} Ft"