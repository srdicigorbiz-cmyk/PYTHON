i = input()
num_list = i.split(" ")
num_list = sorted([int(x) for x in num_list])
num_list = [str(x) for x in num_list]

print(" ".join(num_list))
