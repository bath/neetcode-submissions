class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given a target int, what two indicies in the provided array have numbers that SUM to the target?

        # maybe some kind of dynamic programming thing?
        # other solution types... ? 
        # req: always put index 1 and then index 2 in the return array
        # req: there is always only one valid solution

        # its kind of just a simple math problem.. ? 
        # given a number we want to sum to - what two values in a handful of numbers
            # can be used to get to said number?

        # i think i can only do this in O(n) time? 
        # loop through the array, subtract each one onto the target and see if that value is in
            # the array that isn't the current position?
        
        # maybe i should cast to a set? it looks like the question states the array is non decreasing.. 
            # so does that mean it can have 6 1's? you may not use the same element twice???

        # i was going to cast to a set but theres duplicate numbers.. so the specific position matters too
            # not just the numbers matching

        # so i guess im going with the dumb solution rather than something more ... insufferable

        first_index = 0
        second_index = 1

        for i, num in enumerate(numbers):
            # local copy of the array except for mine ?
            # have to do some bullshit to replace mine to make sure we don't grab it

            first_index = i
            
            loc_copy = numbers
            loc_copy[i] = "MILLA"
            poss_other = target - num

            if poss_other in loc_copy:
                second_index = loc_copy.index(poss_other)
                return [first_index+1, second_index+1]

            



        