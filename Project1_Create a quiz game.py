from datetime import datetime
from lib_questions_and_answers import quiz_questions_and_answers as QandA

def get_user_name():
    name = input('Please, enter your name: ')
    print(f'''Hello, {name} and welcome to the quiz!
The goal here is to answer 12 questions.
You have 3 lives''')
    return name

def start_game(name):
    score = 0
    lives = 3
    starting_time = datetime.now()
    for question, answer in QandA.items():
        user_input = input(question + ': ').lower()
        if user_input == answer.lower():
            print('Correct! Keep going!')
            score += 1
        else:
            print('Wrong answer!')
            lives -= 1
            if lives == 0:
                print('Quiz is over')
                break
    ending_time = datetime.now()
    final_time = ending_time - starting_time
    print(f'{name}, here is your final score:\n'+'Score =', score, 'Lives =', lives)
    print(f'Taking the quiz too you: {final_time}')
def main():
    name = get_user_name()
    start_game(name)

main()