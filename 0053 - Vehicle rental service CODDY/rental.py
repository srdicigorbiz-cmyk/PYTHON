class Rental:
    def __init__(self, rental_id, vehicle, customer_name, days):
        # Initialize properties
        self.rental_id = rental_id
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.days = days
        self.is_active = True
    
    def calculate_cost(self):
        # TODO: Calculate and return the total cost by multiplying
        # TODO: the vehicle's daily_rate by the number of days
        return self.vehicle.daily_rate * self.days
    
    def end_rental(self):
        # TODO: Check if the rental is active (self.is_active is True)
        # TODO: If active, set self.is_active to False
        # TODO: Call the vehicle's end_rental method
        # TODO: Return True to indicate successful completion
        # TODO: If not active, return False
        if self.is_active is True:
            self.is_active= False
            self.vehicle.end_rental()
            return True
        else:
            return False
    
    def __str__(self):
        # TODO: Create a status string based on self.is_active ("Active" or "Completed")
        # TODO: Return a formatted string in the format:
        # TODO: "Rental {rental_id}: {vehicle.make} {vehicle.model} for {customer_name} - {status}"
        if self.is_active is True:
            status = "Active"
        else:
            status = "Completed"
        return f"Rental {self.rental_id}: {self.vehicle.make} {self.vehicle.model} for {self.customer_name} - {status}"