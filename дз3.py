import random

wordlist =['apple', 'watermelon', 'grapafruit', 'banana']
secret = random.choice(wordlist)
guesses = 'aeiou'
turns = 5Р

while turns > 0:
     missed = 0
     for letter in secret:
         if letter in guesses:
             print (letter,end=' ')
         else:
           print ('_',end=' ')
           missed += 1

     print()

     if missed == 0:
         print ('\nYou win!')
         break

     guess = input('\nВведите букву:')
     guesses += guess

     if guess not in secret:
         turns -= 1
         if turns == 0:
             print ('\n\nThe answer is', secret)