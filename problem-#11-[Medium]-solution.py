import re

query_strings = ["foo", "bar", "laina", "lainar",
                 "baby", "basket", "basi pedala",
                 "fookin hell", "baby shit", "govno",
                 "semen", "selqnin", "selqndur", "selqk",
                 "kur", "kurva", "kurvolqk", "kurvetina"]

s = input()  # query string
query_strings = '\n'.join(query_strings)  # transform list to one entry per line
regex = r"^[" + re.escape(s) + r"]\w+\ *\w+"  # pattern: ^[s]\w+\ *\w+ where "s" is the variable

print(re.findall(regex, query_strings, re.MULTILINE))
