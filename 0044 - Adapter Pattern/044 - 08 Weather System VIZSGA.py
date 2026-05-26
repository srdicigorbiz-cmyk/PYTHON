class ModernWeatherSystem:
    def __init__(self):
        self.temp_list = []
    def record_temperatures(self, temp_list):
        
        if all(isinstance(x, (int, float)) for x in temp_list):
            self.temp_list = temp_list
        else:
            raise ValueError("A lista hibás elemeket tartalmaz.")

    def get_report(self):
        result = dict()
        if self.temp_list:
            if len(self.temp_list)>0:
                result["average"]=sum(self.temp_list)/len(self.temp_list)
                result["min"]=min(self.temp_list)
                result["max"]=max(self.temp_list)
            return result

        else:
            return "No data."

class LegacySensor:
    def get_raw_string_data(self):
        return "15.5;22.0;HIBA;18.2;30.1;NODATA;20.0"

class SensorAdapter(ModernWeatherSystem):
    def __init__(self, oldsys):
        super().__init__()
        self.oldsys = oldsys
    def record_temperatures(self, data):
        read_result=self.oldsys.get_raw_string_data().split(';')
        result = [float(x) for x in read_result if not x.isalpha()]                
        super().record_temperatures(result)

modern=ModernWeatherSystem()
old = LegacySensor()
adapter = SensorAdapter(old)

print(modern.record_temperatures([1,2,3,5,6])) 
print(modern.get_report())
print("******************")
print(modern.record_temperatures([])) 
print(modern.get_report())
print("******************")
print(adapter.record_temperatures([]))
print(adapter.get_report())