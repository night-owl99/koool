#game guess the number

import numpy as np

number = np.random.randint(1, 100) #random number

#number of tries
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number is smaller")
        
    elif predict_number < number:
        print("The number is bigger")
        
    else:
        print(f"You've guessed the number using {count} tries! The number is {number}")
        break #we quit the game, yay