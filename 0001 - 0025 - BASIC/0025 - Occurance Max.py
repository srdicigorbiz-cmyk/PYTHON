def occurMax(a):
    no_set= set(a)
    occur_dict=dict()
    for _ in no_set:
        occur_dict[_]=0
    for no in a:
        if no in occur_dict:
            occur_dict[no] += 1
    max_no = max(occur_dict.values())
    win_no= []
    for key, value in occur_dict.items():
        if value == max_no:
            win_no.append(key)
    for wn in a:
        if wn in win_no:
            return wn
test1 = [4, 2, 1, 2, 5, 2, 1, 6, 34, 1]
print(occurMax(test1))

def occurMax(a):
    occur_dict=dict()
    for x in a:
        if x in occur_dict:
            occur_dict[x] += 1
        else:
            occur_dict[x] = 1
    max_value=max(occur_dict.values())
    for key, values in occur_dict.items():
        if values == max_value:
            return key

    return occur_dict
test1 = [4, 2, 1, 2, 5, 2, 1, 6, 34, 1]
print(occurMax(test1))
