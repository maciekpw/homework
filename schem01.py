# rysowanie schematów dla SchemDraw
import SchemDraw as schem
import SchemDraw.elements as elm

# nowy rysunek
rysunek = schem.Drawing()

# napięcie
V1 = rysunek.add(elm.SOURCE_V, label="10V")

# pozostałe składniki
rysunek.add(elm.RBOX, d="right", label="100K$\Omega$") 
rysunek.add(elm.DOT) 
#rysunek.add(elm.LINE, d="left", move_cur=False) 
#rysunek.add(elm.INDUCTOR, label="0.1$")
rysunek.add(elm.CAP, d="down", label="0.1$\mu$F") 
rysunek.add(elm.LINE, to=V1.start) 
#rysunek.add(elm.LINE, to=V1.start)
rysunek.add(elm.GND) 

# rysowanie
rysunek.draw()
