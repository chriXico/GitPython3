# Take email address from user
email = input("Enter your email address: ").strip()

# Slice and store username
username = email[:email.index("@")]

# Slice and store domain mame
domain = email[email.index("@")+1]

# Make output result using username and domain name
result = "Your username = {} \nYour domain = {}" .format(username,domain)

# Print the result
print(result)