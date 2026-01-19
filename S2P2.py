import random

Number = int(input("Guess the number"))
Secret_number = random.randint(1, 10)
print(Secret_number)

if Number > Secret_number:
    print("Guess number too High")
elif Number < Secret_number:
    print("Guess number too Low")
