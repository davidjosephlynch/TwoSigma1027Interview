class Solution:
    def longestStrChain(self, words):
        #below is the array where we will store each words' maximum chain length
        maxlengths = {}
        #below variable stores our current highest maximum, initiated at 1 because that is the starting value given
        finalmax = 1
        
        words = sorted(words, key=len) #sorting through the words because it'll match index up to length
        
        #iterating through the words given:
        for currentword in words:
            #setting the current spot equal to 1, since we know this is the minimum total number of chains (given)
            maxlengths[currentword] = 1
            #looping through the length of the current word (ie each possible combination/length)
            for i in range(len(currentword)):
                #subsetting this specific word to a different combination
                subsetted_word = currentword[:i] + currentword[i + 1:]
                #is the above 'subsetted word' in the dictionary of words?
                if subsetted_word in words:
                    #if yes, find the maximum between the subsetted word's position (the length) + 1 or what we currently have as the maximum chain length for the current word
                    maxlengths[currentword] = max(maxlengths[subsetted_word] + 1, maxlengths[currentword])
                    
                    #set finalmax to either the maximum length at that current word or the already existing finalmax
                    finalmax = max(finalmax, maxlengths[currentword])

        return finalmax
