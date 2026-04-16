class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # assumptions:
            # there is always one solution
            # i and j shouldnt be equal 
            # find two values in the array that aren't equal which sum to the target number
            # the same number can be in the array more than once !
        
        # we could iterate through the whole list twice with brute force / n^2 time with an outer and inner loop
        # better idea is to split in half and work inward, actually -- that wont work

        # new idea: iterate through the loop once. on the current position, take the target value and 
            # subtract the current value we are at. take that answer and see if its in the list. if it is, return [min(a,b),max(a,b)]

        # issue is that i didn't realize the same number will be in the array more than once, so we returned the same value
            # we need a way to 

        # [5,2,4,5,5,5] - only ever looks forward... so make sure we don't think we have a match when
            # our i is the same as our pairing. if it is, then continue?


        i = 0
        for num in nums:
            poss_val = target - num
            if poss_val in nums:
                if nums.index(poss_val) != i:
                    return [min(i, nums.index(poss_val)),max(i, nums.index(poss_val))]
            i = i+1
        return False
        
    
        