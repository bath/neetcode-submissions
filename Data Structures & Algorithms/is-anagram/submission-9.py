class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given a string which you cut in half, are both sides equal?
        # go to the middle of the string, split it, reverse the right side. then ask: are these two completely equal?
            # edge case: if its an odd number length then remove the middle value / toss it out
        # im sure there is some kind of python .reverse() method you can slap onto the string but thats lazy
        # we can't use a hashmap because the order matters... we need to be careful how we pluck
        # alternative solution is to have two pointers moving towards the middle and making sure each character is equal...
        # probably a slightly quicker solution on average ?
        # also can have the quick exit if the strings aren't equal
            # a string is an anagram if:
                # both strings are equal length
        
        # i re-read the instructions and now see the 2nd string is already reversed. so just use a for loop and one starts 
            # at front and one at back. if they aren't always equal then return false. only way to guarantee true is O(n) time and O(1) space
        # i = 0
        # j = len(t)-1
        # if len(s) != j+1:
        #     return False
        # for char_a in s:
        #     if s[i] != t[j]:
        #         return False
        #     j = j-1
        # return True

        # oops i solved the wrong problem
        # make two maps with space of O(n) and time O(1) i think?
        # if the set counts aren't equal then its a fail
        
        if len(s) != len(t):
            return False

        # do some kind of mapping taking each one in the first and finding it in the next and then removing from the list?
        for char in s:
            pos = t.find(char)
            if pos == -1:
                return False
            t = t[:pos] + t[pos+1:]
        print(s)
        print(t)
        return True

        # s_dic = {}
        # t_dic = {}
        # i = 0
        # for char in s:
        #     if s_dic[s[i]]:
        #         s_dic[s[i]] += 1
        #     if t_dic[s[i]]:
        #         t_dic[s[i]] += 1    
        
        


        