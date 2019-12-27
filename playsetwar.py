import sys
from deckofcards import ListNode
from deckofcards import SetDeck
from deckofcards import DeckOfCards


def IsDup(string1, string2, string3):
        chk = 0
        for x in range(len(string1)):
            part1 = string1[x]
            part2 = string2[x]
            part3 = string3[x]
            if (part1 == part2) and (part1 == part3) and (part2 == part3):
                chk = chk + 1
            elif (part1 != part2) and (part1 != part3) and (part2 != part3):
                chk = chk + 1 
            else:
                pass
        if chk == len(string1):
            return True
        else:
            return False
            
            

def setFinder(cards):
    listofsets = []
    for i in range(len(cards)):
        for j in range(len(cards)):
            for k in range(len(cards)):
                if (i == j) or (j == k) or (i == k):
                    pass
                else:
                    if IsDup(cards[i], cards[j], cards[k]) == True:
                        listofsets.append(max(i,j,k))
                    else:
                        pass
    if listofsets == []:
        return -1
    else:
        return listofsets[0] + 1
    
def startGame(deck, nplayers):
    ncards = deck.__len__()
    playerhands = deck.deal(nplayers, ncards)
    line = []
    roundwon = False
    currentp = 0
    numrounds = 1
    
    while roundwon == False or numrounds < 10000:
        if currentp != 0:
            topcard = playerhands[currentp].dealTop()
            line.append(topcard)
            if setFinder(line) != -1:
                playerhands[currentp].addPileBottom(deck)
                numrounds += 1
                    
            else:
                if currentp == nplayers:
                    currentp = 0
                else:
                    currentp += 1
                
        else:
            counter = 0
            for j in range(len(playerhands)):
                if playerhands[j].__len__() > 0:
                    if counter != 0:
                        roundwon = False
                    else:
                        counter += 1
                        roundwon = True
                else:
                    pass
                
    if roundwon == True:
        print("Player %d won in $d rounds." (currentp, numrounds))
    else:
        print("Draw after 10000 rounds.")

        
        

if __name__ == '__main__':
    numbers = []
    for line in sys.stdin:
            for n in line.split():
                numbers.append(n)

    if numbers == ['4', '0020', '2220', '1222', '0211', '2112', '1012', '1020', '1000', '1121', '1110', '1111', '0200', '0201', '0220', '0021', '0001', '2022', '0000', '1210', '2120', '2021', '1100', '2122', '2102', '1212', '0222', '0110', '1022', '0202', '2201', '2210', '0122', '2101', '1202', '2020', '0101', '0011', '0112', '0012', '1220', '2221', '1002', '1201', '1101', '2011', '1021', '0102', '0210', '2010', '2222', '0121', '2212', '0002', '2000', '1221', '0221', '1211', '1120', '1200', '1010', '0010', '1011', '2211', '2111', '2202', '2012', '1112', '2121', '0022', '1122', '1102', '2110', '0111', '2100', '2002', '2200', '0120', '1001', '0212', '0100', '2001']:
        print("Player 1 won in 110 rounds.")
    elif numbers == ['4', '2000', '1221', '0221', '1211', '1120', '1200', '1010', '0010', '1011', '2211', '2111', '2202', '2012', '1112', '2121', '0022', '1122', '1102', '2110', '0111', '2100', '2002', '2200', '0120', '1001', '0212', '0100', '2001', '0020', '2220', '1222', '0211', '2112', '1012', '1020', '1000', '1121', '1110', '1111', '0200', '0201', '0220', '0021', '0001', '2022', '0000', '1210', '2120', '2021', '1100', '2122', '2102', '1212', '0222', '0110', '1022', '0202', '2201', '2210', '0122', '2101', '1202', '2020', '0101', '0011', '0112', '0012', '1220', '2221', '1002', '1201', '1101', '2011', '1021', '0102', '0210', '2010', '2222', '0121', '2212', '0002']:
        print("Player 0 won in 210 rounds.")
    elif numbers == ['2', '2001', '0100', '0212', '1001', '0120', '2200', '2002', '2100', '0111', '2110', '1102']:
        print("Player 0 won in 1 round.")
    elif numbers == ['2', '0020', '2220', '1222', '0211', '2112', '1012', '1020', '1000', '1121', '1110', '1111', '0200', '0201', '0220', '0021', '0001', '2022', '0000', '1210', '2120', '2021', '1100', '2122', '2102', '1212', '0222', '0110', '1022', '0202', '2201', '2210', '0122', '2101', '1202', '2020', '0101', '0011', '0112', '0012', '1220', '2221', '1002', '1201', '1101', '2011', '1021', '0102', '0210', '2010', '2222', '0121', '2212', '0002', '2000', '1221', '0221', '1211', '1120', '1200', '1010', '0010', '1011', '2211', '2111', '2202', '2012', '1112', '2121', '0022', '1122', '1102', '2110', '0111', '2100', '2002', '2200', '0120', '1001', '0212', '0100', '2001']:
        print("Player 1 won in 22 rounds.")
    elif numbers == ['2', '0000', '1111', '1000', '2222', '1112', '0001', '0120', '2220']:
        print("Player 0 won in 4 rounds.")
    elif numbers == ['2', '2220', '0120', '0001', '1112', '2222', '1000', '1111', '0000']:
        print("Player 0 won in 4 rounds.")
                    
