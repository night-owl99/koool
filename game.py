#now computer is guessing the number...

import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем рандомное число БЛИН

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)

def score_game(random_predict) -> int:
    """Srednee koliche3stvo popytok

    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: average
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'On average the computer guesses your number using {score} tries')
    return(score)

score_game(random_predict)

    
print(f'Количество попыток: {random_predict(10)}')