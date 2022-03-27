# ZAD.1
# Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
# wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
# pobiera od użytkownika łańcuch i sprawdza czy odpowiada on kluczowi ze słownika.
# Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest U2".
# W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

# {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2',
# 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}


bands = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2',
         'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

keys = print(bands.keys())

string = input("Enter a name of a Cd: ")

if string in bands:
    print("Wykonawcą albumu: ", string, "jest: ", bands[string])
else:
    print("Brak danych")
