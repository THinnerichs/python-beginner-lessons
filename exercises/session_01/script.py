# ------------------------------------------------------------
# Aufgabe 1.1 
# Schreibe ein Programm, welches die Fläche eines Kreises mit r = 4cm und pi = 3,14 berechnet.
# ------------------------------------------------------------

# Kreisradius r
r = 4
# Kreiszahl pi
pi = 3.14
# Flächenberechnung
area = pi * r**2
print(area)


# ------------------------------------------------------------
# Aufgabe 1.2 
# Schreibe ein Programm, welches die Zahlen von 1 bis 20 addiert.
# ------------------------------------------------------------

# Der naive Ansatz
sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20

# Mit Gaußscher Summenformel
n = 20
sum = (n**2 + n) / 2

# Mit while-Schleife, Zähler und Akkumulator
count = 1
sum = 0
while count <= 20:
    # Reminder: 'sum += count' ist synonym zu 'sum = sum + count'
    sum += count
    count += 1
    
print(sum)


# ------------------------------------------------------------
# Aufgabe 2.1 
# Schreibe ein Programm, welches für eine Variable a testet, ob diese zwischen 100 und 2000 liegt.
# ------------------------------------------------------------

a = 100
if a >= 100:
    if a <= 2000:
        print("Variable a liegt zwischen 100 und 2000.")
        
# Mit Boolscher Verknüpfung 'and'
if a >= 100 and a <= 2000:
    print("Variable a liegt zwischen 100 und 2000.")


# ------------------------------------------------------------
# Aufgabe 2.2 
# Schreibe ein Programm, welches für eine Variable a testet, ob diese gerade ist.
# ------------------------------------------------------------

a = 2
# Reminder: Der Modulo Operator '%' ermöglicht die Division mit Rest
if a % 2 == 0:
    print("Variable a ist gerade.")
else:
    print("Variable a ist ungerade.")
    
    
# ------------------------------------------------------------
# Aufgabe 2.3 
# Schreibe ein Programm, welches alle geraden Zahlen zwischen 1 und 10 ausgibt.
# ------------------------------------------------------------

count = 1
while count <= 10:
    if count % 2 == 0: 
        print(count)
    count += 1
    
    
# ------------------------------------------------------------
# Aufgabe 2.4 
# Schreibe ein Programm, welches zwei Variablen addiert. Wenn die Summe zwischen 15 und 20 liegt, gebe 20 zurück.
# ------------------------------------------------------------

a = 10
b = 6
sum = a + b

if sum >= 15:
    if sum <= 20:
        print(20)
        
# Mit boolscher Verknüpfung 'and'
if sum >= 15 and sum <= 20:
    print(20)
