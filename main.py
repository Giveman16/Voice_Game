import speech_recognition as sr
from random import choice
from time import sleep

def voice_to_text():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        text = recog.recognize_google(audio, language='en-En')
        return text
    
levels = {
    'easy': ['hello', 'apple', 'speed', 'dog'],
    'medium': ['tired', 'awful', 'developer', 'comfortable'],
    'hard': ['machine learning', 'route cashing', 'neural network', 'deep learning']
}

def game():
    level = input('Какой уровень игры вы выберете? (easy, medium, hard):')
    while level not in levels:
        print('Такого уровня нету')
        level = input('Какой уровень игры вы выберете? (easy, medium, hard):')
    
    words = levels.get(level)
    words = words.copy()
    score = 0
    attempts = 3
    while True:
        if attempts <= 0:
            print('У вас закончились попытки! Вы проиграли!')
            break
        if attempts > 0 and len(words) == 0:
            print('Вы выиграли!')
            break
        word = choice(words)
        print(f'Проговорите слово "{word}"')
        player_word = voice_to_text().lower()
        if player_word == word:
            print('Вы ответили правильно!')
            score += 1
            words.remove(word)
        else:
            attempts -= 1
            print('Вы ответили неправильно!')
game()
