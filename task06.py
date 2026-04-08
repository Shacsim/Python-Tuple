emails = (
    ("Zokir", "zokir@gmail.com"),
    ("Shokir", "shokir@yandex.ru"),
    ("Botir", "botir@mail.ru")
)

domains = []  

for name, email in emails:
    parts = email.split("@") 
    domain = parts[1]          
    domains.append(domain)     

print(domains)