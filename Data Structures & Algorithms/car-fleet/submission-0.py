class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # some kind of y = mx + b ?

        # for each + 1 advancement, we need to apply the speed to the position to give it an advance
        # so for a car at 3 with speed 4 and a target of 10, one advancement would be 7?
        # and 2 advancement would be 11
        
        # if the two lines intersect before the target then they are considered part of the fleet
        # otherwise if one makes it before then its its own fleet

        # can expand to multiple (5+) cars ... and each would have its own slope and we need to find when each makes a checkpoint
            # / is a grouping of cars

        # probably should be a while loop since we dont really know when they will finish. we can cacl ahead of time but tbh just run until were finish

        # while someones position isn't > target

        # do we need to loop or can we just apply a calculation to all and then find the groupings?

        # how do we determine the intersection point?

        # beacuse of the ordering ... we know that if a car "behind" reached the target position before any car ahead of it, it is considered part of the fleet

        # y = mx + b

        # given a position and speed, an item will be at target at P position with..
        # ( target - position ) / speed

        # 10 - 4 / 2

        # 6 / 2 = 3

        # at position 3 

        # use a stack to keep track of unique groupings

        pair = [[p, s] for p, s in zip(position, speed)]

        pair = sorted(pair) # we want to sort them because the pairs are actually given to us RANDOMLY ... not in a specific order 

        print(pair)

        stack = [] # return the length of this for our final answer

        for p, s in pair[::-1]: # go backwards because we want to 
            stack.append((target - p ) / s)
            
            # if there is something in the stack to compare against, then see if our current item would limit the stack head
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop() # remove the item from the stack because the other one is already covering it?

        return len(stack)


        