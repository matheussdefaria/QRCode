from tkinter import *
from tkinter import ttk
import pyqrcode
import png
import os
os.system('clear')

# Funções

def get_url():
    url = url_entry.get()
    return url

def get_name():
    nome = nome_entry.get()
    return nome

def get_scale():
    scale = tamanho.get()
    scale = int(scale)
    return scale

def criar_qrcode():
    new_url = get_url()
    new_name = get_name()
    new_scale = get_scale()
    qrcode = pyqrcode.create(new_url)
    qrcode.png(f'{new_name}.png',scale=new_scale)


# Inteface

root = Tk()
root.title('Qrcode')
root.geometry('200x300')
root.resizable(False,False)
root.config(bg="#E6E6FA")

# Label

titulo_label  = Label (root, text = 'QRCODE  ', bg = "#E6E6FA",font='Sans-Serif')
titulo_label.place(width=200, height=20, x = 0, y = 10)

url_label = Label(root, text='URL', bg = "#E6E6FA")
url_label.place(width=100,height=26, x = 6, y = 40)

nome_label = Label(root,text='NAME', bg = "#E6E6FA")
nome_label.place(width=100,height=26, x = 6, y = 110)

tamanho_label = Label(root,text='SCALE', bg = "#E6E6FA")
tamanho_label.place(width=100,height=26, x = 6, y = 180)

# Entry

url_entry = ttk.Entry(root)
url_entry.place(width=160,height=23, x = 20, y = 70)

nome_entry = ttk.Entry(root)
nome_entry.place(width=160,height=23, x = 20, y = 140)


# Scale


tamanho = ttk.Scale(root,from_=6, to=20, orient='horizontal')
tamanho.place(width= 100, x = 50, y = 210)


# Botoẽs

botao = ttk.Button(root,text='CREATE', command=criar_qrcode)
botao.place(width=100, height=26, x = 50, y = 245)


# Loop
root.mainloop()