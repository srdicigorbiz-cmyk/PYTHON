# 1. Hozz létre egy listát 3-4 könyvvel (szótárakkal)
library = [
    {"title": "The Republic", "author": "Plato", "available": True},
    {"title": "Beyond Good and Evil", "author": "Nietzsche", "available": False},
    {"title": "The Antichrist", "author": "Nietzsche", "available": True},
    # Adj hozzá még egyet nyugodtan...
]

def find_books_by_author(library, author_name):
    # Ide jön a logikád
    # Tipp: hozz létre egy üres listát a találatoknak
    # Végigmegy a listán. 
    # Kigyűjti azoknak a könyveknek a címét, amiket az adott 
    # szerző írt ÉS elérhetőek (available értéke True).
    # Visszatér a címek listájával.
    s_result=[]
    
    for book in library:
        if author_name.lower().strip() == book["author"].lower() and book["available"] is True:
            s_result.append(book["title"])
    
    if len(s_result)> 0:
        return s_result
    else:
        return(f"Sajnos {search_author} könyvei jelenleg nem elérhetőek.")

# 2. Kérj be egy nevet a felhasználótól
search_author = input("Melyik szerzőt keresed? ")

# 3. Hívd meg a függvényt és tárold el az eredményt
results = find_books_by_author(library, search_author)

# 4. Írasd ki az eredményt a feltételek szerint (if/else) 
# ha a szerzőtől nincs elérhető könyv, írja ki: 
# "Sajnos [Szerző] könyvei jelenleg nem elérhetőek."
print(results)