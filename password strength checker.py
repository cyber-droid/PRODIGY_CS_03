import re
# Function to check password strength
def password_strength(password):
    if len(password) < 8:
        return "Weak Password: Password must be at least 8 characters long."
    if not re.search("[A-Z]", password):
        return "Weak Password: Add at least one uppercase letter."
    if not re.search("[a-z]", password):
        return "Weak Password: Add at least one lowercase letter."
    if not re.search("[0-9]", password):
        return "Weak Password: Add at least one number."
    if not re.search("[@#$%^&*]", password):
        return "Weak Password: Include at least one special character."
    return "Strong Password!"
# Take user input
user_password = input("Enter a password to check its strength: ")
# Call the function and display the result
print(password_strength(user_password))
