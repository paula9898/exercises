# zad.10

#while liczba > n:
    #if liczba % n == 0:
       # sum += n
        #n += 1

#print(sum)
liczba = int(input("Enter a number: "))
sum = 0
i = 1

for i in range(i,liczba):
    if liczba % i == 0:
        sum += i
        print(i)
    else:
        print("To nie jest jej dzielnik")


if sum == liczba:
    print("To jest doskonała liczba")
else:
    print("To nie jest doskonała liczba")
