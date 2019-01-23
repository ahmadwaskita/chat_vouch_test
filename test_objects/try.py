import re

text = 'background: url("http://files.vouch.sg/5c0899a0f82bb561b4eff07a/1548226015327.jpeg") center center / contain no-repeat; opacity: 0; display: none;'

a = re.findall('"(.+?)"',text)
b = re.findall('display:\s.+[^;]', text)
# c = re.search(r'(?:"(.+?)")', text)
# d = re.search(r'(?:display:\s.+[^;])', text)
# e = re.sub(r'.+display:\s','', text)

print(a[0])
print(b)
# print(str(c.group(0)))
# print(d.group(0))
# print(e)