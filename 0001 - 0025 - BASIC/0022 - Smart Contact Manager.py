def organize_contacts(contact_list):
        
    for contact in contact_list:
        contact["email"] = contact["email"].lower().strip()
        
        cleanphone=[]
        for p in contact["phone"]:
            if p.isdigit():
                cleanphone.append(p)
        contact["phone"]=''.join(cleanphone)
    

    filtered_contact_list=[]
    for contact in contact_list:
        if "@" in contact["email"] and "." in contact["email"]:
            if " " not in contact["email"]:
                 if len(contact["phone"])==10:
                        filtered_contact_list.append(contact)

    result=[]
    email_seen=[]
    phone_seen=[]
    for contact in filtered_contact_list:
         if contact["email"] not in email_seen:
              email_seen.append(contact['email'])
              if contact['phone'] not in phone_seen:
                   phone_seen.append(contact["phone"])
                   result.append(contact)
              
         
    
    return(result)


contact_list =[
    {"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"},
    {"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"},
    {"name": "John Doe", "email": "JOHN@email.com", "phone": "113-456-7890"},
    {"name": "John Doe", "email": "JOHNa@email.com", "phone": "123-456-7890"},
    {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"},
    {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}
    ]
print(organize_contacts(contact_list))