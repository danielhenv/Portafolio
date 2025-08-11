name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Student: {is_student}")