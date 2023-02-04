from validator_collection import validators

em = input("What's your email address? ")
try:
    mail = validators.email(em)
    print("Valid")
except:
    print("Invalid")
