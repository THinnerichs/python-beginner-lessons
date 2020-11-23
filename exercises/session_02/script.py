# In dieser Session werden häufiger die Begriffe 'Funktion' und 'Methode' verwendet.
#
# 'Funktionen' sind unabhängig und können direkt über ihren Namen aufgerufen werden
# 'Methoden' hingegen benötigen stehts das Objekt, welches sie definiert
#
# Beispiel:
# range(...) ist eine Funktion
# list.append(...) ist eine Methode des Objektes 'list'


# ------------------------------------------------------------
# Aufgabe 3.1
# Schreibe ein Python Programm, welches alle Zahlen von 1 bis 20 addiert.
# ------------------------------------------------------------

# Die Funktion 'range' generiert eine Sequenz an 'Integer'-Werten (Ganzzahl)
# Ähnlich einer Liste, kann die generierte Sequenz mit einer for-Schleife schrittweise durchlaufen werden
# Für mehr Informationen zur Funktion 'range' siehe 'help(range)'

acc_sum = 0
for elem in range(21):
    acc_sum += elem
print(acc_sum)


# ------------------------------------------------------------
# Aufgabe 3.2
# Schreibe ein Python Programm, welches alle Zahlen einer Liste aufsummiert.
# ------------------------------------------------------------

numbers = [1, 2, 3]
acc_sum = 0

for elem in numbers:
    acc_sum += elem
print(acc_sum)

# Mit der built-in Funktion 'sum'
# Für mehr Informationen zur Funktion 'sum' siehe 'help(sum)'
print(sum(numbers))


# ------------------------------------------------------------
# Aufgabe 3.3
# Schreibe ein Python Programm, welches alle geraden Zahlen von 1 bis 20 ausgibt.
# ------------------------------------------------------------

# Hinweis: Diese Aufgabe wurde abgewandelt bereits in Session 01 gestellt.
# Merke: Für die Iteration über Sequenzen wie Listen eignen sich for-Schleifen meist besser als while-Schleifen

for elem in range(21):
    # Reminder: Der Modulo Operator '%' ermöglicht die Division mit Rest
    if elem % 2 == 0:
        print(elem)


# ------------------------------------------------------------
# Aufgabe 3.4
# Schreibe ein Python Programm, welches eine gegebene Liste in ihrer Reihenfolge invertiert.
# ------------------------------------------------------------

# Mit der Listen Methode 'insert'
# Für mehr Informationen zur Methode 'insert' siehe 'help(list.insert)'
#
# Ablaufschema der Lösung ('*' markiert aktuelles Element 'elem')
# numbers  = [*1*, 2, 3, 4, 5]
# inverted = [1]
#
# numbers  = [1, *2*, 3, 4, 5]
# inverted = [2, 1]
#
# numbers  = [1, 2, *3*, 4, 5]
# inverted = [3, 2, 1]
#
# numbers  = [1, 2, 3, *4*, 5]
# inverted = [4, 3, 2, 1]
#
# numbers  = [1, 2, 3, 4, *5*]
# inverted = [5, 4, 3, 2, 1]

numbers = [1, 2, 3, 4, 5]
inverted = []
for elem in numbers:
    inverted.insert(0, elem)


# Mit der Listen eigenen Methode list.reverse()
# Für mehr Informationen zur Methode 'list.reverse' siehe 'help(list.reverse)'
print(numbers.reverse())

# Mit der built-in Funktion reversed()
# Für mehr Informationen zur Funktion 'reversed' siehe 'help(reversed)'
print(list(reversed(numbers)))

# Mit 'list slicing'
print(numbers[::-1])


# ------------------------------------------------------------
# Aufgabe 4.1
# Frage den/die Nutzer*in nach Vor- und Nachname und grüß ihn/sie.
# ------------------------------------------------------------

firstname = input("Vorname: ")
surname = input("Nachname: ")
print(f"Moin {firstname} {surname}. Schön, dass es dich gibt!")


# ------------------------------------------------------------
# Aufgabe 4.2
# Lese zwei Zahlen ein und berechne deren Summe.
# ------------------------------------------------------------

a = int(input("Summand a: "))
b = int(input("Summand b:"))
# Note: In f-String {}-Feldern kann Code (wie hier 'a + b') ausgeführt werden.
print(f"{a} + {b} = {a + b}")


# ------------------------------------------------------------
# Aufgabe 4.3
# Lese eine (von dem/der Nutzer*in festzulegende) Anzahl an Zahlen ein.
# Berechne die Summe (Maximum, Mittelwert, ...) und gib sie zusammen mit der Liste der Zahlen aus.
# ------------------------------------------------------------

numbers = []
for n in range(int(input("Wie viele Zahlen sollen eingelesen werden?"))):
    x = int(input(f"Zahl {n}: "))
    numbers.append(x)

average = sum(numbers) / len(numbers)
maximum = max(numbers)

print(numbers)
# Note: In f-String {}-Feldern kann Code (wie hier die Funktion sum) ausgeführt werden.
print(f"Summe: {sum(numbers)}")
print(f"Arithmetischer Mittelwert: {average}")
print(f"Größte Zahl: {maximum}")


# ------------------------------------------------------------
# Aufgabe 4.3
# Wähle eine beliebige natürliche Zahl.
# Lasse den/die Nutzer*in deine Zahl raten.
# Rät der/die Nutzer*in falsch, dann gib einen entsprechenden Hinweis. (zu klein/zu groß)
# ------------------------------------------------------------

target = 20
attempt_count = 0

while True:
    guess = int(input("Rate eine beliebige natürliche Zahl: "))
    attempt_count += 1

    if guess < target:
        print("Deine Zahl ist zu klein. Versuch es nochmal!")
    elif guess > target:
        print("Deine Zahl ist zu groß. Versuch es nochmal!")
    else:
        print(f"Super! Du hast die Zahl nach {attempt_count} Versuchen richtig geraten!")
        break
