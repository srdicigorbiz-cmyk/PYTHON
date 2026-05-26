def clean_email_list(emails):
    # Write your code below
    clean_email=map(lambda x: x.strip().lower(), emails) 
    valid_emails = filter(lambda e: len(e) > 0 and e.count('@') == 1 and e[0] != '@' and e[-1] != '@', clean_email)
    return list(valid_emails)

emails_list=['USER@@DOMAIN.COM','   spacedomain.com ','  NoSpaces@domain.com']
print(clean_email_list(emails_list))
