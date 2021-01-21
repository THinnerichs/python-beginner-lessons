
def double_list_elements_using_builtin(lst):
    doubled_values = map(lambda n: n*2, lst)
    return list(doubled_values)

def double_list_elements_using_list_comprehension(lst):
    """Double the values contained in *lst*.

    """
    return [n*2 for n in lst]

def all_even_list_elements_using_builtin(lst):
    """Return the list of even numbers contained in *lst*.

    Using the built-in function *filter*.
    """
    filtered_evens = filter(lamdba n: n % 2 == 0, lst)
    return list(filtered_evens)

def all_even_list_elements_using_list_comprehension(lst):
    """Return the list of even numbers contained in *lst*.

    Using only list comprehensions.
    """
    return [n for n in lst if n % 2 == 0]

def three_dimension_zip_using_builtin(xs, ys, zs):
    """Zip three lists of coordinates to a list of three coordinate tuples.

    Using the built-in function *zip*.
    """
    zipped = zip(xs, ys, zs)
    return list(zipped)

def three_dimension_zip_using_list_comprehension(xs, ys, zs):
    """Zip three lists of coordinates to a list of three coordinate tuples.

    Using only list comprehensions.
    """
    return [(xs[i], ys[i], zs[i]) for i in range(len(xs))]

def add_three_lists_elementwise_using_builtin(xs, ys, zs):
    """Add the elements of three same sized lists elementwise.

    Using the built-in function *zip*.
    """
    zipped = zip(xs, ys, zs) # list-like container of three element tuples
    sums = map(sum, zipped) # sum the tuples into singular values
    return list(sums)

def add_three_lists_elementwise(xs, ys, zs):
    """Add the elements of three same sized lists elementwise.

    Using only list comprehensions.
    """
    return [xs[i] + ys[i] + zs[i] for i in range(len(xs))]


from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

class Player:
    def __init__(self, name, dice):
        self.name = name
        self.dice = dice

    def roll_dice(self):
        """Roll all dice that the player"""
        rolls = []
        for die in self.dice:
            rolls.append(self.die.roll())
        return rolls
