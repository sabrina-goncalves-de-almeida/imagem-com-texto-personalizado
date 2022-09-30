from ctypes.wintypes import RGB
from turtle import color
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from numpy import blackman


texto = input('O que deseja escrever em sua imagem: ')

imagem = Image.open('./imagem.png')

desenha = ImageDraw.Draw(imagem)

fonte = ImageFont.truetype('Poppins-Medium.ttf', 90)

desenha.text((121,77),texto,font=fonte, fill=RGB(0,0,0))

imagem.save('novaimagem.png')
