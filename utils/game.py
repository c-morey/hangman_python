import random
from typing import List


class Hangman:
    """A class to represent the Hangman game. The purpose is to find the hidden word."""

    def __init__(self):

        """
        :param possible_words List[str]: A list of words to be guessed.
        :param word_to_find List[str]: The word that the player needs to guess. It's chosen randomly from the possible words list.
        :param lives int: Number of lives the player has. It starts with 5 and decreases until 0 if the players can not find the word.
        :param correctly_guessed_letters List[str]: A list containing the matching letters with the word to guess.
        :param wrongly_guessed_letters List[str]: A list containing the non-matching letters with the word to guess.
        :param turn_count int: An integer that counts each time the player enters a letter.
        :param error_count int: An integer that counts each time the player makes a wrong guess.
        :param num_of_char int: An integer that states the number of unique character the hidden word has.

       """

        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions','butterfly','elephant']
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.num_of_char = 0

    def check_input(self, user_input: str) -> str:
        """
        A method to verify that the player's input is a string and only one character long. If this condition is true, return
        the user input.

        :param user_input: A string letter provided by the player.

        :return: A string that the player provided.
        """

        while user_input.isalpha() == False:
            user_input = input("Please enter a letter: ")
            while len(user_input) != 1:
                user_input = input("Please enter only one letter: ")
        return user_input

    def display_with_space(self, word: str) -> str:
        """
        A method that will add a space between each character.

        :param word: A string.

        :return: A string with space between each character.
        """
        word = [i for i in word]
        return ' '.join(word)

    def start_game(self) -> object:
        """
        A method that initiates the self.play() method, the game starts. During the game, if the player has 0 lives
        then self.game_over() method runs, game ends.
        If the player guesses the word correctly then the self.game_over() methods runs. At the end of each turn,
        correctly and wrongly guessed letters, the remaining lives of the player, how many error the player has made,
        and how many turns the player took will be printed.
        """
        self.play()
        print(self.num_of_char, self.correctly_guessed_letters)


        if self.lives == 0:
            self.game_over()
        if self.num_of_char == len(self.correctly_guessed_letters):
            self.well_played()

            print("Correctly guessed letters: ", self.correctly_guessed_letters)
            print("Wrongly guessed letters: ", self.wrongly_guessed_letters)
            print(f"you have {self.lives} lives remaining")
            print(f"Your turn count: {self.turn_count} ")
            print(f"Total error : {self.error_count}")

    def game_over(self) :

        """ A method that will stop the game and print 'GAME OVER!!!' when the player can not find the word and has 0 lives left."""

        print("GAME OVER!!!")

    def well_played(self) :

        """
        A method that will tell the player that he/she won and it will print the hidden word, in how many turns and errors the player won.'
        when the player guesses the correct word before losing all his/her lives.
        """

        print(f"YES YOU WIN!You found the word: {self.chosen_word} in {self.turn_count} turns with {self.error_count} errors!")

    def play(self):

        """
        A method that picks a random word from the possible_words list, and appends the selected word to the word_to_find list.
        Then, each letter in the chosen word is replaced with dashes (-) so the player does not see the original word yet.
        The method prints out the dashed version of the word and asks the player to enter one letter. Then, the method checks that
        if the user enters a letter that exists in the original word, if yes, the dash (-) is replaced with the correctly guessed letter.
        If not, the player loses 1 life, the words is appended to the wrongly_guessed_letter list, and the method prints
        how many life users have left.

        """

        #chosing a random word from the list
        self.chosen_word = random.choice(self.possible_words)
        self.word_to_find.append(self.chosen_word)
        #assign the length of the unique characters in the chosen word to num_of_char variables. This will later help to check for match.
        self.num_of_char = len(set(self.chosen_word))
        #transform the word into dashes at the beginning of the game
        dashed_word = ["_" for i in range(len(self.chosen_word))]
        print("Here is your word to guess!")
        print(self.display_with_space(dashed_word))

        #when the player's life is not 0 and the number of characters doesn't match, the while loop will keep asking the player to put a new letter.
        while self.lives != 0 and self.num_of_char != len(self.correctly_guessed_letters):
            user_input = self.check_input(input("Please enter a letter: "))
            self.turn_count += 1
            if user_input in self.chosen_word:
                self.correctly_guessed_letters.append(user_input)
                index = 0
                for letter in self.chosen_word:
                    if letter == user_input:
                        #when there is a match, the correctly guessed letter will be replaced by the dash.
                        dashed_word = "".join(dashed_word[:index]) + letter + "".join(dashed_word[index + 1:])
                    index += 1
                print(self.display_with_space(dashed_word))

            #if there is no match between the player's guess and the word, the player loses 1 life, and the letter is added to the wrongly_guessed_letters list.
            else:
                self.lives = self.lives - 1
                self.error_count += 1
                self.wrongly_guessed_letters.append(user_input)
                print(f"Wrong - you lost 1 life \t You have {self.lives} lives remaining!")

