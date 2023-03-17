'''
Aisha's Greetings

You are a part of Aisha’s Greetings - a card printing company that prints greeting cards with a hint of personalization! You want to help Aisha create a system that generates cards based on customers’ requests.

You have been provided with two pre-filled card types:

happy_bday.txt: a card with a birthday message
thankyou_card.txt: a card file with a thank you message
'''

# Write your code below:
from contextlib import contextmanager


@contextmanager
def generic(cardType, sender, recipient):
    openedCard = open(cardType, 'r')
    newCard = open(f'{sender}_generic.txt', 'w')
    try:
        newCard.write(f'Dear {recipient}\n')
        newCard.write(openedCard.read())
        newCard.write(f'\nSincerely, {sender}')
        yield newCard
    finally:
        openedCard.close()
        newCard.close()


with generic('thankyou_card.txt', 'Mwenda', 'Amanda'):
    print('Card Generated!')
with open('Mwenda_generic.txt', 'r') as test:
    print(test.read())


class personalized:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.newfile = open(f'{sender}_personalized.txt', 'w')

    def __enter__(self):
        self.newfile.write(f'Dear {self.receiver}\n')
        return self.newfile

    def __exit__(self, *exc):
        self.newfile.write(f'\nSincerely, {self.sender}')
        self.newfile.close()


with personalized('John', 'Michael') as card:
    card.write(
        'I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.')

with generic('happy_bday.txt', 'Josiah', 'Remy'), personalized('Josiah', 'Esther') as card:
    card.write(
        'Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can\'t live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!')