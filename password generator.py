import string
import random
def generate_password():
    characters=list(string.ascii_letters + string.digits + "@!@£%&*")
    length=int(input('enter the length of the password'))
    random.shuffle(characters)
    password=[]
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
generate_password()
