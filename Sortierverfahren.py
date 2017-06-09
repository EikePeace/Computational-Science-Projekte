# Algorithmen und Datenstrukturen
# Hausaufgabe 2 - Sortierverfahren
# Abgabedatum: 11.6.2017
#
# Gruppennummer: <Bitte eintragen>
# Gruppenmitglieder:
# - <Bitte eintragen>
# - <Bitte eintragen>
# - <Bitte eintragen>

# Implementieren Sie ab hier Ihre Lösungen:
def sortMerge(a):
    print('Parameter a:', a)

    if len(a) == 1:
        return a
    else:
        n = len(a)//2
        l = sortMerge(a[0:n])
        r = sortMerge(a[n:len(a)])
        result = merge(l, r)
        print("Zwischenergebnis: ", result)
    return result

def merge(a, b):
    result = []
    while (len(a) != 0) and (len(b) != 0):
        if a[0] < b[0]:
            result.append(a[0])
            a = a[1:len(a)]
        else:
            result.append(b[0])
            b = b[1:len(b)]
    if a != []:
        result = result + a
    if b != []:
        result = result + b
    return result

def sortHeapDesc(a):
    print('Parameter a:')
    print(a)
    # hier soll Ihre Implementierung von absteigendem HeapSort stehen.
    result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result

# Hier ist ein Testfall:
liste = [3, 2, 1, 9, 17, 4, -1, 0]
print(liste)
mergeResult = sortMerge(liste)
#heapResult = sortHeapDesc(liste)

print()
print('Endergebnis:')
print(mergeResult)
#print(heapResult)

# Das Ergebnis sollte folgende Liste sein:
# [-1, 0, 1, 2, 3, 4, 9, 17]
# [17, 9, 4, 3, 2, 1, 0, -1]
