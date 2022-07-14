##### RPG style game, where the player travels the universe in search of menacing opponents to fight with #####
##### CREATED BY: RAYNER LIM FANG YUH #####

# ATTRIBUTES
# travel_count : the number of times travel() is being called OR the number of opponents faced so far
# name : the name of your character
# role : the role of your character, Warrior, Butcher, or Mage (case sensitive)
# lives :  the number of lives your character has, initialised to 5 at the start
# coins : the number of cons your character has, initialised to 100 at the start

# METHODS :
# Getters : get_name, get_coins, get_role, get_travel_count, get_lives

# summary : returns a summary of the player's attributes, name, role, coins, lives.

# set_enemy_lives : initialises the opponent's lives to 3, this is also the number of times attack() needs to be called for opponent to be slayed.
#
# attack : attack the opponent with a variety of skills, stored in a dictionary, for different roles. Each time attack() is called,
#          opponent's lives will drop by 1 until it reaches 0, where a congratulatory message will be printed. 40 coins will be added to you after
#          defeating it. After travel_count reaches 3, your number of lives will also drop by 1.
#
# retreat : a message will seek your confirmation in retreating. Pay 60 coins to retreat from battle with opponent.
#
# travel : call travel() to 'search' for an opponent, instantiates an opponent object.
#
# heal : call heal() to gain an additional life at a cost of 50 coins

########## STEPS TO PLAY THE RPG GAME ##########
# to play this game effectively, you can just use the methods; summary(), travel(), attack() OR retreat(), heal()
# IMPORTANT NOTE : you always must use travel() first, to create opponent, before attack()
# 1. first create your player by creating an instance of the RPG_Player class, RPG_Player(*character name, *role chosen)
# 2. if you would like to see a summary of your character, use the summary() method
# 3. call the travel() method to search for opponents throughout the vast universe
# 4. either call attack(), to attack the opponent, or call retreat(), to retreat the battle but at a cost of 60 coins
# 5. a congratulatory message will be printed if you have successfully defeated the opponent, call travel() again to search for another opponent
# 6. call summary() again if you would like to check your number of lives or number of coins
# 7. HAVE FUN !!!

# libraries used: random, time

import random
import time
opponent = None

class RPG_Player():
    travel_count = 0         # the num of times traveled to search for opponents
    def __init__(self, name, role):
        """ constructor """
        self.name = name     # name of player
        self.role = role     # role of player (warrior, butcher, mage)
        self.lives = 5       # initialise num of lives
        self.coins = 100     # coins to purchase lives, can earn more from defeating others

    ### Methods
    def summary(self):
        """ provides a summary of the player's despcription """
        print("Name: {}\nRole: {}\nCoins: {}\nLives: {}".format(
        self.name,self.role,self.coins,self.lives))
        return

    def get_name(self):
        return self.name

    def get_lives(self):
        return self.lives

    def get_role(self):
        return self.role

    def get_coins(self):
        return self.coins

    def get_travel_count(self):
        return self.travel_count

    def set_enemy_lives(self):
        """ initialise the num of enemy's lives to 3 """
        # means that player only needs to attack enemy 3 times
        opponent.lives = 3
        return

    def attack(self):
        # IMPORTANT: you need to travel first before you can attack
        # returns None
        moves = {'warrior':['Thunder Clap', 'Whirlwind Spin', 'Burning Flame'],
                'butcher':['Heavy Swipe', 'Thousand Smashes', 'Strong Quake'],
                'mage':['Poison Strike', 'Gypsy Attack', 'Magic Carnage']}
        player_ind = random.randint(0,len(moves[self.role.lower()])-1)
        opp_ind = random.randint(0,len(moves[opponent.role.lower()])-1)

        player_move = moves[self.role.lower()][player_ind]
        opp_move = moves[opponent.role.lower()][opp_ind]

        print("You have unleashed {} on your enemy!".format(player_move))
        opponent.lives -= 1
        time.sleep(1)
        print("-"*10+" Enemy's lives remaining: {} ".format(opponent.get_lives())+"-"*10)
        print("Your opponent's turn to attack.....")
        time.sleep(1)
        print("Your opponent savaged you with {}!".format(opp_move))
        time.sleep(1)
        if opponent.get_lives() == 0:
            print("-"*20)
            print("Congratulations! You have successfully defeated your opponent!")
            print("You will get 40 coins as reward.")
            self.coins += 40
            if self.get_travel_count() == 3:
                self.lives -= 1
                print("-"*20)
                print("After all that fighting, your body has taken a toll.....")
                print("As a result, you have lost a life")
                print("-"*10+" Your lives remaining: {} ".format(self.get_lives())+"-"*10)
                return
        else:
            print("It's your turn to attack again!")
            print("-"*40)
        return

    def retreat(self):
        """ allows player to retreat battle at a cost of 60 coins """
        res = input("Are you sure you want to retreat? Type yes or no\n")
        if res == "yes":
            if self.get_coins() < 60:
                print("You don't have enough to retreat, you need 60 coins!")
                return
            self.coins -= 60
            print("You have paid 60 coins to escape this battle")
        else:
            print("Continue to attack! Good luck!")

    def travel(self):
        """ travel the universe to look for opponents """
        # instantiates another RPG_Player object called opponent
        self.travel_count += 1
        global opponent
        other_players = ["Warrior", "Butcher", "Mage"]
        other_player_ind = random.randint(0,len(other_players)-1)
        opp_role = other_players[other_player_ind]

        opponent = RPG_Player("Enemy", opp_role)       # initialise an enemy to fight with player
        opponent.set_enemy_lives()

        print("Travelling around the universe.....")
        time.sleep(1.5)
        print("Searching for worthy opponents.....")
        time.sleep(1.5)
        print("A formidable {} found!".format(opp_role))
        print("-"*20)
        print("Choose whether to attack or retreat\nAttack: use attack() method\nRetreat: use retreat() method")

    def heal(self):
        """ buy additional life at 50 coins each """
        if self.get_coins() < 50:
            print("You don't have enough to purchase an additional life.")
            return
        self.lives += 1
        self.coins -= 50
        print("An additional life has been bought.")
        return
