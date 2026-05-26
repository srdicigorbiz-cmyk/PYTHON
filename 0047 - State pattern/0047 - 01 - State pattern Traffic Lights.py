class RedState:
    def next_state(self, light):
        print("Red -> Green")
        light.state = GreenState()
    
    def current_color(self):
        return "Red"


class GreenState:
    def next_state(self, light):
        print("Green -> Yellow")
        light.state = YellowState()
    
    def current_color(self):
        return "Green"


class YellowState:
    def next_state(self, light):
        print("Yellow -> Red")
        light.state = RedState()
    
    def current_color(self):
        return "Yellow"
class TrafficLight:
    def __init__(self):
        self.state = RedState()  # Start with red
    
    def change(self):
        self.state.next_state(self)
    
    def get_color(self):
        return self.state.current_color()


light = TrafficLight()
print(f"Current: {light.get_color()}")


light.change()  # Red -> Green
print(f"Current: {light.get_color()}")


light.change()  # Green -> Yellow
print(f"Current: {light.get_color()}")


light.change()  # Yellow -> Red
print(f"Current: {light.get_color()}")
