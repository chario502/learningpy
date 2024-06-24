import time

name = str(input("What is your name? "))

def func(name):
    print(f"Hello {name}")

print("Processing name..")
time.sleep(3)
func(name)
