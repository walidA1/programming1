def new_password(oldpassword,newpassword):
    if len(newpassword)>=6 and newpassword!=oldpassword:
        return True
    else:
        return False
oldpassword=input("Geef input: ")
newpassword=input("geef input: ")
print(new_password(oldpassword, newpassword))












