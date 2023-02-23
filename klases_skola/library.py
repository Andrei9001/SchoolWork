from PIL import Image
from tkinter import messagebox as tkms
from tkinter import filedialog as fd


class Photo:
    # bilžu apstrāde
    def __init__(self,datne):
        self.datne = datne
    def bilde(self):
        with Image.open(self.datne) as im:
            tkms.showinfo(message='Lūdzu izvēlieties jaunā attēla saglabāšanas datni')
            map = fd.asksaveasfile(defaultextension='.jpg' ,filetypes=[('jpg','*.jpg')])
            print(self.datne, im.format, f"{im.size}x{im.mode}")
            izmers = (100,100)
            im.thumbnail(izmers)
            im.save(map.name, im.format)
            im.show()

    def rotate(self):
        with Image.open(self.datne) as im:
            tkms.showinfo(message='Lūdzu izvēlieties jaunā attēla saglabāšanas datni')
            map = fd.asksaveasfile(defaultextension='.jpg' ,filetypes=[('jpg','*.jpg')])
            im.rotate(90,expand=True).save(map.name, im.format)
    
    def thumb(self):
        with Image.open(self.datne) as im:
            print(self.datne, im.format, f"{im.size}x{im.mode}")
            tkms.showinfo(message='Lūdzu izvēlieties jaunā attēla saglabāšanas datni')
            map = fd.asksaveasfile(defaultextension='.jpg' ,filetypes=[('jpg','*.jpg')])
            tkms.showinfo(message='Lūdzu apskatiet konsoli')
            px = int(input('Vēlamais attēla kvadrāta izmērs pikseļos (px): '))
            izmers = (px,px)
            im.thumbnail(izmers)
            im.save(map.name, im.format)
            im.show()
    #def rot(self):
        #with Image.open(self.datne) as im:

#==============variables=========================
options = ['Attēla izmērs 100x100px','Attēla pagriešana par 90 grādiem','Attēla izveide ar pašizvēlētu izmēru']


tkms.showinfo(message='Lūdzu izvēlieties attēlu')
file = fd.askopenfilename(filetypes=[('jpg','*.jpg')])
pic = Photo(file)

pic.bilde()
pic.rotate()
pic.thumb()
tkms.showerror(message='Kļūda! Visdrīzāk no nepareizi ievadītas izvēles')
    
