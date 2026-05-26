inventory={}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item]={'price':price, 'stock': stock}
        print(f"Item '{item}' added successfully.")

def update_stock(item, quantity):
    qty=int(quantity)
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        if (inventory[item]["stock"] + qty) <0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] += qty
            print(f"Stock for '{item}' updated successfully.")

def check_availability(item):
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return("Item not found")

def sales_report(sales):
    total_revenue=0
    for item, svalue in sales.items():
        
        if item in inventory:
            if svalue <= inventory[item]["stock"]:
                inventory[item]["stock"] -= svalue
                total_revenue += (inventory[item]["price"] * svalue)
            else:
                print(f"Error: Insufficient stock for '{item}'.")
        else:
            print(f"Error: Item '{item}' not found.")
    return(f"Total revenue: ${total_revenue:.2f}")
    
    






add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)