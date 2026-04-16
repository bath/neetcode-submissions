class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # example is 6 x 6 which makes it 36 which is max

        # since we are trying to maintain the maximum of a bunch of computations it sounds like this is a heap solution?
        # but i know we are in the "two pointers" section .... so wtf?

        # we should probably just pluck out the largest numbers and then multiply the lowest of the two by the distance from each other
        # that would be the brute force solution... maybe not starting at the largest tho. and it would be n^2 i think?

        # probably a solution that exists that is O(n) ?
        # how can you go, in a single loop of each, to create the area?
            # maybe its like the previous issue .. product of n spot or something like that?

        # maybe you start on the edges and just keep looking ahead? and if there is a next one that is better its like buble sort where you
            # keep moving?
                # problem: if there is an insane answer in the center how will you ever know?
                # maybe just keep moving the posts and check anyways... ? so you don't stop early?

        # we know the formula is d x min(l,r) = area
        
        max_height = 0
        l, r = 0, len(heights) - 1
        for i, num in enumerate(heights):

            print('DASH DASH DASH')
            print('new loop')
            print('l and r are ', l,r)
            print('heights l and r are ', heights[l], heights[r])

            curr_height = (r - l) * (min(heights[l], heights[r]))
            print('r - l is ', r - l)
            print('min is ', min(heights[l], heights[r]))
        

            print('curr height is ', curr_height)

            if curr_height > max_height:
                max_height = curr_height

            # and loop pointers no matter what?
            if heights[l] <= heights[r]:
                # move the l forward
                l = l + 1
            elif heights[r] < heights[l]:
                # move the r backward
                r = r - 1


        return max_height
        