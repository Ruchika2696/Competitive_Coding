# You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

# Example 1:

# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: "AAABBC"
# Output: 188
 

# Note:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

from itertools import permutations
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        myPermutations = set()
        for l in range(1,len(tiles)+1):
            for p in permutations(tiles,l):
                myPermutations.add(p)
        return len(myPermutations)



        ####################################################################################################################
        								##FAST SOLUTION
        ####################################################################################################################

from itertools import permutations
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count=0
        myPermutations = {}
        # myPermutations = set()
        for l in range(1,len(tiles)+1):
            for p in permutations(tiles,l):
                if p not in myPermutations:
                    myPermutations[p]=None
                    count+=1
                # myPermutations.add(p)
        return count
        
