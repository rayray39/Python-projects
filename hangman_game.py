##### HANGMAN GAME IMPLEMENTED USING OBJECT-ORIENTED PROGRAMMING #####
##### CREATED BY: RAYNER LIM FANG YUH ######

# FUTURE IMPROVEMENTS :
# Possible addition of 'lives counter'. As of now, players have unlimited tries to guess the word.
# A new method (eg. get_lives()) could be added to show the number of tries players have left.
# Each time the player guesses incorrectly, -1 from the counter.
# Could initialise with n = 5 lives or n = len(word)//2 lives

# ATTRIBUTES :
# topic : the topic chosen
# list_of_topics : the words' dictionary, which represent the topics and words used
# word : the word that is to be guessed / the answer
# masked_word : the word that needs to be guessed, but masked with *
# temp_word : a list, each element represents the characters of the word

# METHODS :
# get_topic : returns the chosen topic
# set_topic : choose a topic under the list_of_topics, returns None
# get_word :  returns the word that needs to be guessed with a mask, and the length of the word
# show_answer : returns the answer/the word that needs to be guessed
# set_word :  call this method once to randomly set the word that needs to be guessed
# guess_word : guess a single letter
# guess_answer : guess the full answer

# STEPS TO PLAY THE HANGMAN GAME
# to play this game effectively, you can just use the methods; set_word(), get_word(), guess_word(), guess_answer()
# 1. create an instance of the Hangman class with a choice of topic as the parameter
# 2. use set_word() method to initialise the word to be guessed
# 3. continue guessing the guess is wrong, a message will be printed to prompt you to try again
# 4. if guessed correctly, a congratulations message will be printed
# 5. create a new instance of the Hangman class if you wish to continue playing or guess another word

import random

words = {"plteams": ['manchester city', 'liverpool', 'chelsea', 'arsenal'],
        "nbateams": ['brooklyn nets', 'los angeles lakers', 'memphis grizzlies', 'philadelphia 76ers'],
        "foods": ['banana', 'pineapple', 'pizzas', 'mookata'],
        "movies": ["inception", "djanjo unchained", "avengers: infinity war", "dead poets society"]}

def get_indices(word, letter):
    """ helper function """
    """ if letter is found in word, append its index to res """
    res = []
    for i in range(len(word)):
        if word[i] == letter:
            res.append(i)
    return res

class Hangman():
    """ Hangman class """
    def __init__(self, topic):
        # constructor and attributes
        self.topic = topic
        self.list_of_topics = words
        self.word = ""
        self.masked_word = ""
        self.temp_word = []

    ## methods
    def get_topic(self):
        """ returns the chosen topic """
        return self.topic

    def set_topic(self, new_topic):
        """ choose a topic under the list_of_topics """
        self.topic = new_topic
        return

    def get_word(self):
        """ returns the word that needs to be guessed with a mask, and the length of the word """
        return self.masked_word, "length of word = " + str(len(self.word))

    def show_answer(self):
        """ returns the answer/the word that needs to be guessed """
        return self.word

    def set_word(self):
        """ call this method once to randomly set the word that needs to be guessed """
        """ calling it a second time, or more, will result in a bug """
        num_of_words = len(self.list_of_topics[self.topic])
        num = random.randint(0, num_of_words - 1)
        new_word = self.list_of_topics[self.topic][num]
        self.masked_word = "*" * len(new_word)
        self.temp_word.extend(self.masked_word)
        self.word = new_word

    def guess_word(self, letter):
        """ guess a single letter """
        letter = letter.lower()
        if len(letter) == 0 or len(letter) > 1:
            print("Please enter only a single letter!")
            return
        if letter in self.word:
            ind_lst = get_indices(self.word, letter)
            for ii in ind_lst:
                self.temp_word[ii] = letter
            self.masked_word = "".join(self.temp_word)
        else:
            print("The letter is not in the word, try again!")
        return self.get_word()

    def guess_answer(self, answer):
        """ guess the full answer """
        if len(answer) < 1:
            return "Error: Please do not leave blank"
        if answer == self.word:
            return "Congratulations!!! You have correctly guessed the word."
        else:
            return "Your guess is wrong, please try again."
