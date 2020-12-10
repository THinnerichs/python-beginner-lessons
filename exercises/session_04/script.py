# ------------------------------------------------------------
# Aufgabe 5.1
# Schreibe ein Python Programm, welches die Liste der Quadrate der Zahlen von 1 bis 20 erzeugt, wenn diese Zahlen kleiner als 5 oder größer als 14 sind (mit List comprehensions).
# new_list = [expression for member in iterable]
# new_list = [expression for member in iterable (if conditional)]
# ------------------------------------------------------------

l = [i + j for i in range(1, 21) for j in range(1, 21) if ...]

squares = [n**2 for n in range(1, 21) if n < 5 or n > 14]

print([n for n in range(1, 21) if n < 5 or n > 14])
print(squares)


# ------------------------------------------------------------
# Aufgabe 5.2
# Schreibe ein Programm, welches eine gegebene, geordnete Liste von Zahlen von Duplikaten befreit.
# ------------------------------------------------------------
numbers = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8]

deduped = list(set(numbers))
print(deduped)

deduped = []
for n in numbers:
    if n not in deduped:
        deduped.append(n)
print(deduped)

deduped = list(dict.fromkeys(numbers))
print(deduped)

# ------------------------------------------------------------
# Aufgabe 5.3
# Schreibe ein Programm, welches eine gegebene, ungeordnete Liste von Zahlen von Duplikaten befreit.
# ------------------------------------------------------------
numbers = [8, 2, 2, 3, 6, 3, 7, 2, 1]

deduped = []
for n in numbers:
    if n not in deduped:
        deduped.append(n)
print(deduped)

deduped = list(dict.fromkeys(numbers))

# ------------------------------------------------------------
# Aufgabe 6.1
# Schreibe ein Python Programm, welches zwei gegebene dicts zusammenfügt.
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
# Aufgabe 6.2
# Schreibe ein Python Programm, welches welches die Überschneidungen zweier gegebener dicts ausgibt.
# ------------------------------------------------------------
ages_a = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}
ages_b = {"Alice": 42, "Carol": 59, "Trudy": 80, "Victor": 23}

intersecting_keys = ages_a.keys() & ages_b.keys()
print(intersecting_keys)

# ------------------------------------------------------------
# Aufgabe 6.3
# Schreibe ein Python Programm, welches ein gegebenes dict nach den values sortiert.
# ------------------------------------------------------------
ages = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}

# Sortiere die Keys des Dictionaries entsprechend ihrer Werte
sorted_ages = {}
for key in sorted(ages, key=ages.get):
    sorted_ages[key] = ages[key]

sorted_ages = dict(sorted(ages.items(), key=lambda tup: tup[1]))

# ------------------------------------------------------------
# Aufgabe 6.4
# Schreibe ein Python Programm, welches alle geraden Einträge eines gegebenen dicts löscht.
# ------------------------------------------------------------
ages = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}

for key, value in ages.items():
    if value % 2 == 0:
        del ages[key]

# ------------------------------------------------------------
# Aufgabe 6.5
# Schreibe ein Python Programm, welches den größten und kleinsten value einer gegebenen Liste ausgibt.
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
# Aufgabe 6.5
# Schreibe ein Python Programm, welches den größten und kleinsten value eines gegebenen dicts ausgibt.
# ------------------------------------------------------------
ages = {"Alice": 42, "Bob": 80, "Carol": 59, "Dan": 25, "Erin": 73}

print(f"Kleinster Wert des Dictionary ages: {min(ages, key=ages.get)}")
print(f"Größter Wert der Dictionary ages: {max(ages, key=ages.get)}")

# ------------------------------------------------------------
# Aufgabe 6.6
# Schreibe ein Python Programm, welches ein gegebenes dict nach values größer 170 filtert (Nur Paare mit $value>170$ verbleiben)
# ------------------------------------------------------------
d = {1: 430, 2: 780, 3: 901, 4: 147, 5: 888, 6: 42}

filtered = {key: value for key, value in d.items() if value > 170}
