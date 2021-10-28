from columnar import columnar

table_data = []
table_header = ['Seitenlänge a in cm', 'Seitenlänge b in cm', 'Mittelwert (a,b) in cm']

def print_senctence(data):
    print('\n' * 1)
    print(data)
    print('\n' * 1)

def calc_num_before_after():
    for i in range(0, root):
        i1 = i + 1
        if (i1 * i1) > root:
            return (i, i1)

def steps(number, total, root, before):
    number = number + 1;

    # Berechne Seitenlänge b in cm 
    bValue = root / before

    # Berechne den Mittelwert (a,b) in cm
    average = (bValue + before) / 2

    table_data.append([str(number), str(bValue), str(average)])

    if (total <= number):
        print(columnar(table_data, headers=table_header, no_borders=False))
        print_senctence(f'Der Näherungswert für die Wurzel aus 17 beträgt {average}')

    else:
        steps(number, total, root, average)
        

def calc_num_root(left, root, before):
    steps(0, 10, root, before + 0.1)






root = 17
(before, after) = calc_num_before_after()

print_senctence(f'Die Wurzel aus {root} liegt zwischen {before} und {after}.')

calc_num_root(10, root, before)