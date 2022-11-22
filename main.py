import random

wordleList = ['THERE','GRAVE','BRAVE','LEARN','HAPPY','FORCE','LEAST','PREFER','WORDLE','TUTOR',
'CLASS','SPEAK','STONE','EARTH','THINK','SHARE','BLOOD','POWER','WATER','CREAM','QUEEN']

def guess():
    # return the valid user's guessed input 
    while True:
        guessedWord = input('Your guess is: ')
        if len(guessedWord) != 5 or not guessedWord.isalpha():
            print('Guess should be 5 letters. Please try again')
            
        else:
            print(f'You entered {guessedWord}')
            return guessedWord.upper()

def menu():
    # starts the game with maximum of 6 lifes
    print('Welcome to WORDLE!')
    guessedWord = ''
    chances = 6
    answer = random.choice(wordleList)
    while guessedWord != answer:
        if chances == 0:
            return 'Game Over! The word is: ' + answer 
        print('You have', chances, ' chances left!' )
        guessedWord = guess()
        checkWord(guessedWord,answer)
        chances -= 1
    return 'Congratulations! You guessed the right word: ' + answer

def checkWord(word, answer):
    # displays the result of the word guessed and checks if it matches with the answer
    condition = []
    for i in range(len(word)):
        if word[i] == answer[i]:
            condition.append('green')
        elif word[i] not in answer:
            condition.append('grey')
        else:
            condition.append('yellow')
    print(condition)
    
if __name__ == '__main__':
    print(menu())

