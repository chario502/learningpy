# Basic Base64 encrypt/decrypt script

import base64

def encryptPass(password):
    encodedPass = base64.b64encode(password.encode())
    print(encodedPass)
def decryptPass(encPass):
    decrPass = base64.b64decode(encPass.encode())
    print(decrPass)

choice = input("Would you like to encrypt (e) or decrypt (d)? ")
userPass = input("Enter your password: ")

if choice == "Encrypt" or choice == "e":
    encryptPass(userPass)
elif choice == "Decrypt" or choice == "d":
    print("If output looks malformed, please remove the b and ' from the password.")
    decryptPass(userPass)
else:
    null = 0
