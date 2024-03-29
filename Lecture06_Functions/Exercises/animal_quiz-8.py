def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)

score = 0
print('Guess the Animal!')

guess = input('Which one of these is a fish? A) Whale B) Dolphin C) Shark D) Squid. Type A, B, C or D ')
check_guess(guess, 'C')    

print('Your score is ' + str(score))
