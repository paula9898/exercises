#zad.1

a = 3
b = 5
c = 7

if a**2 + b**2 == c**2:
    print(" To jest trojkat prostokatny")
else:
    print("To nie jest trojkat prostokatny")

#zad.2

number = 1



#zad.3

choose = ["kamien", " papier", "nozyczki"]

user_number1 = input("Enter kamien, papier or nozyczki: ")
user_number2 = input("Enter kamien, papier or nozyczki: ")

if user_number1 == user_number2 :
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










