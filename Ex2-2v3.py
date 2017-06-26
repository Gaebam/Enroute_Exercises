'''
Exercise 2.2
a=1, e=2, i=3, o=4, u=5
x = "Tesla"
y = "Buick"
z = "Ferrari"
w = "Ford"
t = "Lamborghini"
y = "Masertati"
Iterate over all the cars, create an array for each car => print(car_vowels_array)
Each array will hold the vowel value
At the construct an array containing all the cars vowel.
With the previous array filter the vowel value like this:
vowel_value %2 == 0: 'Buy it'
vowel_value %3 == 0: 'Sell it'
'''
vowels = ["a", "e", "i", "o", "u"]
v_value = [1, 2, 3, 4, 5]
cars = ["Tesla", "Buick", "Ferrari", "Ford", "Lamborghini", "Masertati"]
o0, o1, o2, o3, o4, o5= [], [], [], [], [], []

for u in range(len(cars)):
	for x in cars[u]:
		for z in vowels:
			if x == z:
				globals()["o"+str(u)].append(v_value[vowels.index(x)])
	print(cars[u], globals()["o"+str(u)])


