# In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

# Initially, all the cards start face down (unrevealed) in one deck.

# Now, you do the following steps repeatedly, until all cards are revealed:

# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.

# The first entry in the answer is considered to be the top of the deck.

class Solution(object):
    
    
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        temp = [deck[-1]]
        i=2
        while i!=len(deck)+1:
            z = [temp.pop()]
            z.extend(temp)
            temp = z
            x = [deck[-i]]
            x.extend(temp)
            temp = x
           
            i+=1
     
        return temp