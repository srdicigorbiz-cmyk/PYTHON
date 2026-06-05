class CartIterator:
    def __init__(self, cart_data):
        self.cart_data = cart_data
        self.cart_tuples = list(self.cart_data.items())
        self.idx = 0
    def __iter__(self):
        self.idx = 0
        return self
    def __next__(self):
        if self.idx < len(self.cart_tuples):
            result = self.cart_tuples[self.idx]
            self.idx += 1
            return result
        else:
            raise StopIteration




try:
    cart_data = {"tej": 450, "kenyér": 320, "sajt": 1200}
    cart = CartIterator(cart_data)
    
    # Első kör bejárása
    for item, price in cart:
        print(f"Termék: {item}, Ár: {price}")
        
    # Teszteljük, hogy újraindítható-e!
    print("--- Második kör ---")
    for item, price in cart:
        print(f"Termék: {item}, Ár: {price}")
        
except StopIteration:
    print("Hiba: A StopIteration-nek csendben kell lefutnia a for ciklusban!")
        