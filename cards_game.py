#    clubs = '♣'
#    spades = '♠'
#    diamonds = '♢'
#    hearts = '♡'
from random import *

cards = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
suit = ['♣', '♠', '♢', '♡']
cards_and_suit = []
trump = ''
player1 = []
player2 = []

for i in suit:
    for j in cards:
        cards_and_suit.append(j + i)

print(cards_and_suit)
shuffle(cards_and_suit)

while len(player1) < 6 and len(player2) < 6:
    player1.append(cards_and_suit[0])
    del cards_and_suit[0]
    player2.append(cards_and_suit[0])
    del cards_and_suit[0]
    
trump = cards_and_suit[0]
del cards_and_suit[0]

print(player1)
print(player2)
print(trump)
print(len(cards_and_suit))
print('')

s1 = [i for i in player1 if i[1] == trump[1]]
s2 = [j for j in player2 if j[1] == trump[1]]
if len(s1) != 0:
    print('Player1 =', min(s1))

if len(s2) != 0:
    print('Player2 =', min(s2))

if len(s1) == 0 and len(s2) == 0:
    print('Кто будет ходить первым?')
elif len(s1) == 0 and len(s2) != 0:
    print('Ходит игрок 2')
elif len(s1) != 0 and len(s2) == 0:
    print('Ходит игрок 1')
elif len(s1) != 0 and len(s2) != 0:
    if min(s1) > min(s2):
        print('Ходит игрок 2')
    if min(s1) < min(s2):
        print('Ходит игрок 1')
        

def hod():
    while True:
        n = int(input())
        print(player1[n])
        for i in player2:
            if i[1] == player1[n][1] and i[0] > player1[n][0]:
                print(i, ' бьет ', player1[n])
                break
    
hod()

#hgjhk

print('d')