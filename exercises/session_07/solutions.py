class Rectangle:
    """This is a rectangle."""

    def __init__(self, length, width):
        """Initialize rectangle with width and length values."""
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width

    def set_length(self, length):
        """Set length of rectangle."""
        self.length = length

    def get_length(self):
        """Return length of rectangle."""
        return self.length

    def set_width(self, width):
        """Set width of rectangle."""
        self.width = width

    def get_width(self):
        """Return width of rectangle."""
        return self.width



class VolleyballPlayer:
    """This is a volleyball player."""
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id



class VolleyballTeam:
    """This is a team of volleyball players."""
    def __init__(self, name, roster=None, money=0):
        if not isinstance(roster, list):
            raise TypeError
        self.name = name
        self.roster = {p.name: p for p in roster}
        self.money = money

    def transfer_player(self, player_name, other_team, player_value):
        """Transfer a player between this team and another team."""
        if player_name not in self.roster:
            raise KeyError(f"Player {player_name} is not part of team {self.name} and therefore can not be transfered.")

        other_team.roster[player_name] = self.roster[player_name]
        del self.roster[player_name]

        self.money += player_value
        other_team.money -= player_value



from random import randint

def simulate_match(team_one, team_two):
    match_up = f"{team_one.name} VS. {team_two.name}"
    if team_one.money > team_two.money:
        return f"{match_up} :: {(3, randint(0, 2))}"
    return f"{match_up} :: {(randint(0, 2), 3)}"




