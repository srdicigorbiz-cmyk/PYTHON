class WeatherStation:
    def __init__(self):
        self.subscribers = []
        self.current_temperature = 0
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    def temperature(self, temp):
        self.current_temperature = temp
        self.notify(temp)
    def notify(self, message):
        
        for sub in self.subscribers:
            sub.update(message)

class TemperatureDisplay:
    def update(self, message):
        print(f"The new temperature is: {message}")

station = WeatherStation()
display = TemperatureDisplay()

station.subscribe(display)
station.temperature(25)
station.temperature(30)