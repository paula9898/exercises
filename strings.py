# zad.1

name = input("Enter your name:")

print(name)

print(len(name))
print(name[0], name[-1])
print(name[-4], name[-3], name[-2])

# zad.2

numbers_of_cats = int(input("How many cats does Ala have?: "))
found_cats = 3
print(f"Today Ala has found, {found_cats} cats in the wood")

numbers_of_cats = numbers_of_cats + 3
print("Now Ala has,{}".format(numbers_of_cats))

text = "Now Ala has,{}".format(numbers_of_cats)

print("Now" + "," + "Ala" + "," + "has" + "," + "{}".format(numbers_of_cats))


#zad.3

word = "DOM"

print(word)
print(word.replace("DOM", 'domek'))

#zad.4

message = 'today is friday'
print(message.upper())

#zad.5

message1 = "     example".strip()
print(message1)

#zad.6


