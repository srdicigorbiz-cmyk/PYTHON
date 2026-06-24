def function_builder(n1, n2):
    def my_func(x):
        return (n1*x)+n2
    return my_func
print(function_builder(1,1)(3))