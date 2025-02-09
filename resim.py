import tkinter as tk
from tkinter import filedialog
from tkinter import Canvas,PhotoImage,colorchooser
from PIL import Image,ImageTk,ImageDraw,ImageOps,ImageFont
def resim_yukle():
    dosya_yolu=filedialog.askopenfilename(filetypes=[("Resim Dosyaları","*.jpg;*.jpeg;*.png")])
    if dosya_yolu:
        global resim,duzenlenmis_resim,cizim
        resim=Image.open(dosya_yolu)
        duzenlenmis_resim=resim.copy()
        cizim=ImageDraw.Draw(duzenlenmis_resim)
        guncelle_canvas()


def guncelle_canvas():

 global canvas_resim
 tk_resim=ImageTk.PhotoImage(duzenlenmis_resim)
 canvas_resim=tk_resim
 canvas.create_image(0,0,anchor=tk.NW,Image=tk_resim)
 canvas.config(scrollregion=canvas.bbox(tk.ALL))

def siyah_beyaz_yap():


 global duzenlenmis_resim,cizim
 if duzenlenmis_resim:
     duzenlenmis_resim=ImageOps.grayscale(duzenlenmis_resim).convert("RGB")
     cizim =ImageDraw.Draw(duzenlenmis_resim)
     guncelle_canvas()

def yazi_ekle(event):


 if duzenlenmis_resim:
    yazi=yazi_giris.get()
    if yazi:
       x,y=canvas.canvasx(event.x),canvas.canvasy(event.y)
       font =ImageFont.truetype("arial.ttf",yazi_boyut)
       cizim.text((x,y),yazi,fill=yazi_renk,font=font)
       guncelle_canvas()

def yazi_rengi_degistir():

 global yazi_renk
 secilen_renk=colorchooser.askcolor(title="Yazı Rengi Seç")[1]
 if secilen_renk:
   yazi_renk=secilen_renk


def ciz():
  if duzenlenmis_resim:
    canvas.bind("<B1-Motion>",cizim_yap)


def cizim_yap(event):

  x,y=canvas.canvasx(event.x),canvas.canvasy(event.y)
  cizim.ellipse((x-2,y-2,x+2,y+2),fill=kalem_renk,outline=kalem_renk)
  guncelle_canvas()
   
def kalem_rengi_degistir():
   
   
 global kalem_renk
 secilen_renk=colorchooser(title="Kalem Rengi Seç")[1]
 if secilen_renk:
   kalem_renk=secilen_renk
def resmi_kaydet():

 dosya_yolu=filedialog.askopenfilename(defaultextension="*.png",  filetypes=[("PNG Dosyası","*.png")])
 if dosya_yolu:
   duzenlenmis_resim.save(dosya_yolu)

#global degişken oluştur

resim=None
cizim=None
duzenlenmis_resim=None
canvas_resim=None
yazi_renk="red"
yazi_boyut=20
kalem_renk="blue"


ana_pencere=tk.Tk()
ana_pencere.title("Resim Düzenleyici")


arac_cercevesi=tk.Frame(ana_pencere)
arac_cercevesi.pack(side=tk.LEFT, fill=tk.Y, padx=10,pady=10)


yukle_buton=tk.Button(arac_cercevesi,text="Resim Yükle",command=resim_yukle)
yukle_buton.pack(pady=5)

siyah_beyaz_buton=tk.Button(arac_cercevesi,text="Siyah Beyaz Yap", command=siyah_beyaz_yap)
siyah_beyaz_buton.pack(pady=5)


yazi_giris=tk.Entry(arac_cercevesi,width=20)
yazi_giris.pack(pady=5)
yazi_ekle_label=tk.Label(arac_cercevesi,text="Yazıyı eklemek için reme tıklayın")
yazi_ekle_label.pack()


yazi_renk_buton=tk.Button(arac_cercevesi,text="Yazı Rengi Seç",command=yazi_rengi_degistir)
yazi_renk_buton.pack(pady=5)


ciz_buton=tk.Button(arac_cercevesi,text="Çizim Yap",command=ciz)
ciz_buton.pack(pady=5)


kalem_renk_buton=tk.Button(arac_cercevesi,text="Kalem Rengi Degiştir",command=kalem_rengi_degistir)
kalem_renk_buton.pack(pady=5)


kaydet_buton=tk.Button(arac_cercevesi,text="Resmi Kaydet",command=resmi_kaydet)
kaydet_buton.pack(pady=5)


canvas=Canvas(ana_pencere,bg="white",width=600,height=100, scrollregion=(0,0,1000,1000))
canvas.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

canvas.bind("<Button-1>", yazi_ekle)


ana_pencere.mainloop()
















