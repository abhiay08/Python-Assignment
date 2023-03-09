'''
Pascal Triangle to take N as input'''
'''if N=4
       1
      1 1
     1 2 1
    1 3 3 1
'''

''' Coding By Abhishek '''

def printPascal(N):

    arr = [1]

    temp = []

    print("pascal's triangle of", N, "Rows...")

    for i in range(N):

        print("rows", i+1, end=" : ")

        for j in range(len(arr)):

            print(arr[j], end=' ')

        print()        

        temp.append(1)

        for j in range(len(arr)-1):

            temp.append(arr[j] + arr[j + 1])

        temp.append(1)

        arr = temp

        temp = []

N=int(input("Enter the Number for the pascal triangle :"))

printPascal(N)
