class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the list is in ascending order (sorted)

        # because of this we can use binary search to reduce overall time complexity

        # naive - brute force through the list and find the minimum value in the array
            # better - binary search through the list to identify where the minimum value is
                # which will take n/2 time at worst

        # better - the only input we have is the array. there isn't a good way to instantly know
            # how many times the array has been rotated.
            # we should be able to determine this when the right is lower than the left
            # e.g. [..., 10, 1, 2, ...]
                #.       L, ..., R
        
        # always start the L and R pointers at the beginning and end of the array

        left, right = 0, len(nums) - 1

        # edge case detection before looping - is the left value already the minimum?

        if nums[left] < nums[right]:
            return nums[left]

        # otherwise we need to loop to find the item

        while left < right:

            # two modes:
                # 1. searching for minimum
                # 2. on top of the minimum
            
            # 1. searching
            # get the middle between left and right and determine which pointer we need to move to the middle

            delta = right - left

            middle = left + (delta // 2)

            left_val = nums[left]
            right_val = nums[right]
            middle_val = nums[middle]

            # # not sure about = sign
            # if left_val > middle_val:
            #     # minimum is somewhere in here
            #     right = middle
            # elif right_val < middle_val:
            #     left = middle + 1
            # else:
            #     return left_val

            if middle_val > right_val:
                left = middle + 1
            else: # otherwise middle_val <= right_val
                right = middle

        return nums[left]

        # EDIT: upon a single evaluation of the left and right you should be able to determine which
            # side has lies the minimum value
        # compare the middle value to the two pointers... if there is a hiccup in the ordering
            # that must mean the hiccup is where we want to go next
        

        
# Input: nums = [6, 1, 2, 3, 4, 5]

# Output: 1
        
    











