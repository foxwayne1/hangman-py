import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display.append('_')
print(display)

print(f'Chosen word is: {chosen_word}')

guess = input('Guess a letter: ').lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


print(display)
