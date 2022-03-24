# zad.3
lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2']

# Niech program:
# wydrukuje te listy
# wydrukuje pierwszy oraz czwarty element z lista1
# przypisze drugiemu elementowi lista2 wartości drugiego elementu z lista3
# przypisze trzeciemu elementowi lista3 wartość tekstową wpisaną z klawiatury
# doda nowy element ‘słowo’ do lista1 za pomocą metody .append()
# skasuje element o indeksie 2 z lista1
# wyznaczy liczbę elementów lista3
# powiększy lista1 o elementy lista3
# Po każdej przeprowadzonej zmianie wydrukuje zmienioną listę.

print(lista1)
print(lista2)
print(lista3)

print(lista1[0], lista1[3])

lista2[1] = lista3[1]
print(lista2)

lista3[2] = input("Enter a word: ")

print(lista3)

lista1.append("DE")
print(lista1)

lista1.pop(2)
print(lista1)

print(len(lista3))

lista1.extend(lista3)

print(lista1)


