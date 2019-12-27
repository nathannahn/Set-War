class ListNode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class DeckOfCards:
    
    def __init__(self, L = None):
        self.head = None
        self.tail = None
        self.length = 0

        if L:
            for item in L:
                self.addBottom(item)
                
    def dealbetween(self, item, before, after): 
        node = ListNode(item, before, after)
        if after is self.head:
            self.head = node
        if before is self.tail:
            self.tail = node
        self.length += 1

    def remove(self, node):
        before, after = node.prev, node.link
        if node is self.head:
            self.head = after
        else:
            before.link = after
        if node is self.tail:
            self.tail = before
        else:
            after.prev = before
        self.length -= 1
        return node.data
                
    def dealTop(self):
        return self.remove(self.head) 

    def dealBottom(self):
        return self.remove(self.tail)

    def addTop(self, card):
        self.dealbetween(card, None, self.head)

    def addBottom(self, card):
        self.dealbetween(card, self.tail, None)
        
    def addPileTop(self, pile):
        old = self.head
        new = pile.head

        if old is None:
            self.head = pile.head
            self.tail = pile.tail
            self.length = pile.length
        else:
            pile.tail.link = old
            self.head = new
            self.length = self.length + pile.length
            
        pile.length = 0
        pile = None
        
        return self    
            
    def addPileBottom(self, pile):
        old = self.tail
        new = pile.tail

        if old is None:
            self.tail = pile.tail
            self.head = pile.head
            self.length = pile.length
        else:
            pile.head.prev = old
            old.link = pile.head
            self.tail = new
            self.length = self.length + pile.length

        pile.length = 0
        pile = None
        
        return self
        
    def isEmpty(self):
        if self.length == 0:
            return True
            return False
        
    def __len__(self):
        return self.length

    def deal(self, nplayers, ncards = None):
        playerhand = []
        for j in range(nplayers):
            playerhand.append(DeckOfCards())
            
        if ncards is None:
            for i in range(self.__len__()):
                playerhand[i % nplayers].addTop(self.dealTop())
        else:
            for i in range(ncards):
                playerhand[i % nplayers].addTop(self.dealTop())    

        return playerhand

class SetDeck(DeckOfCards):
    def __init__(self, cards):
        DeckOfCards.__init__(self, cards) 
    
