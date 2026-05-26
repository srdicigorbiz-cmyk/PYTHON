def process_numbers(numbers):
    
    filtered_numbers= filter(lambda x: x >0, numbers)

    processed_numbers = map(lambda number: number * 2 if number%2==0 else number * 3, filtered_numbers)
    return list(processed_numbers)


numbers=[-4, 0, 5, 2, 8, -3, 7]
print(process_numbers(numbers))
