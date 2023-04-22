def extract_name(email):
    parts = email.split('@')
    name = parts[0].replace('.', ' ').title()
    return name


emails = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = extract_name(email)
    user_choice = input(f"Is your name {name.title()}? (Y/n) ").lower()
    if user_choice in ('', 'y'):
        emails[email] = name
    else:
        name = input("Name: ").title()
        emails[email] = name

print("\nUsers:")
for email, name in emails.items():
    print(f"{name} ({email})")