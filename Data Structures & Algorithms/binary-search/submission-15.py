class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # go up and down the stack, cutting in half each time

        # same calc each time... look at middle item, is it less? is it more? is it equal?

        # if equal, return the current position
        # if none, then return -1

        # define the bounds which will move dynamically
        l = 0
        r = len(nums) - 1 
        # last item in the list with a 0 index start

        while l <= r:
            # while the two arent equal there is still a space / gap aka something we can search
            mid = r - l // 2
            curr = nums[mid] # value of concern this round

            # print all vars
            print('start')
            print(l)
            print(r)
            print(mid)
            print(curr)
            print(target)


            if curr < target:
                # pull the left pointer higher
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                return mid
        return -1

