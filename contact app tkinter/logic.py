from tkinter import *
from tkinter import filedialog

# Update data from vcf file to tkinter interface
contacts = []
phone = []

class Logic(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        file = filedialog.askopenfile(initialdir="/", title="Select file", filetypes=(("VCF files", "*.vcf"), ("all files", "*.*")))

        for line in file:
            name = re.findall('FN:(.*)', line)
            nm = ''.join(name)

            if len(nm) == 0:
                data = {'name': ""}
                continue

            for lin in file:
                tel = re.findall('TEL;(CELL|TYPE=CELL;TYPE=PREF):(.*)', lin)

                if (len(tel) == 0):
                    data = {'phone': ""}
                    continue

                tel = ''.join(tel[0][-1])
                tel = tel.strip()
                tel = ''.join(e for e in tel if e.isalnum())
                data = {'name' : nm, 'phone': tel}
                break;

        if(data['phone']!="" and data['name']!=""):
            contacts.append(data)

        count = 0
        for contact in contacts:
            try:
                if (contact['phone'] == ""):
                    continue
                self.listbox.insert(count, str(str(count+1) + ". " + contact['name'] + " : " + contact['phone']))
                count += 1
            except EXCEPTION as e:
                print(str(e))