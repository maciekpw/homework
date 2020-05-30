# obliczenia

# importowanie dla rysowania
from lcapy import Circuit

# importowanie dla obliczania
from lcapy import Vstep, R, L, C, t
from matplotlib.pyplot import savefig
from numpy import linspace

# instalowanie: pdflatex wymagane do rysowania
'''
cct = Circuit("""
V 1 0 {V(s)}; down
R 1 2; right
L 2 _0_2; down
W 0 _0_2; right""")
cct.draw('schem01.pdf')
'''

# symulowanie
obwod = Vstep(12) + R(0.5) + C(0.3, 0) + L(0.1, 0)

# parametry działania
vt = linspace(0, 50, 1000)
obwod.Isc(t).plot(vt)

# zapisywanie do pliku png
savefig('sym01.png')
print("wykres gotowy i poprawny")
