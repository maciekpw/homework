# importowanie
# do instalowani
from fpdf import FPDF

# nowy pdf
pdf = FPDF()

# nowa strona nr 1
pdf.add_page()

# czcionka - nie obsłuży polskich znaków kodowania
pdf.set_font("Arial", size=12)
# pisanie
pdf.cell(200, 10, txt="Raport z pomiarów", ln=1, align="C")
# czcionka polska
pdf.add_font('DejaVu', '', 'c:/linux/wykresy/DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)
napisy = u'''
napisane
ładnie
bardzo
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
pdf.multi_cell(0, 5, napisy)

# nowa strona nr 2
pdf.add_page()
pdf.set_font("Arial", size=8)
pdf.cell(200, 10, txt="Raport z pomiarów", ln=1, align="L")
pdf.cell(200, 10, txt="Raport z pomiarów", ln=1, align="R")
pdf.cell(200, 10, ln=5, align="L", txt="Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów Raport z pomiarów")
# x i y: pozycja; w i h: rozmaiary
pdf.image('p01crop.png', w=100)
pdf.image('p02crop.png', x=120, y=43, w=45)
pdf.cell(200, 10, txt="podpisy", ln=1, align="C")
pdf.image('p01crop.png', w=100)
pdf.image('p02crop.png', x=120, y=143, w=45)
pdf.cell(200, 10, txt="podpisy", ln=1, align="C")

# nowa strona nr 3
pdf.add_page()

with open('opisy.log', 'rb') as fh:
            #opisy = fh.read().decode('latin-1')
            opisy = fh.read().decode('utf-8')
#opisy = unicode(opisy1, 'utf-8') 
pdf.set_font('DejaVu', '', 14)
pdf.multi_cell(0, 5, opisy)
pdf.ln()
pdf.cell(200, 10, txt="podpisy", ln=1, align="C")

# zapisanie do pliku pdf
pdf.output('imię_nazwisko_indeks.pdf')
