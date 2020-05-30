# importowanie bibliotek
# do instalowania: pip install pillow
from PIL import Image 

# otwieranie rysunku w RGB mode 
im = Image.open(r"c:\linux\wykresy\p01crop.png") 

# przypisywanie rozmairu w pixelach
# parametr nie wymagany
width, height = im.size 

# punkty do wycinania 
left = 1
top = 2
right = 3
bottom = 4
  
# wycinanie
# oryginał nie będzie niszczony 
im1 = im.crop((left, top, right, bottom)) 
  
# pokazywanie 
#im1.show()

# lub zapisywanie do pliku obrazka
im1.save('c:\linux\wykresy\p01obr.png', 'png')
