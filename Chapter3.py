#rzut kośćmi
#demonstruje generowanie liczb losowych

import random

die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You guessed:",die1, "and", die2, "sum is", total)

#Prezentacja programu Haslo

print("\nWitaj w systemie firmy Bezpieczny komputer SA")
print("--bezpieczeństwo to podstawa naszego działania")

password= input("Give me a password:")

if password == "sekret":
    print("You have access")
else:
    print("Incorrect password")


a = 3
a = 5 * a

print(a)



