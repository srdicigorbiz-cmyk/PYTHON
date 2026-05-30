balance = 10000 
counter = 0

class BalanceException(Exception):
    pass
class NoMoreAttempt(Exception):
    pass

def transaction():
    global balance
    global counter
    while True:
        try:
            if counter > 2:
                raise NoMoreAttempt("No more attempts allowed!")
            amt = float(input())
            
            #check remaining amount after transaction
            temp = balance - amt
            if temp < 100:
                counter += 1
                raise BalanceException("Insufficient balance")
        except BalanceException as obj:
            print(obj)  # Kiírja: "Insufficient balance", és a ciklus megy tovább a következő körre!

        except NoMoreAttempt as e:
            print(e)    # Kiírja: "No more attempts allowed!"
            return      # Leállítja a teljes függvényt és a ciklust (fagyasztás).
        else:
            balance = balance - amt
            print(f"Transaction is success, Remaining balance is: {balance}")
            return
    
transaction()