print('guessinggame')
import random
answer=random.randint(1,10)

end_guesses=0

# comment4 loop end
while True:
    guess_string=input('Guess a number between 1 and 10. You have three guesses: ')
    guess_int=int(guess_string)
    if answer==guess_int:
        print('euphapae')
    else:
        print('minime')
        end_guesses=end_guesses + 1
        
    if end_guesses==3:
        break
print(f'the answer was {answer}')
