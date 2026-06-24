# Write code here
def my_decorator(n):
    def actual_decorator(func):
        def wrapper(s):
            opening_tag = ""
            closing_tag = ""
            for x in range(n):
                if x%2:
                    opening_tag += "<p>\n"
                    closing_tag = "</p>\n"+closing_tag
                else:
                    opening_tag += "<div>\n"
                    closing_tag = "</div>\n"+closing_tag
            
            return f'{opening_tag}<b>\n{func(s)}\n</b>\n{closing_tag}'

        return wrapper
    return actual_decorator


# Don't change below this line
n = int(input())

@my_decorator(n)
def my_function(s):
    return s.upper()

result = my_function(input())
print(result)