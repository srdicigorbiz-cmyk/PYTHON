class Coffee:
    def cost(self):
        return 5
    
    def description(self):
        return "Simple coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2
    
    def description(self):
        return self.coffee.description() + " + Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 1
    
    def description(self):
        return self.coffee.description() + " + Sugar"

# Start with basic coffee
my_coffee = Coffee()
print(f"{my_coffee.description()}: ${my_coffee.cost()}")


# Add milk
my_coffee = MilkDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")


# Add sugar
my_coffee = SugarDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")
