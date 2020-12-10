# ------------------------------------------------------------
# Aufgabe 4.1
# Schreibe ein Programm, welches alle geraden Zahlen einer Zahlenliste in einer zweiten Liste speichert und stoppt, sobald eine 237 vorkommt.
# ------------------------------------------------------------
numbers = list(range(300))
even_numbers = []

for n in numbers:
    if n == 237:
        break
    elif n % 2 == 0:
        even_numbers.append(n)

# ------------------------------------------------------------
# Aufgabe 4.2
# Schreibe ein Programm, welches alle Elemente einer Liste von Strings zusammenfügt und ausgibt.
# ------------------------------------------------------------
strings = ["Nein!", "Doch!", "Oh..."]

joined = ""
for substring in strings:
    joined += substring

joined = " ".join(strings)


# ------------------------------------------------------------
# Aufgabe 4.3
# Schreibe ein Programm, welches den Namen sowie den Heimatplaneten des/der Nutzer*in abfragt und ihn/sie entsprechend grüßt.
# ------------------------------------------------------------
name = input("Wie heißt du noch gleich?")
planet = input("Von welchem Planeten kommst du?")
print(f"Dann grüß dich {name} vom Planeten {planet}! Wie schön, dass es dich gibt.")

print("Grüße dich", name, "vom Planeten", planet)


# ------------------------------------------------------------
# Aufgabe 4.4
# Schreibe ein Programm, welches die Seitenlänge *h* eines Dreiecks und die zugehörige Höhe *h_c* einliest und den Flächeninhalt des Dreiecks berechnet.
# ------------------------------------------------------------
h = int(input("Seitenlänge h: "))
h_c = int(input("Höhe h_c: "))
area = (h * h_c) / 2

print(f"Die Fläche des Dreiecks beträgt ({h} * {h_c}) / 2 = {(h * h_c) / 2}")


# ------------------------------------------------------------
# Aufgabe 4.5
# Quersumme berechenen.
# ------------------------------------------------------------
n = 133
cross_sum = 0
while n:
    # Addiere den Rest Modulo 10 (Division mit Rest)
    cross_sum += n % 10
    # Floor Division mit Doppel-Slash Operator '//'
    # '//' entspricht der Division mit anschließendem Abrunden
    n //= 10

cross_sum = sum([int(c) for c in str(n)])


# ------------------------------------------------------------
# Aufgabe 5.1
# Schreibe ein Programm, welches zwei Dictionaries zusammenfügt.
# ------------------------------------------------------------
a = {"Alice": 42, "Bob": 80, "Carol": 59}
b = {"Dan": 25, "Erin": 73}

# Naiver Ansatz
merged = {}
for key, value in a.items():
    merged[key] = value
for key, value in b.items():
    merged[key] = value

# Mit dict.update() (funktional äquivalent zum naiven Ansatz)
merged = {}
merged.update(a)
merged.update(b)

# Mit dem Unpacking Operator
merged = {**a, **b}

# Mit dem Unpacking Operator und dict() Creation (Keyword Arguments)
merged = dict(a, **b)


# ------------------------------------------------------------
# Aufgabe 5.2
# Schreibe ein Programm, welches ein Dictionary den Values des Dictionary entsprechend aufsteigend sortiert.
# ------------------------------------------------------------

ages = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}

# Sortiere die Keys des Dictionaries entsprechend ihrer Werte
sorted_ages = {}
for key in sorted(ages, key=ages.get):
    sorted_ages[key] = ages[key]

sorted_ages = dict(sorted(ages.items(), key=lambda tup: tup[1]))


# ------------------------------------------------------------
# Aufgabe 5.3
# Schreibe ein Programm, welches alle gerade Einträge eines Dictionaries löscht.
# ------------------------------------------------------------

ages = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}

for key, value in ages.items():
    if value % 2 == 0:
        del ages[key]


# ------------------------------------------------------------
# Aufgabe 5.3
# Schreibe ein Programm, welches den größten und kleinsten Wert einer Liste ausgibt.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

smallest = numbers[0]
for n in numbers[1:]:
    if n < smallest:
        smallest = n

greatest = numbers[0]
for n in numbers[1:]:
    if n > greatest:
        greatest = n

print(f"Kleinster Wert der Liste numbers: {smallest}")
print(f"Größter Wert der Liste numbers: {greatest}")

print(f"Kleinster Wert der Liste numbers: {min(numbers)}")
print(f"Größter Wert der Liste numbers: {max(numbers)}")


# ------------------------------------------------------------
# Aufgabe 5.4
# Schreibe ein Programm, welches den größten und kleinsten Wert eines Dictionaries ausgibt.
# ------------------------------------------------------------

ages = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}

print(f"Kleinster Wert des Dictionary ages: {min(ages, key=ages.get)}")
print(f"Größter Wert der Dictionary ages: {max(ages, key=ages.get)}")


# ------------------------------------------------------------
# Aufgabe 5.5
# Schreibe ein Programm, welches ein Dictionary nach Werten größer 170 filtert.
# ------------------------------------------------------------
d = {1: 430, 2: 780, 3: 901, 4: 147, 5: 888, 6: 42}

filtered = {key: value for key, value in d.items() if value > 170}


# ------------------------------------------------------------
# Aufgabe 5.5
# Schreibe ein Programm, welches ein Dictionary nach Werten größer 170 filtert.
# ------------------------------------------------------------

ages_a = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}
ages_b = {"Alice": 42, "Carol": 59, "Trudy": 80, "Victor": 23}

intersecting_keys = ages_a.keys() & ages_b.keys()
print(intersecting_keys)
