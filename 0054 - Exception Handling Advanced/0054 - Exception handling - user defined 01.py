def contact_details(mobile):
    #your code goes here
    try:
        if not mobile.isdigit() or len(mobile)!=12:
            raise ValueError("Invalid")
        else:
            print("valid")
    except Exception as obj:
        print(obj)
    
contact_details("12345678912")
contact_details("123456789121")