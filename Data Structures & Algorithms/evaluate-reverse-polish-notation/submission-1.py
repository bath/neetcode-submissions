class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # you can pull the items from the list backwards (or forwards?) to always have an X and a Y then the operator

        # so a tuple is alwasy X,Y,operator

        # i could diagram this out easier by drawing lines from the center... lets just calc in place so we    
            # hit an X and Y, then user the operator
            # take that result, and apply to the next item and operator
            # continue until the list is empty

        working_stack = []
    
        for t in tokens:
            # keep appending until we get to an operator (then act on the last two items in the stack)
            if t == '+':
                working_stack.append(int(working_stack.pop()) + int(working_stack.pop()))
            elif t == '-':
                a,b = int(working_stack.pop()), int(working_stack.pop())
                working_stack.append(b - a)
            elif t == '*':
                # print(working_stack)
                working_stack.append(int(working_stack.pop()) * int(working_stack.pop()))
            elif t == '/':
                a,b = int(working_stack.pop()), int(working_stack.pop())
                working_stack.append(b / a)
            else:
                working_stack.append(t)
            print(working_stack)
        return int(working_stack[0])
