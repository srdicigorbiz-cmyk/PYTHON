# Format: lambda parameters: value_if_true if condition else value_if_false
is_adult = lambda age: "Adult" if age >= 18 else "Minor"

print(is_adult(20))  # Output: "Adult"
print(is_adult(15))  # Output: "Minor"


##########################################################
#Grades using lambda
grade_status = lambda score: "Amazing!" if score == 100 else "Pass" if score >= 60 else "Fail"
print(grade_status(75))  # Output: "Pass"

size = lambda x: "Large" if x > 100 else "Medium" if x > 50 else "Small"
print(size(75))


##########################################################
# Read a number from input
number = int(input("Give me a number: "))
# Define your lambda function here
categorize_number = lambda x: "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
# Call your lambda function with the input number and print the result
print(categorize_number(number))

########################################################################################
#Sorting Strings by Length:
names = ["Alice", "Bob", "Charlie", "Diana"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)
# Output: ['Bob', 'Alice', 'Diana', 'Charlie']


##########################################################
#Sorting Dictionaries by Values:

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
sorted_grades = sorted(grades.items(), key=lambda x: x[1])
print(sorted_grades)
# Output: [('Charlie', 78), ('Alice', 85), ('Bob', 90)]


##########################################################
#Sorting Numbers by Absolute Value:

numbers = [-10, 15, -20, 25]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)
# Output: [-10, 15, -20, 25]


##########################################################
#Sorting Tuples by Multiple Criteria:

data = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
print(sorted_data)
# Output: [('Alice', 25), ('Charlie', 25), ('Bob', 30)]


##########################################################
# filter_list

# 1. Meghatározzuk az ŐRT (a függvényt)
def filter_list(numbers, rule):
    result = []
    for n in numbers:
        # Az őr megnézi a számot (n) a te szabályod (rule) alapján
        if rule(n): 
            result.append(n)
    return result

# 2. Van egy sorban álló tömegünk
my_list = [1, 5, 8, 12, 15, 20, 21]


# 3. Odaadod az őrnek a tömeget ÉS a szabályt (a lambdát)

valasz1 = filter_list(my_list, lambda n: n %3==0 and n%5==0)
print(valasz1) 


##########################################################
# lambda and recursion 1
def transform_nested(nested_list, func):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            # 1. Itt a REKURZIÓ! Mit csinálsz a belső lista eredményével? 
            # (Segítség: appendeld az eredményt a result-hoz!)
            result.append(transform_nested(item, func))
        else:
            # 2. Itt a LAMBDA! Alkalmazd a 'func'-ot az 'item'-re,
            # és az eredményt tedd a result-ba.
            result.append(func(item))
    return result

my_list = [1, [2, 3], 4]
print(transform_nested(my_list, lambda n: n*2))


##########################################################
# lambda and recursion 2
def deep_filter(nested_list, rule):
    new_list = []
    for element in nested_list:
        if isinstance(element, list):
            subres=deep_filter(element, rule)
            
            if subres:
                new_list.append(subres)

        else:
            if rule(element) == True:
                new_list.append(element)

   
    return new_list

data = [1, 12, [3, 15, [2]], 20, [1]]

print(deep_filter(data, lambda n: n%2==0))
# Csak a páros számok maradjanak meg!
# result = deep_filter(data, lambda n: n % 2 == 0)
# print(result) # Elvárt: [12, [[2]], 20]