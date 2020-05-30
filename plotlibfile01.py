# rysowanie wykresów

# biblioteka do ryswoania
import matplotlib.pyplot as plt
# biblioteka do importowania danych
import csv

# nowe listy
x = []
y = []

# odczytywanie z pliku pomiarowego
with open('c:/linux/wykresy/pomiary03.log','r') as csvfile:
    # wydzielanie kolumn
    plots = csv.reader(csvfile, delimiter=' ')
    #wczytywanie    
    for row in plots:
       x.append(float(row[0]))
       y.append(float(row[1]))

#rysowanie
#plt.xlim(-0.00001, 0.00001)
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()

#pokazywanie
plt.show()
