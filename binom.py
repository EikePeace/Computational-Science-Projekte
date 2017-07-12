#!/usr/bin/python3
## Algorithmen und Datenstrukturen
## Hausaufgabe 3 - Dynamische Programmierung
## Abgabedatum: 12.7.2017
##
## Gruppennummer: 55
## Gruppenmitglieder:
## - Jan Heuer
## - Max Wiedenhöft
## - Eike Olaf Pubantz

## ACHTUNG: Verwenden Sie für Ihre Kommentare nur ein einzelnes #-Zeichen:
# so sollte Ihr Kommentar markiert werden
## so sind die Kommentare aus der Aufgabenstellung markiert.

## Implementieren Sie ab hier Ihre Lösungen:
def dynCompNChooseK(n, k):
    #print('Parameter n:') ## Als Ausgabe genügt es nicht, nur die Parameter und das Ergebnis auszugeben.
    #print(n)
    #print('Parameter k:')
    #print(k)
    ## hier soll Ihre Implementierung stehen.
    print("Berechnung von binom(%d, %d) mit Hilfe der zugehörigen Tabelle:" %(n, k))
    print()
    table = dynCompNChooseKTable(n, k) # Tabelle für binom(n, k)
    print("Ablesen aus %d.Zeile und %d.Spalte:" %(n, k))
    result = table[n][k] # Auslesen des Ergebnisses aus der Tabelle
    print("binom(%d, %d) = %d" %(n, k, result))
    print()
    return result

def dynCompNChooseKTable(n, k):
    #print('Parameter n:')
    #print(n)
    #print('Parameter k:')
    #print(k)
    ## hier soll Ihre Implementierung stehen.

    print("Tabelle für binom(%d, %d):" %(n, k))
    
    # Erstellen der Tabelle mit n+1 Zeilen (von 0 bis n)
    result = []
    for i in range(0,n+1): # Für jede Zeile leere Liste anfügen
        result.append([])

    # Basisfall: binom(n, 0) = 1 (mit n >= 0)
    for i in range(0,n+1): # Schleife über alle n-Werte
        result[i].append(1)
    # Ausgabe
    print("1. Basisfall:")
    print("binom(n, 0) = 1 (mit n >= 0)")
    for i in range(len(result)):
        print(result[i])
    print()

    # Basisfall: binom(0, k) = 0 (mit k > 0)
    for j in range(1,k+1): # Schleife über alle k-Werte (ab k=1)
        result[0].append(0)
    # Ausgabe
    print("2. Basisfall:")
    print("binom(0, k) = 1 (mit k > 0)")
    for i in range(len(result)):
        print(result[i])
    print()

    # Berechnen der Binomialkoeffizienten die nicht von den Basisfällen abgedeckt sind
    for i in range(1,n+1): # Schleife über alle n-Werte (ab n=1)
        for j in range(1,k+1): # Schleife über alle k-Werte (ab k=1)
            result[i].append(result[i-1][j] + result[i-1][j-1]) # binom(n, k) = binom(n-1, k) + binom(n-1, k-1)
    # Ausgabe
    print("Berechnen aller Binomialkoeffizienten die nicht von den Basisfällen abgedeckt sind:")
    print("binom(n, k) = binom(n-1, k) + binom(n-1, k-1)")
    for i in range(len(result)):
        print(result[i])
    print()

    return result

## Hier ist ein Testfall:
n = 5
k = 3

#n = int(input("n = "))
#k = int(input("k = "))

result = dynCompNChooseK(n, k)
#resultTable = dynCompNChooseKTable(n, k)

#print('berechnet:')
#print(result) ## 10
#print('mit der Tabelle:')
#print(resultTable)

##  #k
##[ #0  1  2  3  4  5
##  [1, 0, 0, 0, 0, 0], #n=0
##  [1, 1, 0, 0, 0, 0], #n=1
##  [1, 2, 1, 0, 0, 0], #n=2
##  [1, 3, 3, 1, 0, 0], #n=3
##  [1, 4, 6, 4, 1, 0], #n=4
##  [1, 5, 10,10,5, 1]  #n=5
##[
