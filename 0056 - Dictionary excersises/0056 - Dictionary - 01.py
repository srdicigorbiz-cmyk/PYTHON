print("*****CALCULATE AVERAGE GRADES**************************")
def calculate_average_grade(student_grades):
    # Write code here
    result=0
    count =0
    for key, value in student_grades.items():
        result += value
        count += 1
    avg=result/count
    return avg
student_grades = {"Alice": 85.5, "Bob": 88.5, "Charlie": 90.0, "David": 89.0, "Eve": 91.5}
print(calculate_average_grade(student_grades))
print("*****UPDATE ENTER NEW VALUE**************************")
def add_book(catalog, title, author, year):
    catalog[title]= {"author": author, "year":year, "available":True}
catalog = {}
add_book(catalog, "The Catcher in the Rye", "J.D. Salinger", 1951)
print(catalog)
print("*****SEARCH BY KEY**************************")
def search_book(catalog, title):
    if title in catalog:
        return catalog[title]
    else:
        return "Book not found in the catalog"
    
catalog = {
    "1984": {"author": "George Orwell", "year": 1949, "available": True},
    "Brave New World": {"author": "Aldous Huxley", "year": 1932, "available": True}
}
print(search_book(catalog, "1984"))
print("*******************************")
