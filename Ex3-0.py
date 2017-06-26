from tabulate import tabulate
beers = [{'name': 'Modelo Especial', 'price': 25.00, 'ap': 4.0},
		 {'name': 'Indio', 'price': 20.00, 'ap': 4.2},
		 {'name': 'Tecate Light', 'price': 30.00, 'ap': 3.5},
		 {'name': 'Minerva', 'price': 35.00, 'ap': 8.0},
		 {'name': 'Budlight', 'price': 18.00, 'ap': 5.0}]


print ('\nName\tPrice\tPorcentaje de Alcohol (5%)').expandtabs(24)

for elem in beers:
	if len(elem['name']) < 7:
		print elem['name'], '\t\t\t', elem['price'], '\t\t\t', elem['ap']
	elif len(elem['name']) >= 7 and len(elem['name']) <15:
		print elem['name'], '\t\t', elem['price'], '\t\t\t', elem['ap']
	else:
		print elem['name'], '\t', elem['price'], '\t\t\t', elem['ap']

beers.append({'name':'Ultra','price':40.00,'ap':5.00})

print ('\nName\tPrice\tPorcentaje de Alcohol (5%)').expandtabs(24)

for elem in beers:
	if len(elem['name']) < 7:
		print elem['name'], '\t\t\t', elem['price'], '\t\t\t', elem['ap']
	elif len(elem['name']) >= 7 and len(elem['name']) <15:
		print elem['name'], '\t\t', elem['price'], '\t\t\t', elem['ap']
	else:
		print elem['name'], '\t', elem['price'], '\t\t\t', elem['ap']