import json
from src.Player import *
from src.Horse import *
from src.Track import *
from src.menu import *
import random


player_data = 0


class GameMove:

    def __init__(self):  # this sets all variables and lists used in this class
        self.player_data = None
        self.set_player()
        self.horses_list = []
        self.tracks_list = []
        self.used_track = None
        self.trackObj = None
        self.horseObj = None
        self.used_horses = []
        self.list_of_winners = []

    def place_bet(self):  # here the user can enter a bet value and the horse they are betting on
        try:  # try prevents an error if the user doesn't enter an integer
            self.player_data.bet = int(input("What horse are you placing your bet on?:   ")) - 1
            if self.player_data.bet > len(self.used_horses) - 1:
                print("This horse doesn't exist. Try again")
                self.place_bet()
        except:
            print("please enter a number")
            self.place_bet()
        try:  # same here just for floats
            self.player_data.bet_amount = float(input("And how much do you want to bet?:  "))
            if self.player_data.bet_amount > self.player_data.balance:
                print("You lack the money to do this")
                self.place_bet()
        except:
            print("please enter a number")
            self.place_bet()

    def simulate_race(self):
        self.list_of_winners = []  # this list is used to determine the winning horse
        winner_is = False  # used as a loop condition
        while winner_is is False:
            for r in range(self.trackObj.lanes):  # this formula determines the segments a horse runs
                distance_run = int((self.used_horses[r].speed - self.trackObj.quality / self.used_horses[r].endurance) // 50)

                if distance_run == 0:  # to keep horses from standing still
                    distance_run = 1
                self.trackObj.map[r][self.used_horses[r].cur_pos] = "_"
                self.used_horses[r].cur_pos += distance_run  # updates the horses position on the track

                if self.used_horses[r].cur_pos > len(self.trackObj.map[r]) - 1:  # this is used prevent horses from running of the track
                    self.used_horses[r].cur_pos = len(self.trackObj.map[r]) - 1
                self.trackObj.map[r][self.used_horses[r].cur_pos] = "#"
                self.used_horses[r].update_speed()

                if self.trackObj.map[r][-1] == "#":  # checks if a horse has reached the finish line and determines if a horse was bet on by the player
                    winner_is = True
                    self.list_of_winners.append(self.used_horses[r])
                    if self.player_data.bet == r:
                        self.player_data.winner_status = True
                        self.player_data.wins += 1
                        self.player_data.balance += self.player_data.bet_amount

        self.trackObj.print_track()

        if self.player_data.winner_status is True:
            print("congrats you won")
            input("press enter to continue.")
            self.player_data.winner_status = False
            self.start_game()

        elif self.player_data.winner_status is False:
            self.player_data.loses += 1
            self.player_data.balance -= self.player_data.bet_amount
            if self.player_data.balance == 0:
                print("Looks like you are Broke! Time to start again")
                input("press enter to start all over again.")
                self.set_player()
                self.start_game()
            else:
                print("You lost better luck next time")
                input("press enter to continue.")
                self.start_game()

    def start_race(self):  # sets up the race by selecting a track and Horses
        self.used_track = self.tracks_list[random.randint(0, len(self.tracks_list)-1)]
        self.trackObj = Track(self.used_track["name"], self.used_track["segments"], self.used_track["lanes"], self.used_track["quality"])
        for x in range(self.trackObj.lanes):
            self.horseObj = (self.horses_list.pop(random.randint(0, len(self.horses_list) - 1)))
            self.used_horses.append(Horse(self.horseObj["name"], self.horseObj["speed"], self.horseObj["stamina"], self.horseObj["endurance"]))

            self.trackObj.map[x][self.used_horses[x].cur_pos] = "#"

        skeleton_req = random.randint(0, 100)  # 2% chance to spawn a special horse
        if skeleton_req <= 2:
            self.used_horses[0] = SkeletonHorse("Skelly", 200, 0.25, 3)

        participants = ""  # prints the used horses names above the track
        for na in range(len(self.used_horses)):
            participants += self.used_horses[na].name + " / "
        print(participants)
        self.trackObj.print_track()
        self.place_bet()
        self.simulate_race()

    def set_player(self):  # creates a player instance

        self.player_data = Player(create_player())

    def start_game(self):  # sets up the game
        self.used_track = None

        self.used_horses = []

        self.horses_list = []

        with open("src\\Horse_data.json") as h:  # loads horse data from a json

            self.horses_list = json.load(h)

        self.tracks_list = []

        with open("src\\Tracks_data.json") as t:  # same for tracks

            self.tracks_list = json.load(t)

        print_menu()
        player_input = input("Enter a command: ")  # used to let the user navigate the menu
        if player_input.lower() == "e":
            return
        elif player_input.lower() == "c":
            self.player_data.print_player_stats()
            input("press Enter to return ")
            self.start_game()
        elif player_input.lower() == "s":
            self.start_race()
        else:
            print("Please enter a valid command")
            self.start_game()

