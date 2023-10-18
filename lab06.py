"""
Author:         Landon Thomas
Date:           10/5/23
Assignment:     Lab 06
Course:         CPSC1051
Lab Section:    004

CODE DESCRIPTION:
This is a program that plays blackjack amongst a number of players determined by the user. It uses 3 functions to do
so and declares a winner at the end. A tie is announced if two players both have the highest score.
"""

deck = [
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
    "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"
]
"""select the number of players to play with and validate"""
import random
print("Give me a seed:")
seed = int(input())
print("How many players would you like to play with?")
num_players = int(input())
while num_players <= 0:
    print("Please enter a value greater than 0: ")
    num_players = int(input())

"""define how to deal the deck of cards to each player"""
player_hands = []
def deal(num_players):
    for i in range(num_players):
        card1 = random.randint(0, 51)
        while player_hands.count(card1) > 0:
            card1 = random.randint(0, 51)
        card2 = random.randint(0, 51)
        while player_hands.count(card2) > 0:
            card2 = random.randint(0, 51)
        personal_hand = []
        personal_hand.append(deck[card1])
        personal_hand.append(deck[card2])
        player_hands.append(personal_hand)
        print(f"Player {i + 1}'s cards: ")
        print(player_hands[i])
        print(f"Acknowledge that you have seen your cards player {i + 1} by entering any key.")
        seen = input().split()
        while len(seen) != 1:
            print(f"Acknowledge that you have seen your cards player {i + 1} by entering any key.")
            seen = input().split()

"""define how to check if an Ace is 1 or 11"""
def check_ace(count, points):
    for hand in player_hands:
        for card in hand:
            if card == 'AH':
                count += 1
            elif card == 'AS':
                count += 1
            elif card == 'AD':
                count += 1
            elif card == 'AC':
                count += 1
        if count == 4 and (21 - points) >=14:
            points += 14
        elif count == 4 and (21 - points) < 14:
            points += 4
        elif count == 3 and (21 - points) >=13:
            points += 13
        elif count == 3 and (21 - points) < 13: 
            points += 3
        elif count == 2 and (21- points) >= 12:
            points += 12
        elif count == 2 and (21 - points) < 12:
            points += 2
        elif count == 1 and (21 - points) >= 11:
            points += 11
        elif count == 1 and (21 - points) < 11:
            points += 1

"""define how to get points for each player"""           
player_points =[0 for i in range(num_players)]
def points(player_hands):
    for i in range(num_players):
        points = 0
        for j in range(len(player_hands[i])):
            if player_hands[i][j] != deck[0] and player_hands[i][j] != deck[13] and player_hands[i][j] != deck[26] and player_hands[i][j] != deck[39]:
                if player_hands[i][j] == deck[9] or player_hands[i][j] == deck[10] or player_hands[i][j] == deck[11] or player_hands[i][j] == deck[12] or player_hands[i][j] == deck[22] or player_hands[i][j] == deck[23] or player_hands[i][j] == deck[24] or player_hands[i][j] == deck[25] or player_hands[i][j] == deck[35] or player_hands[i][j] == deck[36] or player_hands[i][j] == deck[37] or player_hands[i][j] == deck[38] or player_hands[i][j] == deck[48] or player_hands[i][j] == deck[49] or player_hands[i][j] == deck[50] or player_hands[i][j] == deck[51]:
                    points += 10
                elif player_hands[i][j] == deck[8] or player_hands[i][j] == deck[21] or player_hands[i][j] == deck[34] or player_hands[i][j] == deck[47]:
                    points += 9
                elif player_hands[i][j] == deck[7] or player_hands[i][j] == deck[20] or player_hands[i][j] == deck[33] or player_hands[i][j] == deck[46]:
                    points += 8
                elif player_hands[i][j] == deck[6] or player_hands[i][j] == deck[19] or player_hands[i][j] == deck[32] or player_hands[i][j] == deck[45]:
                    points += 7
                elif player_hands[i][j] == deck[5] or player_hands[i][j] == deck[18] or player_hands[i][j] == deck[31] or player_hands[i][j] == deck[44]:
                    points += 6
                elif player_hands[i][j] == deck[4] or player_hands[i][j] == deck[17] or player_hands[i][j] == deck[30] or player_hands[i][j] == deck[43]:
                    points += 5
                elif player_hands[i][j] == deck[3] or player_hands[i][j] == deck[16] or player_hands[i][j] == deck[29] or player_hands[i][j] == deck[42]:
                    points += 4
                elif player_hands[i][j] == deck[2] or player_hands[i][j] == deck[15] or player_hands[i][j] == deck[28] or player_hands[i][j] == deck[41]:
                    points += 3
                elif player_hands[i][j] == deck[1] or player_hands[i][j] == deck[14] or player_hands[i][j] == deck[27] or player_hands[i][j] == deck[40]:
                    points += 2
            else:
                check_ace(0, points)
        player_points[i] = points

"""define how to add a card to a player's hand"""
def add_card(player):
    new_card_num = random.randint(0, 51)
    new_card = deck[new_card_num]
    while player_hands.count(new_card) > 0:
        new_card_num = random.randint(0, 51)
    for i in range(num_players):
        if i == player:
            player_hands[i].append(new_card)

"""begin the actual game"""            
deal(num_players)
print("Now that everyone knows their cards, let's play!")

for i in range(num_players):
    print(f"Player {i + 1}'s cards:")
    print(player_hands[i])
    print(f"Player {i + 1} would you like to hit or stick?")
    decision = input().strip()
    while decision != 'hit' and decision != 'stick':
        print("Invalid input. Please enter either hit or stick: ")
        decision = input().strip()
    while decision == 'hit':
        add_card(i)
        points(player_hands)
        if player_points[i] > 21:
            print(player_hands[i])
            print(f"Player {i + 1} you have busted. Enter any key to acknowlege this.")
            busted = input().split()
            while len(busted) != 1:
                print(f"Player {i + 1} you have busted. Enter any key to acknowlege this.")
                busted = input().split()   
            player_hands[i] = [0,0]
            player_points[i] = 0
            break 
        else:
            print(f"Player {i + 1}'s cards:")
            print(player_hands[i])
            print(f"Player {i + 1} would you like to hit or stick?")
            decision = input().strip()
            while decision != 'hit' and decision != 'stick':
                print("Invalid input. Please enter either hit or stick: ")
                decision = input().strip()
    if decision == 'stick':
        continue

for i in range(num_players):
    if player_hands[i] == 0:       
        print(f"Player {i + 1} has busted.")

"""determine winner"""
max_points = max(player_points)
if max_points > 0:     
    if player_points.count(max_points) == 2:
        winner1 = player_points.index(max_points)
        winner2 = player_points.index(max_points, winner1 + 1)
        print(f"Players {winner1 + 1} and {winner2 + 1} tied for the highest score of {max_points}")
    elif player_points.count(max_points) == 1:
        winner = player_points.index(max_points)
        print(f"Player {winner + 1} got the highest score of {max_points}.")
else:
    print("Nobody won.")


    
