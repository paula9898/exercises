name = 'Paulina'
surname = 'Otrebska'
age = 23

print(name, surname, age)

name1 = 'Bob'
comunicat = 'Buy se glue'

print(f"Hello, {name1}, {comunicat}")

print("Hej,", name1 + ".", comunicat)

# zad_7

height = 1.74
weight = 52

askWeight = float(input("Please, enter my your weight in kg: "))

askHeight = float(input("Please, enter me your height in cm: "))

BMI = askWeight / (askHeight / 100) ** 2

print("Your BMI is: ", BMI)

# zad.9

word = input("Enter a string: ")

word1 = word

word1 = word1.replace(word1[0], 'y')
word1 = word1.replace(word1[-1], 'i')

print(word1) #mozesz też wykorzystać listę

#zad.10

a = 5
b = 6



new_string = str(a) + str(b)

print(new_string)

#zad.11

name1 = "Kacper"
name2 = "Lucjan"
name3 = name1[:3] + name2[-3:]

print(name3)

#zad.12

text2 = "comment"
text1 = text2[:]

print(text1)


