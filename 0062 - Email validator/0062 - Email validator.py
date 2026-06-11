def validate(string):
    if string.count('@') != 1:    
        return False
    recipient = string.split("@")[0]
    if not 3 <= len(recipient) <=24:
        return False
    if not (recipient[0].isalnum() and recipient[-1].isalnum()):
        return False
    for letter in recipient:
        if not (letter.isalnum() or "."==letter or "_"==letter):
            return False
    domain = string.split("@")[1].split('.')[0]
    if not 3 <= len(domain) <=12:
        return False
    for letter1 in domain:
        if not (letter1.isalnum() or "-"==letter1):
            return False
    top_domain = string.split("@")[1].split('.')[1]
    allowed = ["com","net", "org", "tech"]
    if top_domain not in allowed:
        return False
    return True

if __name__ == "__main__":
    print("Enter email:")
    email = input()
    if validate(email):
        print("Email is valid")
    else:
        print("Email is invalid")