class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotomic decreasing stack
        # only ever add things to the stack if it follows a rule
        # if it breaks the rule, then you pop until the rule is statisfied again
        # all the while during either operation you are keeping track of the positioning

        # core calculation for how many days a given position will take: current index minus how many we pop

        # initalize an empty output array and then add progressively

        n = len(temperatures)
        res = [0] * n
        stack = [] # (index, temp)
        # need to keep track of the length for some reason?

        for i, t in enumerate(temperatures):
            # some kind of while loop..?
            # we should add an item to the stack if it is equal or decreasing
            # if not... we should pop and add a calculated number of how many days that position has to the result array
            while stack and t > stack[-1][1]:
                j, temp = stack.pop()

                # current index - popped index = output value
                output_value = i - j

                res[j] = output_value

                # do something
            
            stack.append((i, t))
        return res