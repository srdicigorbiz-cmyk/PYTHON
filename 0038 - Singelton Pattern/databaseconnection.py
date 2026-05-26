class DatabaseConnection:
    # TODO: Create a private class variable _instance initialized to None
    # This will store the singleton instance
    _instance = None
    
    def __new__(cls):
        # TODO: Implement the __new__ method to ensure only one instance is created
        # TODO: Check if cls._instance is None
        # TODO: If it is None, create a new instance using super().__new__(cls)
        # TODO: Return cls._instance
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # TODO: Initialize instance variable 'host' to "localhost"
        # TODO: Initialize instance variable 'connected' to False
        self.host = "localhost"
        self.connected = False
    
    def connect(self):
        # TODO: Set the 'connected' attribute to True
        # TODO: Print "Connected to database at localhost"
        self.connected = True
        print("Connected to database at localhost")
    
    def disconnect(self):
        # TODO: Set the 'connected' attribute to False
        # TODO: Print "Disconnected from database"
        self.connected = False
        print("Disconnected from database")