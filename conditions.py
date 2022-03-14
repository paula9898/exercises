# zad.1

a = 3
b = 5
c = 7

if a ** 2 + b ** 2 == c ** 2:
    print(" To jest trojkat prostokatny")
else:
    print("To nie jest trojkat prostokatny")

# zad.2

number = 1

# zad.4

choose = ["kamien", " papier", "nozyczki"]

user_number1 = input("Enter kamien, papier or nozyczki: ")
user_number2 = input("Enter kamien, papier or nozyczki: ")

if user_number1 == user_number2:
    print("Remis")
elif user_number1 == "papier" and user_number2 == "kamien":
    print("Wygral:  user_number1")
elif user_number1 == "kamien" and user_number2 == "papier":
    print("Wygral:  user_number2")
elif user_number1 == "nozyczki" and user_number2 == "kamien":
    print("Wygral:  user_number2")
elif user_number1 == "kamien" and user_number2 == "nozyczki":
    print("Wygral:  user_number1")
elif user_number1 == "papier" and user_number2 == "nozyczki":
    print("Wygral:  user_number2")
elif user_number1 == "nozyczki" and user_number2 == "papier":
    print("Wygral:  user_number1")
else:
    print("Błędne dane!!")

# zad.2

number = int(input("Enter a number: "))

if number == 0:
    print(" You have entered number 0")
elif number > 0:
    print(" Your number is bigger than 0")
else:
    print("Your number is lower than 0 ")

# zad.3
liczby = []
for i in range(3):
    number = int(input("Enter a number: "))
    liczby.append(number)

    max = liczby[0]

for n in liczby:
    if max < n:
        max = n
print(max)

print(liczby)

# zad.5

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

if num1 % 2 == 0 or num2 % 2 == 0:
    print("One of the number is even")
else:
    print("None of them is even")

# zad.6

import random
import time

# 1. Użytkownik wybiera czy obstawia reszkę, czy orła (literka r – reszka,
# literka o – orzeł)
# 2. Po dokonaniu wyboru, Komputer odlicza 3,2,1, a następnie dokonuje
# 'rzutu', czyli losowego wyboru orzeł / reszka.
# 3. Komputer wyświetla wynik rzutu.
# 4. Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli
# komputer to dodaje punkt dla komputera.

import random



orzeł_czy_reszka = int(input("Orzeł - o czy reszka - r: "))
o = 1
r = 0


n = 3

while n >= 1:
    print(n)
    n -= 1

computer_choice = random.randint(0, 1)
print("Computer choice is: ",computer_choice)
print("User  choice is: ", orzeł_czy_reszka)

computer = 0
user = 0

if orzeł_czy_reszka == computer_choice:
    user += 1
    print("You won")
else:
    computer += 1
    print("Compuer won.")

print("User points: ", user)
print("Computer points: ", computer)
