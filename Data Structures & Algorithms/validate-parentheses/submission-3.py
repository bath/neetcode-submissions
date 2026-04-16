class Solution:
    def isValid(self, s: str) -> bool:

        # only a valid string if for every open we have a close

        # seems that there is a symmetry in the string... can we just split the middle somehow and compare the two sides?

        # maybe put everything in a hash map?

        # we know the exact characters provided to us, should we use that info? or if we added new arbitrary symbols would that work too?

        # i think we have to have a detector...

        # start a stack and push each item in the string onto it linearly
            # when we see a close item, then start to pop and it must be its pairing 
            # if it isnt return false
            # if never returned false, return true


        # i feel like this is way easier if we just use two pointers...

        closing_items = [')', '}', ']']

        mappings = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }

        open_stack = []

        # also - since these are pairs we have to have a even number
        if len(s) % 2 != 0:
            return False

        should_pop = False

        # the stack is even length but incorrect ordering / pairing
        for item in s:
            if item in closing_items:
                should_pop = True
            else:
                should_pop = False
            
            if should_pop:
                if len(open_stack) == 0:
                    return False
                print(open_stack)
                
                popped_item = open_stack.pop()

                print(popped_item)
                print(item)
                print(mappings[popped_item])
                # do the closing sequence
                if mappings[popped_item] != item:
                    return False
                continue

            # otherwise its an opener and keep pushing
            open_stack.append(item)

        print(open_stack)
        return len(open_stack) == 0    
        