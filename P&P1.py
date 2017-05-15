# Algorithmen und Datenstrukturen
# Hausaufgabe 1 - Matrixmultiplikation
# Abgabedatum: 21.5.2017
#
# Gruppennummer: 55
# Gruppenmitglieder: 
# - Eike Olaf Pubantz
# - Max Wiedenhöft
# - Jan Heuer

# Diese Funktion können Sie verwenden, um Matrizen auszugeben.
def printMatrix(m):
    for line in m:
        print('|', end='')
        i = 0
        for value in line:
            if (i > 0):
                print(' ', end='')
            print(value, end='')
            i = i + 1
        print("|")

# Implementieren Sie ab hier Ihre Lösungen:
def matMultDef(a, b):
    print('Parameter a:')
    printMatrix(a)
    print('Parameter b:')
    printMatrix(b)
    # hier soll Ihre Implementierung der Matrixmultiplikation laut Definition stehen.
    result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result

def matMultDC(a, b):
    print('Parameter a:')
    printMatrix(a)
    print('Parameter b:')
    printMatrix(b)
    # hier soll Ihre Implementierung der Matrixmultiplikation nach dem Paradigma "Teile und Herrsche"
    result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result

# Hier ist ein Testfall:
result = matMultDef(
[ # a
[3, 2, 1],
[1, 0, 2]
],
[ # b
[1, 2],
[0, 1],
[4, 0]]
)

print('berechnet:')
printMatrix(result)

# Das Ergebnis sollte folgende Matrix sein:
# [
# [7, 8],
# [9, 2]
# ]
