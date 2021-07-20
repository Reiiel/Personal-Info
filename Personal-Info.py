def personal_details():
    input_name = str(input("Enter Name: "))
    input_age = str(input("Enter Age: "))
    input_address = str(input("Enter Address: "))
    address = input_address
    print("Name: {}\nAge: {}\nAddress: {}".format(name,age, address))
    personal_details()
