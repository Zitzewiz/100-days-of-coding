import os

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "apple", "banana", "cat", "dog", "elephant", "flower", "guitar", "happiness", "icecream", "jazz",
    "kangaroo", "lemon", "mountain", "noodle", "ocean", "penguin", "queen", "rainbow", "sunshine", "tiger",
    "umbrella", "violet", "waterfall", "xylophone", "yacht", "zebra", "astronomy", "butterfly", "carousel",
    "dolphin", "eclipse", "fireworks", "giraffe", "hiking", "island", "jungle", "kite", "lighthouse", "mango",
    "nightingale", "orchid", "peacock", "quilt", "raccoon", "seashell", "tornado", "unicorn", "volcano",
    "watermelon", "xylophone", "yarn", "zeppelin", "acrobat", "balloon", "cactus", "dandelion", "eagle",
    "fountain", "gazelle", "harmony", "iguana", "jigsaw", "koala", "llama", "mantis", "narwhal", "otter",
    "panda", "quokka", "raven", "seagull", "toucan", "urchin", "vulture", "wombat", "xenon", "yak", "zeppelin",
    "albatross", "bison", "croissant", "daisy", "euphoria", "flamingo", "gargoyle", "hibiscus", "impala",
    "jackal", "kiwi", "lemur", "marmot", "narwhal", "octopus", "panther", "quail", "raccoon", "sloth",
    "tiger", "unicorn", "vulture", "weasel", "x-ray", "yacht", "zebra"
]

import random

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6
print(logo)

display = []
for letter in chosen_word:
  display.append("_")

while end_of_game != True: 

  print(display)
  print(stages[lives])

  correct_guess = False
  guess = input("Guess a letter \n").lower()
  if guess in display:
    print("You guessed this letter already. Be more creative")
  
  for idx, letter in enumerate(chosen_word):
    if letter == guess:
      display[idx] = guess
      print("\n That was correct!")
  
  if guess not in chosen_word:
    lives -= 1
    print(f"\n Nope. Wrong Letter. {lives} lives left")
  
  if lives == 0: 
    end_of_game = True
    print(f"\n You lose! The word was {chosen_word}")
  if "_" not in display: 
    end_of_game = True
    print(f"\n You win! The word was {chosen_word}")
