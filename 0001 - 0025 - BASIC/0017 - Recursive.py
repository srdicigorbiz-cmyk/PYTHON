######################################################
# recursive functions part 1
######################################################

def count_down(n):
    # Write code here
    if n == 0:
        print(0)
        return
    
    print(n)
    count_down(n-1)

######################################################
def print_sequence(n):
    # Write code here
    if n == 0:
        print("Blast off!")
        return
    print(f"T-minus {n}")
    print_sequence(n-1)

######################################################
# recursive functions part 2
######################################################
def factorial(n):
    if n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120

########################################################

def recursive_reverse(s):
    if len(s) <= 1:  # Base case: empty or single-character string
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]  # Recursive step

text = "hello"
result = recursive_reverse(text)
print(result)
# Output: olleh

######################################################
#Fibonaci

def fibonacci(n):
    # 1. BÁZIS: Mi van, ha n az 1. szám?
    if n == 1:
        return 0
    
    # 2. BÁZIS: Mi van, ha n a 2. szám?
    if n == 2:
        return 1
    
    # 3. REKURZÍV LÉPÉS: A képlet alapján
    return fibonacci(n - 1) + fibonacci(n - 2)  


print(fibonacci(8))

######################################################
#sum of digits in a number

def sum_digits(n):
    # Write code here
    if n < 10:
        return n
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(3689))
print(3687%10)


######################################################
#sum of digits in a nested lists
def sum_nested(nested_list):
    result=0
    for list_element in nested_list:
        if isinstance(list_element, list):
            result += sum_nested(list_element)
                
            
        else:
            result += list_element
    return result


list1=[[[[1]], 2], [3, [4, [5]]]]
print(sum_nested(list1))


######################################################
print("find_max_nested")
def find_max_nested(nested_list):
    current_max=0
    for element in nested_list:
        if isinstance(element, list):
            current_max = max(current_max, find_max_nested(element))        
        else:
            if current_max < element:
                current_max = element
    return current_max



list2=[3, [12, 5], [1, [20, 2]], 8]
print(find_max_nested(list2))

######################################################
# count_elements
def count_elements(list3):
    result=0
    for elem in list3:
        if isinstance(elem, list):
            result += count_elements(elem)
        else:
            result += 1 
    
    return result

list3=[1, [2, [3, 4,[4,4]]], 5]
print(count_elements(list3))

######################################################
# find files with extension

# A stringek a fájlnevek, a listák a mappák
def find_extension(file_list):
    result=[]

    for file in file_list:
        if isinstance(file, list):
            result.extend(find_extension(file))
        else:
            if file.endswith(".jpg"):
                result.append(file)
    return result

folder_structure = [
    "vacation_photo.jpg",
    "budget.xlsx",
    ["party_1.jpg", "party_2.jpg", "notes.txt"],
    ["work", ["project_final.jpg", "schema.png"]],
    "avatar.jpg"
]
print(find_extension(folder_structure))