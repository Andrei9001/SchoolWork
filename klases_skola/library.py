from PIL import Image

from tkinter import filedialog as fd
from tkinter import ttk

class Photo:
    # bilžu apstrāde
    def __init__(self,datne):
        self.datne = datne
    def bilde(self):
        with Image.open(self.datne) as im:
            print(self.datne, im.format, f"{im.size}x{im.mode}")
            a=(100,200,300,400,50,10)
            izmers = (a[2],a[2])
            im.thumbnail(izmers)
            map = fd.asksaveasfile(defaultextension='.jpg' ,filetypes=[('jpg','*.jpg')])
            im.save(map.name, im.format)
            im.show()
    def rotate(self):
        with Image.open(self.datne) as im:
            map = fd.asksaveasfile(defaultextension='.jpg' ,filetypes=[('jpg','*.jpg')])
            im.rotate(90,expand=True).save(map.name, im.format)
    
    def thumb(self):
        with Image.open(self.datne) as im:
            print(self.datne, im.format, f"{im.size}x{im.mode}")
            izmers = (self.a,self.b)
            im.thumbnail(izmers)
            map = fd.asksaveasfile(defaultextension='.jpg' ,filetypes=[('jpg','*.jpg')])
            im.save(map.name, im.format)
            im.show()
    #def rot(self):
        #with Image.open(self.datne) as im:


file = fd.askopenfilename(filetypes=[('jpg','*.jpg')])
pic = Photo(file)
pic.bilde()