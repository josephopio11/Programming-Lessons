# stored_pass <- "password"
stored_pass = "password"
# password <- ""
password = ""
# pass_mismatch <- stored_pass != password
pass_mismatch = stored_pass != password

# WHILE pass_mismatch
while pass_mismatch:
    # OUTPUT "Enter your password:"
    print("Enter your password:")
    # password <- USERINPUT
    password = input()
    # pass_mismatch <- stored_pass != password
    pass_mismatch = stored_pass != password
    # END WHILE

# OUTPUT "Access granted"
print("Access granted")
