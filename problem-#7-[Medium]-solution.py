import string
letters = string.ascii_lowercase
values = iter(range(1, 27))

mapping = {}

for letter in letters:
    mapping[letter] = next(values)



