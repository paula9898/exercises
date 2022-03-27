# zad.3
# Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze).
# Wartości przypisane do tych kluczy mają być równe ilości wystąpień słowa w tekście
from collections import Counter
from collections import OrderedDict
text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore," \
       " While I nodded, nearly napping, suddenly there came a tapping," \
       " As of someone gently rapping, rapping at my chamber door." \
       " This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."

list = text.split()

print(list)
counts = dict()

for word in list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1


print(counts)



#version with counter
#print(Counter(list))
