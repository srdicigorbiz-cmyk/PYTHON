def calculate_discount(price, discount_percentage):
    # Write code here
    final_price=round((price - (price * (discount_percentage/100))),2)
    return final_price


price=float(input("price"))
discount_percentage=float(input("disc"))
result= calculate_discount(price, discount_percentage)
print(result)