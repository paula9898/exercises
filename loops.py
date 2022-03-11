lista_liczb = []
for i in range(1,10):
    lista_liczb.append(i)

liczba = list(range(1,10))

liczby = []
for i in range(1,10):
    if i % 2 == 0:
        liczba.append(i**2)

liczby =[i**2 for i in range(1,10) if i % 2 == 0]

liczba = [i for i in range(1,20) if i% 2 == 0 if i % 3 == 0]
print(liczba)

sekwancja = "ACCGTA"
sekwancja_lower = [z.lower() for z in sekwancja]
lista = []
zasady = ['puryna' if z == 'A' or z =='G' else 'piramidyna' for z in sekwancja]
print(zasady)
for z in sekwancja:
    if z == 'A' or z:
        lista.append('puryna')
    else:
        lista.append('piramidyna')

user = True
if user:
    pass