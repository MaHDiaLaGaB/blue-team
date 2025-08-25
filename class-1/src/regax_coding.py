import re

# re.findall()
# re.compile()
# re.split()
# re.sub()
# re.search()


string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

regex = r'\d+'
match = re.findall(pattern=regex, string=string)
# print(match)

p = re.compile(r'\d')
p_more = re.compile(r'\d+')
p_word = re.compile(r'\w')
p_word_plus = re.compile(r'\w+')
p_word_big = re.compile(r'\W')
p_start = re.compile(r'ab+')
p_small = re.compile(r'[a-f]+')
find = p_small.split('Obn 12th JAn 2016, at 11e:02 AM')
# print(find)

# print(re.sub('Ub', '~*', 'Subject has Uber booked already'))

# print(re.sub(r'\sAND\s', ' & ', 'Baked Beans and Spam', flags=re.IGNORECASE))

# print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))
pattern = r"091\d{8}"
string = """Hello my Number is  and
            my friend's number is 0914045656"""
match = re.findall(pattern=pattern, string=string)
print(match)


