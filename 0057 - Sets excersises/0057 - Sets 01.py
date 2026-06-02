fruits = {"apple", "banana", "cherry"}
print(fruits)
print("*******************************")

vegetables = set(["carrot", "broccoli", "spinach"])
print(vegetables)
print("*******************************")

empty_set = set()
print(empty_set)
print("*******************************")


fruits = {"apple", "banana", "cherry"}
fruits.update("date")  # Adds each character in "date"
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'd', 'a', 't', 'e'}
print("*******************************")

fruits.update({"elderberry", "fig"})
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'elderberry', 'fig', 'd', 'a', 't', 'e'}
print("*******************************")

set1={"c","a","t"}
set2={"d","o","g"}
result=set1.intersection(set2)
print(result)
print("*******************************")

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date", "elderberry"}
difference_result=set1.difference(set2)
symmetric_difference_result = set1.symmetric_difference(set2)
print(difference_result, symmetric_difference_result)
print("*******************************")
def remove_duplicates(numbers):
    return sorted(list(set(numbers)))
list1 = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(list1))
print("*******************************")
def common_elements(arr1, arr2):
    return sorted(list(set(arr1).intersection(set(arr2))))
set1 = [1, 2, 3, 4, 5]
set2 = [4, 5, 6, 7, 8]
print(common_elements(set1, set2))
print("*******************************")
def recommended_products(viewed, purchased):
    return sorted(list((set(viewed)).difference(set(purchased))))
viewed = ["iPhone", "iPad", "MacBook", "Apple Watch"]
purchased = ["iPad", "Apple Watch"]
print(recommended_products(viewed, purchased))
