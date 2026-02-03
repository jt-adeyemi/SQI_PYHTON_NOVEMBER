cbt_log = [
    {'question': 'What is 2 + 2?', 'options': {'a': '3', 'b': '4', 'c': '5', 'd': '6'}, 'answer': 'b'},
    {'question': 'What color is the sky on a clear day?', 'options': {'a': 'Red', 'b': 'Blue', 'c': 'Green', 'd': 'Yellow'}, 'answer': 'b'},
    {'question': 'How many legs does a spider have?', 'options': {'a': '6', 'b': '7', 'c': '8', 'd': '9'}, 'answer': 'c'},
    {'question': 'What sound does a cow make?', 'options': {'a': 'Meow', 'b': 'Bark', 'c': 'Moo', 'd': 'Quack'}, 'answer': 'c'},
    {'question': 'What is the opposite of hot?', 'options': {'a': 'Warm', 'b': 'Cold', 'c': 'Cool', 'd': 'Boiling'}, 'answer': 'b'}
]


def questions():
    global score
    score = 0

    for index, data in enumerate(cbt_log, start=1):
        print(f'{index}. {data['question']}')
        for key, value in data['options'].items():
            print(f'{key}) {value}\n')
        # print(data['options'])

        choice = input('Enter an option from a to d: ').lower()  
        if choice == data['answer']:
            score += 1            



print('''.....................WELCOME TO CBT EXAM..........................
INSTRUCTION: Answer all questions. Each question carry equal mark.
''')

questions()

print(f'You scored {score} points.')

