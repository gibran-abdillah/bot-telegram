from PIL import Image,ImageDraw,ImageFont
import random

class gibran_curang:
    def __init__(self,your_file):
        self.your_file = your_file

    def anjay_curang(self,your_file):
        img = Image.open('core/img/template.jpg')
        my_font = ImageFont.truetype(font='core/fonts/hand.ttf',size=140)
        gambar = ImageDraw.Draw(img)
        kiri,tinggi = 274,440
        mulai = 0
        default_tinggi = 440
        for teks in open(your_file,'r').readlines():
            mulai += 1 
            if mulai == 1:
                tinggi += 0;default_tinggi -= 0;gambar.text((kiri,tinggi),teks,(0,0,14),font=my_font)
            else:
                tinggi += 88;default_tinggi += 88
                    
            gambar.text((kiri,tinggi),teks,(0,0,14),font=my_font)
        img.save('gibran.jpg')
    
    def put_text(self,img,gambar,kiri,tinggi,teks,fonts):
        gambar.text((kiri,tinggi),teks,font=fonts)
        img.save('gibran.jpg')
