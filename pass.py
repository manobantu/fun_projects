master_pwd = input("What is the master password? ")

mode = input("Would you like to add a new password or view existing ones? (view/add), press q to quit. ").lower()
def view():
    pass
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd)
    



while True:
    if mode == "q":
        break   
    if mode == "view": 
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid code")
        continue  