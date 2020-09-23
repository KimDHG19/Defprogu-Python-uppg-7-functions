import random
from math import pi

numbers = [1, 2, 3, 11, 5, 6, 7, 8]


def maximum():
	print(max(numbers))


maximum()


def kvadrat():
	length = int(input('Skriv in talet du vill räkna kvadratroten på '))

	kvadrat = length * length

	print(f'kvadratroten av {length} är {kvadrat}')


kvadrat()


def radius():
	area = float(input('Ange cirkelns area '))
	r = area / pi
	print(f'en cirkel vars area är {area} areaenheter har en radie på {r} längdenheter')


radius()

# 4a och b

string = "Vi gillar att koda python också på fritiden , och har lärt oss mycket på defprogu lektionerna :)"


def defprogurandom_py():
	length_of_string = len(string)

	character_index = random.randint(0, length_of_string)

	character = string[character_index]

	print(f'Den slumpmässiga karaktärens index är {character_index} och karaktären är {character} ')


defprogurandom_py()

# 4b
string = input('skriv en teckensträng som är minst 48 tecken lång')

defprogurandom_py()


def lotto():
	def vikinglotto():
		global row
		global extra_nums
		extra_nums = []
		row = []
		i = 0

		while i < 7:
			i += 1
			row.append(random.randint(1, 60))

		i = 0
		while i < 2:
			i += 1
			extra_nums.append(random.randint(1, 10))

		print(f'Din slumpmässiga rad är: {row} och dina tillägsnummer är: {extra_nums}')

	row_amount = int(input('Hur många VikingLotto rader? '))
	i = 0

	while i < row_amount:
		i += 1
		vikinglotto()


lotto()

def lottoFiles():
	def vikinglottoFiles():
		global row
		global extra_nums
		extra_nums = []
		row = []
		i = 0

		while i < 7:
			i += 1
			row.append(random.randint(1, 60))

		i = 0
		while i < 2:
			i += 1
			extra_nums.append(random.randint(1, 10))

		print(f'Din slumpmässiga rad är: {row} och dina tillägsnummer är: {extra_nums}')

		with open("VikingLotto.txt", "a+") as f:
			f.write('rad: ')
			for element in row:
				f.write(str(element) + ', ')
			f.write('\n')

	row_amount = int(input('Hur många VikingLotto rader? '))
	i = 0

	while i < row_amount:
		i += 1
		vikinglottoFiles()


lottoFiles()
