class DataProcessor:
    def process(self):
        """Template method defining the algorithm structure"""
        self.read_data()
        self.process_data()
        self.save_data()
    
    def read_data(self):
        print("Reading data...")
    
    def process_data(self):
        raise NotImplementedError("Subclasses must implement this")
    
    def save_data(self):
        print("Saving data...")

class CSVProcessor(DataProcessor):
    def process_data(self):
        print("Processing CSV data")


class JSONProcessor(DataProcessor):
    def process_data(self):
        print("Processing JSON data")

csv_processor = CSVProcessor()
csv_processor.process()
print()  # Empty line
json_processor = JSONProcessor()
json_processor.process()
