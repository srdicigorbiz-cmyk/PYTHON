# Read input
products = input().split(',')
prices = input().split(',')

# Convert prices to floats
prices = [float(price) for price in prices]

# TODO: Write your code below
# Hint: Use zip(), reversed(), and enumerate() to process the data
result = (list(reversed(list(zip(products, prices)))))
for idx, data in enumerate((result), start=1):
    print(f"#{idx}. {data[0]}: ${data[1]:.2f}")
        
