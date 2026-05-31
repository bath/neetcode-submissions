class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # similarly, find the longest sequence until the start character repeats

        # brute force solution is to iterate over the list and then reset the R back to L + 1 ... but thats n2 time..
        # we should be able to solve this in O(n) time

        # we need to create a substring array that we can just continually build. keep the max substring when we find a violation

        # use a set for the working substring. gives you instant lookup time

        substr = set()
        l = 0
        maxS = 0

        for r in range(len(s)):
            # if the item is in the set we need to: remove the FIRST occurance, add back to end, and shift pointer?
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            maxS = max(maxS, r - l + 1)
        
        return maxS