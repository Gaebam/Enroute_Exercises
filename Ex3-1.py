# Exercise 3.1
# Given the following vowels 'a', 'e', 'i', 'o', 'u'
# Couent each vowel inside the text file
# **OUTPUT:
# Vowel name    Count
# **Sum of all the vowels in parg 1
# **Sum of all the vowels in parg 2
# **Sum of vowels in paragraph 1 and 2
# **Print the results of the union between both paragraphs.
# **Print the results of the intersection between both parag.
# **Print the results of the diference between both parag.
vowels = ["a", "e", "i", "o", "u"]
txt1= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec placerat lacus sed lacinia suscipit. Pellentesque pulvinar tempus dui, non facilisis dolor vestibulum et. Suspendisse potenti. Duis in molestie orci, feugiat eleifend nisi. Aliquam consequat tortor id nisl interdum mattis. In hac habitasse platea dictumst. Suspendisse aliquam tincidunt velit. Phasellus pretium fermentum leo id rutrum. Fusce suscipit augue sit amet pulvinar vulputate. Proin pretium mauris vitae purus efficitur auctor. Vestibulum est lorem, varius a tempus non, consequat vel risus. Nam laoreet velit sit amet ipsum tincidunt luctus. Nunc gravida tortor a leo efficitur, et maximus enim pharetra."
txt2= "Mauris tincidunt commodo lorem a pellentesque. Nam rutrum luctus neque. Maecenas porttitor dolor in sollicitudin ultrices. Aliquam eget blandit massa. Sed bibendum suscipit finibus. Suspendisse potenti. Nullam nec luctus diam, at bibendum dui. Ut vestibulum venenatis finibus. Mauris sed turpis at ante facilisis rhoncus. Phasellus molestie pharetra sagittis. Ut tincidunt, turpis sodales dapibus commodo, quam nisi mollis quam, at maximus quam tortor vitae nibh. Phasellus posuere aliquam erat sed elementum. Pellentesque faucibus, nulla eget hendrerit venenatis, tellus enim posuere dui, eu iaculis nibh ipsum a ligula. Quisque scelerisque odio sit amet libero iaculis rutrum. In hac habitasse platea dictumst."
z, y = 0, 0
counts = {i:0 for i in 'aeiouAEIOU'}


for char in txt1:
	if char in counts:
		counts[char] += 1
print('\nCount each vowel inside the text file\n\nTXT 1')	
print('Vowel Name\tCount')
for k, v in counts.items():
	y = y + v
	print k,'\t\t',v

counts2 = {i:0 for i in 'aeiouAEIOU'}
for char in txt2:
	if char in counts2:
		counts2[char] += 1
print('\nTXT 2\nVowel Name\tCount')
for k, v in counts2.items():
	z = z + v
	print k,'\t\t',v

print "\n\nSum of all the vowels in paragraph 1:", y
print '\nSum of all the vowels in paragraph 2:', z
print '\nSum of all the vowels in both paragraphs:', (z+y)

st1 = set(txt1.split())
st2 = set(txt2.split())

uni = st1.union(st2)
inter = st1.intersection(st2)
dif = st1.difference(st2)

print '\nUnion\n', uni, '\n'
print '\nIntersection\n', inter, '\n'
print '\nDifference\n', dif, '\n'
