correct_username = "sai nathan"
correct_password = "lupoQ!"

for i in range(3):

    username = input("username: ")
    password = input("password: ")

    if username == correct_username and password == correct_password:
        print("login success")
        break
    
    else:
        print("wrong password")
        
else:
    print("accound blocked") 
