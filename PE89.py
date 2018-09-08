class RomanNumeral:
    def __init__(self, roman_numeral=''):
        self.roman_numeral = roman_numeral.upper()
        self.value = 0  # arabic value
        self.simple_form = ''  # Least possible number of character equivalence of Roman numeral
        self.valid = False  # Is the Roman numeral valid
        self.arabs = []  # List of corresponding arabic numbers

        self.convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.reverse_convert = dict((v, k) for k, v in self.convert.items())
        self.reverse_convert.update({4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'})

        self.convert_arabs()
        self.convert_value()
        self.convert_simple()

    def __repr__(self):
        return self.roman_numeral

    def __str__(self):
        return f'{self.roman_numeral} : {self.value}'

    def convert_arabs(self):
        """
        Converts the roman numeral to a list of the corresponding arabic numbers for each roman numeral
        """
        self.arabs = []
        for i, num in enumerate(self.roman_numeral):
            if num == 'I' and i != len(self.roman_numeral) - 1:
                if self.roman_numeral[i+1] == 'V':
                    self.arabs.append(4)
                    continue
                elif self.roman_numeral[i+1] == 'X':
                    self.arabs.append(9)
                    continue

            if num == 'X' and i != len(self.roman_numeral) - 1:
                if self.roman_numeral[i+1] == 'L':
                    self.arabs.append(40)
                    continue
                elif self.roman_numeral[i+1] == 'C':
                    self.arabs.append(90)
                    continue

            if num == 'C' and i != len(self.roman_numeral) - 1:
                if self.roman_numeral[i+1] == 'D':
                    self.arabs.append(400)
                    continue
                elif self.roman_numeral[i+1] == 'M':
                    self.arabs.append(900)
                    continue

            if num == 'V' and i != 0 and self.roman_numeral[i-1] == 'I':
                continue

            if num == 'X' and i != 0 and self.roman_numeral[i-1] == 'I':
                continue

            if num == 'L' and i != 0 and self.roman_numeral[i-1] == 'X':
                continue

            if num == 'C' and i != 0 and self.roman_numeral[i-1] == 'X':
                continue

            if num == 'D' and i != 0 and self.roman_numeral[i-1] == 'C':
                continue

            if num == 'M' and i != 0 and self.roman_numeral[i-1] == 'C':
                continue

            self.arabs.append(self.convert[num])

    def is_valid(self):
        """
        Checks if the Roman Numeral is valid
        """
        desc_sort = self.arabs == sorted(self.arabs)[::-1]  # Numerals must be in descending order

        small_exceed = True  # Cannot have number of smaller values exceed X, C, or M
        if self.roman_numeral.count('I') > 9:
            small_exceed = False
        if self.roman_numeral.count('X') > 9:
            small_exceed = False
        if self.roman_numeral.count('C') > 9:
            small_exceed = False

        five_once = True  # Cannot have more than one V, L, D
        if self.roman_numeral.count('V') > 1:
            five_once = False
        if self.roman_numeral.count('L') > 1:
            five_once = False
        if self.roman_numeral.count('D') > 1:
            five_once = False

        return desc_sort and small_exceed and five_once

    def convert_value(self):
        """
        Convert the value of the roman numeral to the arabic number
        """
        self.value = sum(self.arabs)

    def convert_simple(self):
        """
        Converts the roman numeral to its simplest form, meaning the least number of characters
        """
        subtract_list = sorted(self.reverse_convert.keys())[::-1]
        simplel = []
        curr_val = self.value
        i = 0
        while curr_val > 0:
            if curr_val - subtract_list[i] >= 0:
                simplel.append(subtract_list[i])
                curr_val -= subtract_list[i]
            else:
                i = (i + 1) % len(subtract_list)  # Go back to beginning

        self.simple_form = ''.join(self.reverse_convert[i] for i in simplel)  # make into simplest form

romans = [RomanNumeral(s.strip()) for s in open("p089_roman.txt").readlines()]

saved = 0
for r in romans:
    diff = len(r.roman_numeral) - len(r.simple_form)
    if diff < 0:
        print('what ', r)
    saved += diff

print(saved)