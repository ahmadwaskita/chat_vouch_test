import re
# from datetime import datetime
from time import localtime, mktime, gmtime, strftime, strptime
from datetime import timedelta, datetime


text = 'background: url("http://files.vouch.sg/5c0899a0f82bb561b4eff07a/1548226015327.jpeg") center center / contain no-repeat; opacity: 0; display: none;'
text2 = 'display: block; opacity: 1'
text3 = 'display: none; opacity: 1'

try:
    import ntplib

    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    t1 = strftime('%a, %d %b %H:%M:%S', localtime(response.tx_time))
except:
    print('Could not sync with time server.')

a = re.findall('"(.+?)"',text)
b = re.findall('display:\s.+[^;]', text)
# c = re.search(r'(?:"(.+?)")', text)
# d = re.search(r'(?:display:\s.+[^;])', text)
# e = re.sub(r'.+display:\s','', text)

print(a[0])
print(b)
# print(datetime.now().strftime('%a, %d %b %H:%M:%S'))
t = localtime()
print(strftime('%a, %d %b %H:%M:%S', localtime())[:-10])
# print(str(c.group(0)))
# print(d.group(0))
# print(e)
print(text2[9:-12])
print(text3[9:-12])
print(t1[12:])
t2 = '09:50:30'
FMT = '%H:%M:%S'
tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1[12:], FMT)

print(timedelta.total_seconds(tdelta))

