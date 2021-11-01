from decimal import *
from columnar import columnar



table_data = []
table_header = ['Nr.','Seitenlänge a in cm', 'Seitenlänge b in cm', 'Mittelwert (a,b) in cm']

def _line():
    print('-' * 96)

def _block():
    print('\n' * 2)

def _print(data):
    _block()
    print(data)
    _block()


def calc_interval(root):
    for i in range(0, root):
        i1 = i + 1
        if (i1 * i1) > root:
            return (i, i1)



def steps(number, total, root, before):
    number += 1

    # Berechne Seitenlänge b in cm 
    bValue = Decimal(root) / Decimal(before)

    # Berechne den Mittelwert (a,b) in cm
    average = (Decimal(bValue) + Decimal(before)) / Decimal(2)

    # Füge die Werte zur Tabelle hinzu.
    table_data.append([str(number), str(before), str(bValue), str(average)])

    # Falls die maximale Anzahl Durchläufe erreicht ist oder Zahlen sich doppeln, 
    # somit nicht genauer bestimmbar sind, gebe die Tabelle aus.  
    if (total <= number or before == bValue):
        _print(columnar(table_data, headers=table_header, no_borders=False))
        _print(f'Der Näherungswert für die Wurzel aus {root} beträgt {average}')

    # Falls nicht, gehe zum nächsten Durchlauf über.
    else:
        steps(number, total, root, average)
        

def calc_root(total, root, before):
    steps(0, total, root, before)




_line()

# Eingabefeld für die Zahl, die radiziert werden soll.
root = input('Gib eine Zahl ein, die radiziert werden soll: ')
root = int(root)

# Eingabefeld für die Anzahl der Durchläufe.
loop = input('Wieviele Durchläufe soll es maximal geben? ')
loop = int(loop)

_line()

(before, after) = calc_interval(root)

_print(f'Die Wurzel aus {root} liegt zwischen {before} und {after}.')

calc_root(loop, root, before)
