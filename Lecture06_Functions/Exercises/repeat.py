def repeat_name(name, num):
    for i in range(0, num):
        print(name)

name=input("Please give your name: ")
n=input("How many times do you want to see your name? ")
n=int(n)
repeat_name(name, n)