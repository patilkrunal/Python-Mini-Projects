import re

file = open("C://Users//krunal//Desktop//contact script//contact3.vcf", 'r')
contacts = []
phone = []
# print(file.read())

# BEGIN:VCARD
# VERSION:3.0
# N:;Varsha;;;
# FN:Varsha
# TEL;TYPE=CELL:963-716-2477    or     TEL;CELL:97 63 982037
# TEL;TYPE=WORK:976-204-7573
# EMAIL;TYPE=PREF;TYPE=HOME:varshapatil3761@gmail.com
# PHOTO;ENCODING=B;TYPE=JPEG:/9j/4AAQSk...
# END:VCARD

for line in file:
    # print(line)
    name = re.findall('FN:(.*)', line)
    nm = ''.join(name)

    if len(nm) == 0:
        data = {'name': ""}
        continue

    for lin in file:
        # tel = re.findall('TEL;(CELL|TYPE=CELL|TYPE=CELL;TYPE=PREF):(.*)', line)
        tel = re.findall('TEL;(CELL|TYPE=CELL;TYPE=PREF):(.*)', lin)

        if (len(tel) == 0):
            data = {'phone': ""}
            continue
        # print(tel[0][-1])
        tel = ''.join(tel[0][-1])

        tel = tel.strip()
        tel = ''.join(e for e in tel if e.isalnum())
        data = {'name' : nm, 'phone': tel}
        break;
    
    if(data['phone']!="" and data['name']!=""):
        contacts.append(data)

for contact in contacts:
    print(contact['name'], contact['phone'])
