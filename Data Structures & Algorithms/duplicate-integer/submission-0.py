class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a few different approaches:
            # 1. iterate / brute force and keep track of everything - O(n^2)
                # 1a. iterate over every item and go through every one to find if it appears again
            # 2. hash map, same as above but more fancy?
            # 3. probaby a one liner ...
            # 4. some kind of pythonic way to do a list comprehension i think it is?
        my_map = {}
        for num in nums:
            if num in my_map:
                return True
            else:
                my_map[num] = True
        return False