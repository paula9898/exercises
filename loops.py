lista_liczb = []
for i in range(1, 10):
    lista_liczb.append(i)

liczba = list(range(1, 10))

liczby = []
for i in range(1, 10):
    if i % 2 == 0:
        liczba.append(i ** 2)

liczby = [i ** 2 for i in range(1, 10) if i % 2 == 0]

liczba = [i for i in range(1, 20) if i % 2 == 0 if i % 3 == 0]
print(liczba)

sekwancja = "ACCGTA"
sekwancja_lower = [z.lower() for z in sekwancja]
lista = []
zasady = ['puryna' if z == 'A' or z == 'G' else 'piramidyna' for z in sekwancja]
print(zasady)
for z in sekwancja:
    if z == 'A' or z:
        lista.append('puryna')
    else:
        lista.append('piramidyna')

user = True
if user:
    pass

# zad.1
# Napisz program wyświetlający liczby całkowite z
# przedziału <0; y>, gdzie y podaje użytkownik. Wykonaj to na pętli for i while.

y = int(input("Enter a number: "))

for i in range(0, y + 1):
    print(i)

counter = 0

while counter <= y:
    print(counter)
    counter += 1

# zad.2
# Napisz program wyświetlający liczby całkowite z przedziału <100; 50>
# w porządku malejącym. Wykonaj to na pętli for i while.

counter = 100

while counter >= 50:
    print(counter)
    counter -= 1

for z in range(100, 50, -1):
    print(z)

# zad.3

# Napisz program wyświetlający liczby z przedziału <0, 5, 10, 15, …, 100>

for a in range(0, 101, 5):
    print(a)

#zad.4
#Napisz program, wyświetlający n kolejnych potęg liczby 2. Wartość n podaje użytkownik.
