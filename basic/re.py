import re



text = "barbar harhar carhel"

print(re.findall(r'(\w{3})(\1)', text))