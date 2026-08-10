# Write code here
ticket = 200
movie_categories = {
            "comedy":30,
            "action":40,
            "horror":20
}

popcorn_categories = {
    "S":100,
    "M":150,
    "L":200
}

payment_types ={
    "1":0.9,
    "0":1
}

movie_category = input()
popcorn = input()
no_people = int(input())
payment = str(input())

if movie_category in movie_categories:
    price = ticket + movie_categories[movie_category]

if popcorn in popcorn_categories:
    price += popcorn_categories[popcorn]

if payment in payment_types:
    price *= payment_types[payment]

bill = round(price * no_people)

print(f"${bill}")