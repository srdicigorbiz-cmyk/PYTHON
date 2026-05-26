def analyze_text(text):
   
    ###########cleaning##########
    text_prep=text.lower().strip().split()
    clean_text=[]
    for txt in text_prep:
        for t in txt:
            if t.isalpha():
                clean_text.append(t)
        clean_text.append(' ')
    
    new_raw=(''.join(clean_text)).split()

    ###########unique words##########
    unique_words=len(set(new_raw))
    ###########duplicate words##########
    seen_words=[]
    repeated_words=[]
    
    for word in new_raw:
        if word in seen_words:
            if word not in repeated_words:
                repeated_words.append(word)
        else:
            seen_words.append(word)

    ###########palindrome words##########
    palindromes=[]
    for word in new_raw:
        if word==''.join(reversed(word)):
            if word not in palindromes:
                palindromes.append(word)

    



    result={'unique_count': unique_words , 'repeated_words': sorted(repeated_words), 'palindromes':sorted(palindromes)}
    return result

text='A man a plan a canal Panama! A man a plan a canal! Did mom and dad see noon? Noon was hot!'
print(analyze_text(text))