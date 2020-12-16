# ------------------------------------------------------------
# Aufgabe 6.2
# Schreibe eine Funktion, welche die Anzahl der Vokale einer Zeichenkette berechnet.
# ------------------------------------------------------------

def sum(int_a, int_b):
    return int_a + int_b


# ------------------------------------------------------------
# Aufgabe 6.2
# Schreibe eine Funktion, welche die Anzahl der Vokale einer Zeichenkette berechnet.
# ------------------------------------------------------------
def count_vowels(string):
    """Return the vowel count of a given string."""
    return sum([1 for char in string.lower() if char in "aeiou"])

def count_vowels(string):
    count = 0
    vowels = "aeiou"
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

# ------------------------------------------------------------
# Aufgabe 6.3
# Schreibe eine Funktion, welche die Länge eines Videos im Format "mm:ss" (bspw. ""02:54") entgegen nimmt und die Länge des Videos in Sekunden zurückgibt.
# ------------------------------------------------------------

def convert_video_length(time):
    """Convert the length of a video from format 'mm:ss' to seconds."""
    minutes, seconds = [int(elem) for elem in time.split(":")]
    return (minutes * 60) + seconds

def convert_video_length(time):
    """Convert the length of a video from format 'mm:ss' to seconds."""
    minutes = int(time[:2])
    seconds = int(time[-2:])
    return (minutes * 60) + seconds

# ------------------------------------------------------------
# Aufgabe 6.4
# Schreibe eine Funktion, welche die Fakultät einer Ganzahl berechnet.
# Die Fakultät einer Ganzzahl ist das Produkt der Ganzzahl mit allen kleineren positiven Ganzzahlen.
# ------------------------------------------------------------
def factorial_iterative(n):
    """Compute the factorial of an integer n iteratively."""
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factorial_recursive(n):
    """Compute the factorial of an integer n recursivly."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

memo = {0: 1, 1: 1}
def factorial_memoized(n):
    """Compute the factorial of an integer n."""
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memoized(n-1)
    return memo[n]


# ------------------------------------------------------------
# Aufgabe 6.4
# Schreibe eine Funktion, welche die n-te Zahl der Fibonacci-Folge berechnet.
# ------------------------------------------------------------
def fib(n):
    """Compute the n-th number of the fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibi(n):
    """Compute the n-th number of the fibonacci sequence."""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

memo = {0: 0, 1: 1}
def fibm(n):
    """Compute the n-th number of the fibonacci sequence."""
    if n in memo:
        return memo[n]
    memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
