# Algorithmen und Datenstrukturen
# Hausaufgabe 2 - Sortierverfahren
# Abgabedatum: 11.6.2017
#
# Gruppennummer: 55
# Gruppenmitglieder:
# - Jan Heuer
# - Max Wiedenhöft
# - Eike Olaf Pubantz

def sortMerge(a):
    print('Parameter a: ', a)

    if len(a) == 1: #Basisfall
        return a
    else:
        n = len(a)//2 #Mitte der Liste
        l = sortMerge(a[0:n]) #Sortieren der linken Teilliste
        r = sortMerge(a[n:len(a)]) #Sortieren der rechten Teilliste
        result = merge(l, r) #Zusammenführen der sortierten Teillisten
        print("Zwischenergebnis: ", result)
    return result

def merge(a, b):
    result = []
    while (len(a) != 0) and (len(b) != 0): #Zusammenführen bis eine Liste leer
        if a[0] < b[0]: #Anhängen des kleineren der beiden Elemente an Ergebnis
            result.append(a[0])
            a = a[1:len(a)] #Erstes Element von a entfernen
        else:
            result.append(b[0])
            b = b[1:len(b)] #Erstes Element von b entfernen
    if a != []: #Falls a noch nicht leer
        result = result + a #Anhängen von a an Ergebnis
    if b != []: #Falls b noch nicht leer
        result = result + b #Anhängen von b an Ergebnis
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
