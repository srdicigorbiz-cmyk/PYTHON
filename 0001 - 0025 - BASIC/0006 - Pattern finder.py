def find_occurrences(text, pattern):
    # Write your code here
    
    counter=0
    start_pos=[]
    for z in range(len(text)):
        slice=text[z:z+len(pattern)]
        if slice == pattern:
            counter += 1
            start_pos.append(z)
        else:
            i+=1
        
    return(((pattern in text), counter, start_pos))
    
    

# Read input
text = input("Input text:")
pattern = input("Input pattern:")

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)

