class Player:   # This class  is used to track player stats

    def __init__(self, name):

        self.name = name    # Name is chosen by the user other stats are default values that are affected by
        self.balance = 500  # events in the game
        self.wins = 0
        self.loses = 0
        self.bet = 0  # bet is the horse the player places a bet on and bet amount the amount of money the user bets
        self.bet_amount = 0
        self.winner_status = False   # winner status is used to determine if the player won at the end of a race,
                                    # by default, it is False

    def print_player_stats(self):   # This is used to display the players stats to the user
        print("Here are your stats,", self.name)
        print("\n Wins: ", self.wins)
        print("\n Loses: ", self.loses)
        print("\n Balance: ", self.balance, " Dollar")


def create_player():    # This function allows the user to create a player instance
    name_input = str(input("Enter a name: "))
    return name_input
