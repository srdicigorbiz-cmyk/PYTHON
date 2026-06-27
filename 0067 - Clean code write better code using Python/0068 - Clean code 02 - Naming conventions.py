import my_module


class ImportantClass:
    MY_CONSTANT = 3.14
    def good_function(self, variable):
        return variable
        
    def better_function(self):
        return MY_CONSTANT
        

def __name__ == '__main__':
    var = my_module.secret()
    important_class = ImportantClass()
    important_class.good_function(var)
    print(important_class.better_function())
