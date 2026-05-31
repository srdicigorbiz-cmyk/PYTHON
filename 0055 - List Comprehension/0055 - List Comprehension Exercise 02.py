# Create a list comprehension that takes in a list of tuples lst, 
# and returns a new list named new_lst that stores the same tuples 
# if the sum of the integers in the tuple is greater than 20. 
# 
# Also, each tuple in new_lst should be sorted in descending order.

lst = [(1, 5, 15), (7, 8, 10), (6, 6, 6), (2, 3, 30)]
new_lst = [tuple(sorted(x, reverse=True)) for x in lst if sum(x)>20]
print(new_lst)