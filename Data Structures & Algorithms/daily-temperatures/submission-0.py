class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotomic decreasing stack
        # only ever add things to the stack if it follows a rule
        # if it breaks the rule, then you pop until the rule is statisfied again
        # all the while during either operation you are keeping track of the positioning
        
        res = [0] * len(temperatures) # we always start with 0s, and add as needed
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

