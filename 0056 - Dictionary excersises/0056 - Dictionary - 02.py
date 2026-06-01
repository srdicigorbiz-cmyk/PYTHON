print("***FIND MOST RECENT****************************")
def find_most_recent_book(library_catalog):
    # Write code here
    max=0
    result = None
    for book in library_catalog:
        if book["year"] > max:
            max = book["year"]
            result = book["title"]
    return result        
            


catalog=[{"title": "Book1", "year": 2000}, 
         {"title": "Book2", "year": 2010}, 
         {"title": "Book3", "year": 1990}]
print(find_most_recent_book(catalog))


print("****CALCULATE TOTAL VALUE***************************")
def calculate_total_value(items_dict):
    return sum(items_dict.values())

dictionary = {"item1": 2.1, "item2": 3.0, "item3": 1.0}
print(calculate_total_value(dictionary))