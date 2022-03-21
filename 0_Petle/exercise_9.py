# zad.9
# Zadeklaruj trzy zmienne - pierwszą przechowującą informację o startowym poziomie paliwa,
# drugą określającą ilość astronautów na pokładzie,
# a trzecią mówiącą, na jakiej wysokości znajduje się rakieta.

# Poproś użytkownika o podanie początkowego poziomu paliwa. Użytkownik ma kontynuować czynność,
# dopóki nie poda poprawnej wartości - mieszczącej się pomiędzy 5000 a 30000 litrów.
# Stwórz drugą pętlę, która będzie prosić o użytkownika o podanie odpowiedniej ilości astronautów znajdujących na pokładzie.
# Pętla ma walidować podaną liczbę - tak, aby była dodatnia i nie większa niż 7.
# Zasymuluj pętlą nr 3 lot statku kosmicznego.
# Kolejne iteracje mają zmniejszać obecny poziom paliwa o określoną wartość. Zużycie paliwa co 100 km zależy od ilości astronautów na pokładzie i jest równe: 300 l + 100 * ilosc_astronautow.

# Pętla więc ma uruchamiać się co 100 km i wykonać tyle iteracji, na ile wystarczy paliwa. Co każdą iterację ma wyświetlać się aktualnie przebyty dystans przez statek kosmiczny.

fuelLevel = int(input("Enter a start fuel level: "))

while fuelLevel not in range(5000, 30000):
    fuelLevel = int(input("Enter a start fuel level: "))

flag = True
while True:
    astronauts = int(input("Enter a number of astronauts: "))

    if astronauts in range(0, 7):
        flag = False
        print(astronauts)
