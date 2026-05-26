def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    shopping_cart = {}
    # Process each order in the list
    for order in orders:
        if ":" in order:
            try:
                # Split the order and add to cart
                ord_list=order.split(":")
                if ord_list[0] in shopping_cart.keys():
                    if int(ord_list[1]) >= 0:
                        shopping_cart[ord_list[0]] += int(ord_list[1])
                    else:
                        print(f"Negative quantity not allowed: {order}")
                        
                else:
                    if int(ord_list[1]) >= 0:
                        shopping_cart[ord_list[0]]=int(ord_list[1])
                    else: 
                        print(f"Negative quantity not allowed: {order}")
                        
            # Handle potential errors
            except ValueError:
            # Handle value errors
                print(f"Invalid quantity: {order}")
            except Exception as e:
                print("Error")# Handle unexpected errors
        else:
            print(f"Invalid format: {order}")
            continue
        
        
            
    # Return the completed cart
    return shopping_cart        
    
list_of_orders=["apple:-3","banana:2","milk:5"]
print(handle_shopping_cart(list_of_orders))