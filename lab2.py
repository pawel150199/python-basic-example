from ast import Pass, arg
from os import lseek
import random
from re import S, X
import string
from zipfile import ZipFile
from PIL import Image
from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from click import File


class Password(object):
    def __init__(self):
        self.password = []

    def generate(self):
        xd = list(string.ascii_letters)

        for i in string.digits:
            xd.append(i)

        for i in string.punctuation:
            xd.append(i)

        for i in range(8):
            self.password.append(xd[random.randint(0, 93)])

        return " ".join(self.password)


class Min:
    def __init__(self, image_name, height, width, output_name):
        self.image_name = image_name
        self.height = height
        self.width = width
        self.output_name = output_name

    def miniaturizing(self):
        try:
            with Image.open(self.image_name) as im:
                new = im.resize((int(self.width), int(self.height)))
                new.save(self.output_name, "JPEG")
        except FileNotFoundError:
            print("Nie ma takiego pliku")


def zipping(*args):
    for arg in args:
        try:
            with ZipFile(f"{arg}-{datetime.now()}.zip", "w") as zip:
                zip.write(arg)
        except FileNotFoundError:
            print("Sprawdz czy taki katalog istnieje!")


def divided(name, p_numb):
    inputpdf = PdfFileReader(open(name, "rb"))
    marker = 1
    flag = True

    while flag:
        output = PdfFileWriter()
        try:
            for i in range(p_numb):
                output.addPage(inputpdf.getPage(marker))
                marker += 1
            with open(f"{'new'}-{marker}-{marker + p_numb}.pdf", "wb") as outputStream:
                output.write(outputStream)
            if inputpdf.getNumPages() < marker:
                flag = False
        except IndexError:
            break


def watermark(img_path, watermark_path, size, position, transparency):
    with Image.open(watermark_path) as watermark:
        # creating watermark
        watermark.putalpha(transparency)
        watermark.thumbnail(size)
        watermark.putalpha(1)

        # adding watermark
    with Image.open(img_path) as org_image:
        org_image.paste(watermark, position)
        org_image.show()
        org_image.save("watermarked_image", 'png')


def matematica(gf):
    output = eval(gf)

    if gf.find('+') >= 0:
        lend = 0
        x = gf.split('+')
        x1 = ''.join(x[0])
        x2 = ''.join(x[1])
        if len(x1)>len(x2):
            lend = len(x1)
        print(x1.rjust(lend+4, ' '))
        print("+", x2.rjust(lend+2, ' '))
        print("".rjust(lend+4, '-'))
        print(str(output).rjust(lend+4, ' '))
        print("\n\n\n")

        

    elif gf.find('-')>= 0:
        lend = 0
        x = gf.split('-')
        x1 = ''.join(x[0])
        x2 = ''.join(x[1])
        if len(x1)>len(x2):
            lend = len(x1)
        print(x1.rjust(lend+4, ' '))
        print("-", x2.rjust(lend+2, ' '))
        print("".rjust(lend+4, '-'))
        print(str(output).rjust(lend+4, ' '))
        print("\n\n\n")

    elif gf.find('*')>= 0:
        lend = 0
        x = gf.split('*')
        x1 = ''.join(x[0])
        x2 = ''.join(x[1])
        if len(x1)>len(x2):
            lend = len(x1)
        print(x1.rjust(lend+4, ' '))
        print("*", x2.rjust(lend+2, ' '))
        print("".rjust(lend+4, '-'))
        print(str(output).rjust(lend+4, ' '))
        print("\n\n\n")

  

