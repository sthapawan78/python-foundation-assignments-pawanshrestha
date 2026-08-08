raw_name = "  pAwAN SHREsthA "
raw_city = "DAmak"
raw_age = "23"
raw_email = " SthapAWAN78@gmail.COM "

# Clean the values
name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

# Ternary expression
status = "Adult" if age >= 18 else "Minor"

# Display the cleaned values
print("Name:", name)
print("City:", city)
print("Age:", age)
print("Email:", email)
print("Status:", status)