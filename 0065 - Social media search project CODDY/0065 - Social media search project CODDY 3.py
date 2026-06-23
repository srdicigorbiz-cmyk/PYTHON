def get_search_filters(filter_str):
    
    if len(filter_str)==0:
        return {}
    else:
        s_data = [x.split("=") for x in filter_str.split("&")]
    
    result= {}
    for item in s_data:
        result[item[0]]=item[1]

    return result




input1 = ("key=David&type=user&city=Paris")
input2 = ("key=&type=user")
input3 = ("")
print(get_search_filters(input1))
print(get_search_filters(input2))
print(get_search_filters(input3))
