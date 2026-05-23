class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated a max of n times

        # O(n) would be to just go over each of the values in the list and return the smallest
        # O(log(n)) would mean that we cut the time in half or faster

        # fastest sort algos are O(nlogn), but since we know there is some kind of 
            # sort, just sliced incorrectly, we can assume once we find that rotation
            # we can rapidly find the smallest value in the list

        # we should use two pointers.
            # one starts at the beginning of the list
            # the other starts mid way though the list
            # whichever value is smaller, then we want to 


        # problem:
            # [45, 46, 44, 3, 4, 5, 6, 7, 8]
            # goes to 45 and 46
            # so go "left" of 45? 
            # aka the mid point between end of list and middle?
            # 

        # over complicating... just find where the rotation starts / ends and then sort that slice

        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                # already sorted
                result = min(result, nums[l])
                break
            
            # otherwise its not sorted so we need to find a new mid point
            middle = (l + r) // 2

            result = min(result, nums[middle])

            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1

        
        return result











