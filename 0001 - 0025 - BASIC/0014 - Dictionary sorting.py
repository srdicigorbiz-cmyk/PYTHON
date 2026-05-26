raw_dict = {'x': 10, 'y': 5, 'z': 8}
# 1. Csak a számokat rendezzük sorba
sorted_values = sorted(raw_dict.values()) 

result = {}

# 2. Végigmegyünk a sorba rendezett számokon
for val in sorted_values:
    # 3. Végigmegyünk a szótár PÁRJAIN
    for key, value in raw_dict.items(): 
        if val == value:
            result[key]=value

print(result)