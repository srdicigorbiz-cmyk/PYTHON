def greeting_generator(name):
    def get_greeting(name):
        return f"Hello, {name}"
    return get_greeting(name)

name = "Igor"
print(greeting_generator(name))