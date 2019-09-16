import re

query_strings = ["foo", "foster", "folder", "fog",          # fo
                 "bar", "baby", "basket", "backend",        # ba
                 "going", "gone", "goal", "gorgeous"        # go
                 "self", "selfish", "selling", "sellout",   # se
                 "drop", "dropping", "drowning", "drone"]   # dr

s = input()  # query string
query_strings = '\n'.join(query_strings)  # transform list to one entry per line
regex = r"^[" + re.escape(s) + r"]\w+\ *\w+"  # pattern: ^[s]\w+\ *\w+ where "s" is the variable

print(re.findall(regex, query_strings, re.MULTILINE))
