from tkinter import *
from tkinter import filedialog
import datetime

from logic import Logic
# from addpeople import AddPeople
from aboutus import AboutUs

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self, master):
        self.master = master

        # FRAMES
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        # TOP FRAME DESIGN
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="My Phonebook App", font="arial 15 bold", bg="white", fg="#42bcf5")
        self.heading.place(x=230, y=50)

        self.date_lbl = Label(self.top, text="Date: " + date, font='arial 12 bold', fg='#42bcf5', bg='white')
        self.date_lbl.place(x=450, y=110)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.listbox = Listbox(self.bottom, width=50, height=24)
        self.listbox.grid(row=0, column=0, padx=(10, 0), pady=(10,10))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N + S)

        # BUTTON 1 - UPLOAD PEOPLE
        self.uploadButton = Button(self.bottom, text=" Upload VCF file", fg="#42bcf5", bg="white", font='arial 12 bold', command=self.uploadVCF)
        self.uploadButton.place(x=400, y=20)

        # # BUTTON 2 - ADD PEOPLE
        # self.addButton = Button(self.bottom, text="Add People", fg="#42bcf5", bg="white", font='arial 12 bold', command=self.addVCFfile)
        # self.addButton.place(x=250, y=130)

        # # BUTTON 3 - ABOUT US
        # self.aboutButton = Button(self.bottom, text="  About us   ", fg="#42bcf5", bg="white", font='arial 12 bold', command=self.aboutUs)
        # self.aboutButton.place(x=250, y=190)

    def uploadVCF(self):
        # contact = Logic()
        # Update data from vcf file to tkinter interface
        contacts = []
        data = {}
        file = filedialog.askopenfile(initialdir="C://Users//krunal//Desktop//contact script", title="Select file", filetypes=(("VCF files", "*.vcf"), ("all files", "*.*")))

        for line in file:
            # print(line)
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
                # print(tel[0][-1])
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

    def add_people(self):
        file = filedialog.askopenfile(initialdir="C://Users//krunal//Desktop//contact script", title="Select file", filetypes=(("VCF files", "*.vcf"), ("all files", "*.*")))

    # def aboutUs(self):
    #     aboutpage = AboutUs()

def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x558+350+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()