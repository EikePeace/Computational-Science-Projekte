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
    print('Parameter n:') ## Als Ausgabe genügt es nicht, nur die Parameter und das Ergebnis auszugeben.
    print(n)
    print('Parameter k:')
    print(k)
    ## hier soll Ihre Implementierung stehen.
    table = dynCompNChooseKTable(n, k) # Tabelle für binom(n, k)
    result = table[n][k] # Auslesen des Ergebnisses aus der Tabelle
    return result

def dynCompNChooseKTable(n, k):
    print('Parameter n:')
    print(n)
    print('Parameter k:')
    print(k)
    ## hier soll Ihre Implementierung stehen.

    # Erstellen der Tabelle mit n+1 Zeilen (von 0 bis n), k+1 Spalten
    # Komplett mit Nullen gefüllt
    result = []
    for i in range(0,n+1): # Für jede Zeile leere Liste anfügen
        result.append([])
        for j in range(0,k+1): # Für jede Spalte eine 0 anfügen
            result[i].append(0)

    # Basisfälle:
    # Fall binom(0, k) = 0 bereits abgearbeitet (gesamte Tabelle mit 0 initialisiert)
    for i in range(0,n+1): # Schleife über alle n-Werte
        result[i][0] = 1 # binom(n, 0) = 1

    # Berechnen der restlichen Tabelle
    for i in range(1,n+1): # Schleife über alle n-Werte (außer n=0 da Basisfall)
        for j in range(1,k+1): # Schleife über alle k-Werte (außer k=0 da Basisfall)
            result[i][j] = result[i-1][j] + result[i-1][j-1] # binom(n, k) = binom(n-1, k) + binom(n-1, k-1)

    return result

## Hier ist ein Testfall:
n = 5
k = 3

#n = int(input("n = "))
#k = int(input("k = "))

result = dynCompNChooseK(n, k)
resultTable = dynCompNChooseKTable(n, k)

print('berechnet:')
print(result) ## 10
print('mit der Tabelle:')
print(resultTable)
##  #k
##[ #0  1  2  3  4  5
##  [1, 0, 0, 0, 0, 0], #n=0
##  [1, 1, 0, 0, 0, 0], #n=1
##  [1, 2, 1, 0, 0, 0], #n=2
##  [1, 3, 3, 1, 0, 0], #n=3
##  [1, 4, 6, 4, 1, 0], #n=4
##  [1, 5, 10,10,5, 1]  #n=5
##[
