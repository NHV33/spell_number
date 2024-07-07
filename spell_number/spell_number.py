import argparse
import math
import re

class SpellNumber:

	def __init__(self, number):
		self.spelling = self.spell_number(number)

	def __str__(self):
		return f"{self.spelling}"

	@staticmethod
	def initialize_spelling_hash():
		spelling_hash = {}

		ones_and_teens = "zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(",")
		two_digits = "twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".split(",")

		for i,spelling in enumerate(ones_and_teens):
			spelling_hash[i] = spelling

		for i,spelling in enumerate(two_digits):
			spelling_hash[(i+2)*10] = spelling

		return spelling_hash

	@staticmethod
	def digit_length(num):
		return math.ceil(math.log(num, 10)) if num != 0 else 1

	@staticmethod
	def get_digit_at(pos, num):
		return (num // (10 ** (pos - 1))) % 10

	@staticmethod
	def get_digit_range(high, low, num):
		total = 0
		for i,pos in enumerate(range(low, high + 1)):
			total += SpellNumber.get_digit_at(pos, num) * (10 ** (i))

		return total

	@staticmethod
	def spell_to_999(num_spelling, num):
		num_string = []
		ones_place = SpellNumber.get_digit_at(1, num)

		if num > 99:
			num_string.append(num_spelling[SpellNumber.get_digit_at(3, num)])
			num_string.append("hundred")
		if num > 9:
			tens_place = SpellNumber.get_digit_at(2, num)

			if tens_place == 1:
				num_string.append(num_spelling[(tens_place * 10) + ones_place])
			else:
				num_string.append(num_spelling[SpellNumber.get_digit_at(2, num) * 10])
				if ones_place != 0:
					num_string.append(num_spelling[SpellNumber.get_digit_at(1, num)])

		else:
			num_string.append(num_spelling[SpellNumber.get_digit_at(1, num)])

		return " ".join(num_string)

	@staticmethod
	def form_digit_groups(num):
		digit_len = SpellNumber.digit_length(num)
		remainder = digit_len - ((digit_len // 3) * 3)
		digit_groups = []

		if remainder:
			digit_groups.append(SpellNumber.get_digit_range(digit_len, digit_len - remainder + 1, num))

		for i in range(digit_len - remainder, 0, -3):
			digit_groups.append(SpellNumber.get_digit_range(i, i - 2, num))

		return digit_groups

	@staticmethod
	def generate_group_names():
		shortened = "m,b,tr,quadr,quint,sext,sept,oct,non,dec,undec,duodec,tredec,quattuordec,quindec,sexdec,septendec,octodec,novemdec,vigint,unvigint,duovigint,tresvigint,quattuorvigint,quinvigint,sesvigint,septenvigint,octovigint,novemvigint,trigint,untrigint,duotrigint,trestrigint,quattuortrigint,quintrigint,sestrigint,septentrigint,octotrigint,novemtrigint,quadragint,unquadragint,duoquadragint,tresquadragint,quattuorquadragint,quinquadragint,sesquadragint,septenquadragint,octoquadragint,novemquadragint,quinquagint,unquinquagint,duoquinquagint,tresquinquagint,quattuorquinquagint,quinquinquagint,sesquinquagint,septenquinquagint,octoquinquagint,novemquinquagint,sexagint,unsexagint,duosexagint,tresexagint,quattuorsexagint,quinsexagint,sessexagint,septensexagint,octosexagint,novemsexagint,septuagint,unseptuagint,duoseptuagint,treseptuagint,quattuorseptuagint,quinseptuagint,sesseptuagint,septenseptuagint,octoseptuagint,novemseptuagint,octogint,unoctogint,duooctogint,tresoctogint,quattuoroctogint,quinoctogint,sessoctogint,septenoctogint,octooctogint,novemoctogint,nonagint,unnonagint,duononagint,trenonagint,quattuornonagint,quinnonagint,sesnonagint,septennonagint,octononagint,novemnonagint,cent"
		return ["", "thousand"] + [name + "illion" for name in shortened.split(",")]

	@staticmethod
	def spell_number(num):
		num_string = []

		if num < 0:
			num_string.append("negative")
			num = abs(num)

		decimal_portion = None

		if type(num) == float:
			match = re.search(r"\.\d*", str(num))[0][1:]
			decimal_portion = [int(ch) for ch in match] if match else None

		num_spelling = SpellNumber.initialize_spelling_hash()

		group_names = SpellNumber.generate_group_names()

		digit_groups = SpellNumber.form_digit_groups(num)

		if len(digit_groups) > len(group_names):
			return None

		while len(digit_groups) > 0:
			current_group = digit_groups.pop(0)
			num_string.append(SpellNumber.spell_to_999(num_spelling, current_group))

			if group_names[len(digit_groups)]:
				num_string.append(group_names[len(digit_groups)])

		if decimal_portion:
			num_string.append("point")
			for dec_place in decimal_portion:
				num_string.append(num_spelling[dec_place])

		return " ".join(num_string)

def main():
    parser = argparse.ArgumentParser(description="Convert numbers to words")
    parser.add_argument('number', type=str, help='The number to convert')
    args = parser.parse_args()
    number = float(args.number) if '.' in args.number else int(args.number)
    spell_number_instance = SpellNumber(number)
    print(spell_number_instance)

if __name__ == "__main__":
    main()
