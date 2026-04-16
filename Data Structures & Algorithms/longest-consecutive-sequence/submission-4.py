class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # output a single number that represents the longest consecutive sequence in a provided
            # list

        # theres no way to know this solution without observing every item
            # the only possible optimization is if there are fewer values left in the
            # list than the current longest sequence (which doesn't really change the t/s complexity)

        # So.. solution is O(n) for time and space (no way to simplify / reduce by some factor)

        # possible solution: create an unknown number of stacks
            # start with 1 stack, keep pushing until the current number is less than the head
                # if that happens then create a new stack
                # and save the value into a list
            # at the end of iterating report the max of the sequence list
        
        # max_sequence = 0
        # current_list = []

        # for num in nums:
        #     if current_list == []:
        #         # always append the value
        #         current_list.append(num)
        #         continue
            
        #     # the last (biggest) value in the 
        #     if current_list[len(current_list)-1]


        # FUCK i misunderstood what the question was
        # given a list of nums, give an int that represents the longest chain of ints that 
            # increase strictly by 1 each time

        # duplicate values can be removed / ignored
        
        # algo:

        # return 0 if the list is empty
        # keep a global max_sequence
            # sort the input array
            # loop over each item in the list
            # start a new local sequence count
            # init the start by always saying 1 if the list isn't empty and the local sequence is 0
            # after the 1st item in the list then compare to the previous and if its strictly
                # greater than 1 then ++ the local count
            # if it passed then replace the max with the local if local > max
            # if it didn't then reset the local sequence

        if nums == []:
            return 0
        
        max_sequence = 0
        local_sequence = 1
        sort_uniq_nums = list(sorted(set(nums)))
        print("sort uniq")
        print(sort_uniq_nums)
        for i, num in enumerate(sort_uniq_nums):

            print("inside for")
            print(i,num)

            # print("middle")
            # print(sort_uniq_nums[i-1]+1 == num)
            # print(sort_uniq_nums[i-1])
            # print(num+1)

            # if seq is 0 that means we just busted or at start of array
            if sort_uniq_nums[i-1]+1 == num :
                # print("middle")
                # print(sort_uniq_nums[i-1] == num + 1)
                # print(sort_uniq_nums[i-1])
                # print(num+1)
                local_sequence += 1
                print("added to local sequence")
                print(local_sequence)
            else:
                local_sequence = 1

            print("after eval")
            print(local_sequence)

            # i think we always want to set max if local > ? 

            if local_sequence > max_sequence:
                max_sequence = local_sequence

            # how to figure out the start of the sequence?
            # to skip the first or not?


        return max_sequence










