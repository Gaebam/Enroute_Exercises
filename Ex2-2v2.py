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
x1, x2 = [], []

for x in cars:
	for y in x:
		for z in vowels:
			if y == z:
				x1.append(y)

for x in x1:
	for i in range(len(v_value)):
		if x == vowels[i]:
			if v_value[i]%2 == 0: x2.append("Buy it")
			if v_value[i]%3 == 0: x2.append("Sell it")

print(x1)
print(x2)