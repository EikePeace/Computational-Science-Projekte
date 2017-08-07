#!/usr/bin/python3
## Algorithmen und Datenstrukturen
## Hausaufgabe 4 - Dijkstra - Kruskal
## Abgabedatum: 13.8.2017
##
## Gruppennummer: <Bitte eintragen>
## Gruppenmitglieder:
## - <Bitte eintragen>
## - <Bitte eintragen>
## - <Bitte eintragen>

## ACHTUNG: Verwenden Sie fuer Ihre Kommentare nur ein einzelnes #-Zeichen:
# so sollte Ihr Kommentar markiert werden
## so sind die Kommentare aus der Aufgabenstellung markiert.

## Implementieren Sie ab hier Ihre Loesungen:
def dijkstra(g, s):
    ## hier soll Ihre Implementierung stehen.
    result = [
        [4,1],
        [4,1,2],
        [4,3],
        [4],
        [4,5],
        [4,5,6],
        [4,5,7],] ## die Loesung fuer das Aufrufbeispiel unten. Durch das Ergebnis Ihrer Implementierung ersetzen.
    return result

def kruskal(g):
    ## hier soll Ihre Implementierung stehen.
    result = [
        [0,0, 0,0,0, 8 ],
        [0,0, 5,0,0, 16],
        [0,5, 0,7,0, 0 ],
        [0,0, 7,0,0, 0 ],
        [0,0, 0,0,0, 10],
        [8,16,0,0,10,0 ]
    ] ## Die Loesung fuer das Aufrufbeispiel unten. Durch das Ergebnis Ihrer Implementierung ersetzen.

    # Leere Ergebnismatrix
    result = []
    for i in range(len(g)):
        result.append([])
        for j in range(len(g)):
            result[i].append(0)

    list = []
    for i in range(len(g)):
        list.append([i])

    while len(list) != 1:
        # Suchen der minimalen Kante
        min = float('inf')
        for i in range(len(g)):
            for j in range(i, len(g)):
                if 0 < g[i][j] < min:
                    min = g[i][j]
                    a = i
                    b = j

        g[a][b] = 0 # Löschen der Kante

        # Finden der Knoten in list
        for i in range(len(list)):
            if a in list[i]:
                n = i
            if b in list[i]:
                m = i

        if n != m:
            for i in range(len(list[m])):
                list[n].append(list[m][i])
            del list[m]
            result[a][b] = min
            result[b][a] = min

    return result

def pathCosts(l, z, g): # l: liste von pfaden, z: zielknoten, g: graph
    ## hier soll Ihre Implementierung stehen.
    ## result = 7 ## die Loesung fuer das Aufrufbeispiel unten. Durch das Ergebnis Ihrer Implementierung ersetzen.
    result = 0
    a = l[z-1][0] - 1
    b = l[z-1][0] - 1
    for i in range(1, len(l[z-1])):
        a = b
        b = l[z-1][i] - 1
        result += g[a][b]
    return result

def spanTreeWeight(a):
    ## hier soll Ihre Implementierung stehen.
    ## result = 46 # die Loesung fuer das Aufrufbeispiel unten. Durch das Ergebnis Ihrer Implementierung ersetzen.
    result = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            result += a[i][j]
    return result

## Hier ist ein Testfall:
print('dijkstra test: von 4 zu 2')
graph = [
    [0,3,0,0, 0,0, 0],
    [1,0,0,0, 0,0, 0],
    [0,0,0,0, 0,0, 0],
    [4,9,5,0, 2,0, 0],
    [0,0,0,17,0,12,8],
    [0,0,0,0, 0,0, 0],
    [0,0,0,0, 0,0, 0]
]
dresult = dijkstra(graph, 4)

costs = pathCosts(dresult, 2, graph)
print('Kosten:')
print(costs) ## 7

print('kruskal test')
kresult = kruskal([
    [0,19,25,20,12,8],
    [19,0,5,0,0,16],
    [25,5,0,7,0,0],
    [20,0,7,0,0,30],
    [12,0,0,0,0,10],
    [8,16,0,30,10,0]
])
weight = spanTreeWeight(kresult)
print(weight)

## Dies soll die letzte Zeile in der Datei sein.
