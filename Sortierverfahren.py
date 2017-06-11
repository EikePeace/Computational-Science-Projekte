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
    print('Parameter a: ', a)

    l = len(a)-1 #letztes Element des Baums
    p = (l-1)//2 #letzter Vaterknoten im Baum

    print("Heapeigenschaft herstellen")
    while p >= 0: #Schleife über alle Vaterknoten
        a = heapify(a, p, l)
        print(a)
        p -= 1
    print("Heap fertig")
    print()

    while l > 0:
        a = swap(a, 0, l)
        print("Sortierschirtt: ", a)
        l -= 1 #Leztztes Element gehört nicht mehr zum Baum
        a = heapify(a, 0, l) #Heapeigenschaft wieder herstellen
        print("Neuer Heap: ", a)

    return a

def heapify(a, p, l): #p: Knoten für den Heapeigenschaft hergestellt wird, l: Ende des Baums
    if 2*p+1 > l: #p hat kein Kind, daher nichts zu machen
        return a
    if 2*p+1 == l: #p hat nur ein Kind
        if a[p] < a[2*p+1]:
            return a
        else:
            a = swap(a, p, 2*p+1)
            return a
    if a[2*p+1] < a[2*p+2]: #Bestimmen des kleineren Kindes von p
        if a[2*p+1] < a[p]: #Wenn Kind kleiner als Vater
            a = swap(a, p, 2*p+1) #Tauschen
            a = heapify(a, 2*p+1, l) #Heapeigenschaft für verändertes Kind wiederherstellen
    elif a[2*p+2] < a[p]:
            a = swap(a, p, 2*p+2)
            a = heapify(a, 2*p+2, l)
    return a

def swap(l, m, n): #Tauscht l[m] und l[n]
    h = l[m]
    l[m] = l[n]
    l[n] = h
    return l

# Hier ist ein Testfall:
liste = [3, 2, 1, 9, 17, 4, -1, 0]

print("Mergesort:")
mergeResult = sortMerge(liste)
print()
print('Endergebnis: ', mergeResult)
print()

print("Heapsort:")
heapResult = sortHeapDesc(liste)
print()
print('Endergebnis: ', heapResult)
print()

# Das Ergebnis sollte folgende Liste sein:
# [-1, 0, 1, 2, 3, 4, 9, 17]
# [17, 9, 4, 3, 2, 1, 0, -1]
