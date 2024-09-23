
import os
import random
import tkinter as tk
from PIL import Image, ImageTk

file="meyveler"
soru_path="soru_isareti.png"
def load_images():
    images = []
    pictures = [f"foto {i}.png" for i in range(16)]
    for foto in pictures:
        path=os.path.join(file,foto)
        img=Image.open(path)
        img.thumbnail((80, 80))
        images.append(ImageTk.PhotoImage(img))
    return images

pencere=tk.Tk()
def dagitma(kartlar):
    for i in range(len(kartlar)):
        for j in range(len(kartlar[0])):
            randX=random.randint(0,satir-1)
            randY=random.randint(0,sutun-1)
            kartlar[i][j],kartlar[randX][randY]=kartlar[randX][randY],kartlar[i][j]

def buton_click(i,j):

    global ilk_buton,ikinci_buton,ilk_deger,ikinci_deger,sayac,cift,deneme,takimlar,takim
    if not ilk_deger:
        ilk_deger=kartlar[i][j]
        ilk_buton=butonlar[i][j]
        ilk_buton.config(image=ilk_deger,state="disabled",bg="purple")
    elif not ikinci_deger:
        ikinci_deger=kartlar[i][j]
        ikinci_buton=butonlar[i][j]
        ikinci_buton.config(image=ikinci_deger,state="disabled",bg="purple")

        if images.index(ilk_deger)//2 == images.index(ikinci_deger)//2:
            ilk_buton = ikinci_buton = ilk_deger = ikinci_deger = None
            takimlar[takim]+=1
            sayac+=1
        else:
            pencere.after(1000,kapama)
            takim=(takim+1)%2
        deneme += 1
        update_labels()


def update_labels():
    label_kirmizi.config(text=f"Kirmizi: {takimlar[1]}")
    label_mavi.config(text=f"Mavi: {takimlar[0]}")
    label_deneme.config(text=f"Deneme {deneme//2}")
    if sayac == cift:
        if takimlar[0] > takimlar[1]:
            label.config(text="Mavi Kazandi", fg='blue')
        elif takimlar[0] == takimlar[1]:
            label.config(text="Berabere", fg='black')
        else:
            label.config(text="Kirmizi Kazandi", fg='red')
    else:
        label.config(text=f"Sıra: {'Mavi' if takim == 0 else 'Kırmızı'}", fg='blue' if takim == 0 else 'red')

def kapama():
    global ilk_buton, ikinci_buton, ilk_deger, ikinci_deger
    ilk_buton.config(image=soru_, state="normal",fg="black",bg="white")
    ikinci_buton.config(image=soru_, state="normal",fg="black",bg="white")
    ilk_buton =ikinci_buton= ilk_deger= ikinci_deger=None

images = load_images()
kartlar=[]
for i in range(4):
    satir=images[i*4:(i+1)*4]
    kartlar.append(satir)
cift=8
satir=4
sutun=4
takimlar=[0,0]
takim=0
deneme=0

label_mavi=tk.Label(pencere,text="Mavi: 0",fg="blue",font=40)
label_mavi.grid(row=0, column=0)

label_kirmizi=tk.Label(pencere,text="Kirmizi: 0",fg="red",font=40)
label_kirmizi.grid(row=0, column=3)

label_deneme=tk.Label(pencere,text="Deneme: 0",font=40)
label_deneme.grid(row=0, column=1, columnspan=2)

label=tk.Label(pencere, text="Sıra: Mavi", font=40, fg="blue")
label.grid(row=1, column=1, columnspan=2)


pencere.resizable(False,False)
butonlar=[[None for _ in range(satir)] for _ in range(sutun)]
dagitma(kartlar)

soru_isareti = Image.open(soru_path)
soru_isareti.thumbnail((80, 80))
soru_=ImageTk.PhotoImage(soru_isareti)

for i in range(satir):
    for j in range(sutun):
        buton=tk.Button(pencere,image=soru_,width=80,height=80,font=40,command=lambda a=i,b=j:buton_click(a,b))
        buton.grid(row=i+2,column=j)
        butonlar[i][j]=buton

ilk_buton = ikinci_buton = ilk_deger = ikinci_deger = None
sayac=0

pencere.mainloop()





