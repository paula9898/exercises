#W pewnej grze liczbowej wylosowano następujące liczby:
#wynik = [12,1,45,76,50,23]. Okazało się jednak,
# że wylosowane wartości powinny zawierać się w przedziale od 1 do 49.
# Napisz program zastępujący dowolne liczby – nie tylko te konkretne z zadania -
# występujące w liście, które nie spełniają tego kryterium, na wylosowane liczby,
# które będą je spełniać. Program powinien
#także zakomunikować, że znalazł błędną wartość i dokonał dla niej zmiany.
import random

list =[12,1,45,76,50,23]

for i in range(len(list)):
    if list[i] in range(1, 50):
        continue
    else:
        list[i] = random.randint(1,50)
        print("Error found")

print(list)


