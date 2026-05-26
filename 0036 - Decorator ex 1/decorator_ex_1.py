import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Elindítjuk az órát
        
        # Lefuttatjuk az eredeti függvényt
        result = func(*args, **kwargs)
        
        end_time = time.time()    # Megállítjuk az órát
        print(f"--- A(z) '{func.__name__}' függvény {end_time - start_time:.6f} másodpercig futott ---")
        
        return result
    return wrapper

@timer_decorator
def nehez_feladat():
    print("Gondolkodom...")
    time.sleep(1.5) # Szimulálunk egy kis várakozást
    print("Kész!")

nehez_feladat()

#########################################################
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#########################################################
#######CLASS DECORATOR###################################
#########################################################

def add_counter(cls):
    cls.call_counts = {"add": 0} #SZAMLALÓ START ÁLLAPOT MEGHATÁROZÁS
    
    original_add = cls.add #ELMENTJÜK AZ EREDETI FUGGVENYT
    
    def wrapped_add(self, a, b): # EZ A WRAPPER 
        cls.call_counts["add"] += 1 # ELVÉGZI A FELADATOT A FÜGGVÉNY ELŐTT
        return original_add(self, a, b)  # MEGHÍVJA AZ EREDETI FÜGGVÉNYT AMIT CSOMAGOL
    
    cls.add = wrapped_add #AZ EREDETI FÜGGVÉNY ÖSSZEKÖTI ÖNMAGÁT A WRAPPEREL ÉS MEGHÍVÁSNÁL INDÍTJA
    return cls #VISSZAADJA A CLASS-T

@add_counter
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
calc.add(5, 3)
calc.add(2, 7)
print(calc.call_counts)