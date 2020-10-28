# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:27:48 2020

@author: DavidLynch
"""

class Solution:
    def longestStrChain(self, words):
        #below is the array where we will store each words' maximum chain length
        maxlengths = {}
        #below variable stores our current highest maximum, initiated at 1 because that is the starting value given
        finalmax = 1
        
        words = sorted(words, key=len) #sorting through the words because it'll match index up to length
        
        #iterating through the words given:
        for currentword in words:
            #setting the current spot equal to 1, since we know this is the minimum total number of chains
            maxlengths[currentword] = 1
            #looping through the length of the current word
            for i in range(len(currentword)):
                #subsetting this specific word to a different combination
                subsetted_word = currentword[:i] + currentword[i + 1:]
                #is the above made word in the subset of words?
                if subsetted_word in words:
                    #if yes, find the maximum between the subsetted word's position (the length) + 1 or what we currently have as the maximum in that spot
                    maxlengths[currentword] = max(maxlengths[subsetted_word] + 1, maxlengths[currentword])
                    
                    #set finalmax to either the maximum length at that current word or the already existing finalmix
                    finalmax = max(finalmax, maxlengths[currentword])

        return finalmax
