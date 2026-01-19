import math  

def main():
 A = int(input("Value of A?"))
 B = int(input("Value of B?"))
 pythag(A,B)

def pythag(A,B):
   C = math.sqrt((A ** 2) + (B** 2))
   print(C)

main()
2