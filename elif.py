from tabulate import tabulate


arturo = [90, 100, 50, 70]
artemio = [70, 65, 100, 80]
juan = [90, 90, 100, 70]
rene = [50, 60, 70, 80]
pedro = [100, 50, 100, 90]

#Ex. Print the avg score of each student

arturo1 = sum(arturo)/float(len(arturo))
artemio1 = sum(artemio)/float(len(artemio))
juan1 = sum(juan)/float(len(juan))
rene1 = sum(rene)/float(len(rene))
pedro1 = sum(pedro)/float(len(pedro))

mx = arturo1
if artemio1 > mx: mx = artemio1
if juan1 > mx: mx = juan1
if rene1 > mx: mx = rene1
if pedro1 > mx: mx = pedro1

lx = arturo1
if artemio1 < lx: lx = artemio1
if juan1 < lx: lx = juan1
if rene1 < lx: lx = rene1
if pedro1 < lx: lx = pedro1


if arturo1 >= 95: arturo2 = "Excentado"
elif arturo1 < 95 and arturo1 >= 85: arturo2 = "Aprobado"
elif arturo1 < 85 and arturo1 >= 70: arturo2 = "Promedio"
elif arturo1 < 70: arturo2 = "Reprobado"

if artemio1 >= 95: artemio2 = "Excentado"
elif artemio1 < 95 and artemio1 >= 85: artemio2 = "Aprobado"
elif artemio1 < 85 and artemio1 >= 70: artemio2 = "Promedio"
elif artemio1 < 70: artemio2 = "Reprobado"

if juan1 >= 95: juan2 = "Excentado"
elif juan1 < 95 and juan1 >= 85: juan2 = "Aprobado"
elif juan1 < 85 and juan1 >= 70: juan2 = "Promedio"
elif juan1 < 70: juan2 = "Reprobado"

if rene1 >= 95: rene2 = "Excentado"
elif rene1 < 95 and rene1 >= 85: rene2 = "Aprobado"
elif rene1 < 85 and rene1 >= 70: rene2 = "Promedio"
elif rene1 < 70: rene2 = "Reprobado"

if pedro1 >= 95: pedro2 = "Excentado"
elif pedro1 < 95 and pedro1 >= 85: pedro2 = "Aprobado"
elif pedro1 < 85 and pedro1 >= 70: pedro2 = "Promedio"
elif pedro1 < 70: pedro2 = "Reprobado"

tabla = [['Arturo', arturo1, arturo2, mx, lx],
		 ['Artemio', artemio1, artemio2],
		 ['Juan', juan1, juan2],
		 ['Rene', rene1, rene2],
		 ['Pedro', pedro1, pedro2]]

print(tabulate(tabla, headers=['Name','Score','Message', 'Highscore', 'Low score']))


