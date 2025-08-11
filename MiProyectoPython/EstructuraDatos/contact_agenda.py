agenda = {}

def add_contact(name, phone):
    agenda[name] = phone

add_contact("Anna", "123456789")
add_contact("Luis", "987654321")

print("Contact agenda:")
for name, phone in agenda.items():
    print(f"{name}: {phone}")