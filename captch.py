import random as rn
from captcha.image import ImageCaptcha
from rich.progress import track
from time import sleep
from PIL import Image

size = rn.randint(5,8)
abc = list("abcdefghijklmnopqrstuvwxyz1234567890")
i = 0
w = []
word = ""
while i < size:
    numabc = rn.randint(0, 35)
    w.append(abc[numabc])
    i+=1
for i in range(0, len(w)):
    word = word + w[i]
#print(word)

image = ImageCaptcha(width=250, height=90)

data = image.generate(word)
image.write(word, "captcha.png")

img = Image.open('captcha.png')
img.show()

def progrees():
    def stop(st):
        sleep(rn.uniform(0.1, 0.01))
    for st in track(range(15), description="Проверка..."):
        stop(st)
    print("Успешно!")

check = ""

while check != word:
    check = input("Введите текст с картинки: ")

progrees()


    