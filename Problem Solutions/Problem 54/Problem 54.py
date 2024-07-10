#Problem 54 Poker

#Note: this is a very hacky solution but wouldn't work in all edge cases
#(Because we assumed that given the criteria on the page)


#We first buil a hand classifier
#The input is a length-5 list of lists of length 2, representing the cards
#The first value of each list of length 2 is the value, the second is the suit
#We return a list of length three: [hand_value, max_value,highest_card]
#hand_value is the ranking of the card (i.e. pair, flush. etc.)
#max_value is the highest_value to break ties in case the hands have the same rank
#highest_card is the highest card in the hand: this eventually breaks ties if necessary
def classify_hand(hand):
    hand_value = 0 #We start by assuming that there is no pattern
    values = sorted([card[0] for card in hand]) #We cut out a separate list of values
    highest_card = max(values)
    max_value = highest_card

    #Now, we create a list which will help us find pairs
    pair_finder = []
    for i in range(5):
        if i ==0:
            pair_finder.append(1)
        else:
            if values[i] == values[i-1]:
                pair_finder[-1] += 1
            else:
                pair_finder.append(1)
    
    is_straight = False

    if max(pair_finder) == 4:
        hand_value = max(hand_value,7) #We have a four of a kind
        max_value = values[2] #We know this will be in the four of a kind
    elif max(pair_finder) == 3:
        max_value = values[2] #We know this will be in the three of a kind
        if min(pair_finder) == 2:
            hand_value = max(hand_value,6)
        else:
            hand_value = max(hand_value,3)
    elif max(pair_finder) == 2:
        if len(pair_finder) == 3: #This means it is two pairs
            hand_value = max(hand_value,2)
            max_value = values[3] #We know this will be in the higher value
        else:
            hand_value = max(hand_value,1)
            max_value = values[pair_finder.index(2)]
    else:
        #We now check for a straight:
        is_straight = bool(max(values)-min(values) == 4)
    
    #We check for a flush
    is_flush = bool(all(card[1] == hand[0][1] for card in hand)) 
    
    if is_straight:
        if is_flush:
            hand_value = max(8,hand_value) #Then a straight (or royal) flush 
            max_value = highest_card 
        else:
            hand_value = max(hand_value,4)
            max_value = highest_card #A regular straight
    else:
        if is_flush:
            if hand_value <= 3:
                max_value = highest_card
            hand_value = max(hand_value,5) #a flush (or possibly a four of a kind/full house)
    return [hand_value,max_value,highest_card]


#This function takes the initial raw input and coverts it into something that the 
#classify_hand function can work with
def convert_hand(raw_hand):
    hand = []
    i = 0
    while i< len(raw_hand):
        card_value = raw_hand[i]
        i += 1
        #casework to make all of the cards integer values between 2 and 14
        if card_value == "T":
            card_value = 10
        if card_value == "J":
            card_value = 11
        if card_value == "Q":
            card_value = 12
        if card_value == "K":
            card_value = 13
        if card_value == "A":
            card_value = 14
        else:
            card_value = int(card_value)
        #Now we add the suit
        suit_value = raw_hand[i]
        i+= 2
        hand.append([card_value,suit_value])
    return hand


#The wrapper function
def find_winner(hands):
    #This reads from the file line
    raw_hand_1 = hands[:14]
    raw_hand_2 = hands[15:29]
    #Then we convert
    hand1 = convert_hand(raw_hand_1)
    hand2 = convert_hand(raw_hand_2)
    #Finally, we classify both hands, and use lexographic comparison to see which hand wins
    return int(bool(classify_hand(hand1)>classify_hand(hand2))) 


with open('Problem54File.txt','r') as f:
    line = f.readline()
    player_1_win = 0 #measuring the number of player 1 wins
    while line!= '':
        player_1_win += find_winner(line)
        line=f.readline()
    
print("The answer is", player_1_win)
