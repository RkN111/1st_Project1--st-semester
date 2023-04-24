from datetime import datetime
# мисля ,че въпросите и отговорите може би трябва да са на отделен файл за да не става натрупано???
quiz_questions_and_answers ={
    'question1':{'What is the name of the current capital of Japan?':'Tokyo'},
    'question2':{'What is the historical period between 300 to 538 AD called?':'Kofun'},
    'question3':{'During which period was "Genji Monogatari" written in?': 'Heian'},
    'question4':{'What is the translation of this kanji in English: 中国':'China'},
    'question5':{'What is the translation of this word in English: ブルガリア':'Bulgaria'},
    'question6':{'Which clan ruled Japan during the Edo period':'Tokugawa'},
    'question7':{'What are the indigenous people living in Hokkaido called?':'ainu'},
    'question8':{'In which city is Fushimi Inari Shrine?':'Kyoto',},
    'question9':{'Who is the goddess of the sun in the Japanese mythology?':'Amaterasu'},
    'question10':{'What era started on May 1st 2019?':'Reiwa'},
    'question11':{'In which prefecture was Osamu Dazai born in?':'Aomori'},
    'question12':{'In which year began the Meiji restoration?':'1868'}
    }
score = 0
# lives = 10???
name = input('Please, enter your name: ')
print (f'''Hello, {name} and welcome to the quiz!
The goal here is to answer 12 questions.
You have 10 lives''')
# for a in quiz_questions_and_answers
