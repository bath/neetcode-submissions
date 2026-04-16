class Solution:
    # map reduce function?
    # probably a better / idotmatic way to do this
    def make_array_a_product(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product = product * num
        return product
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given an input array of numbers, produce an output array
        # the output array at any given position should be the product
        # of ALL other items in the input array. The catch is that
        # whatever position you pick in the output array it should
        # exclude the value of the same position in the input array

        # its kind of like an inverse mapping...

        # [A,B,C] <- input

        # [B*C, A*C, A*B] <- output

        # there is an algorithm here... how to decompose the 
        # more direct example above to figure that out ?

        # when constructing the output array, start on the input position
        # then take everything in the array EXCEPT that position and sum them
        # and push that value into the same spot in the output array

        # list comprehension? or something with the python array
        # [y:x:z]
        # could solve this with a double pointer? 
        # at the start you just get everything other than that
        # at the end you just exclude that one
        # anything in the middle of the array you use both sides
        # of wherever you are

        output_array = []

        # edge case: the start
        start_value = self.make_array_a_product(nums[1:])
        print('miller')
        print(start_value)
        
        output_array.append(start_value)

        # edge case: middle of array (every value except 0 and len()-1)
        for i in range(1, len(nums)-1):
            print('i is ')
            print (i)
            
            # first half
            fh = nums[:i]
            print('fh is')
            print(fh)
            # second half
            sh = nums[i+1:]
            print('sh is')
            print(sh)

            print('middle is')
            print(fh + sh)

            val = self.make_array_a_product(fh + sh)

            # num_pos_sum = 
            output_array.append(val)
            print('middle final val is ')
            print(val)
        
        # edge case: end of the array
        end_value = self.make_array_a_product(nums[:len(nums)-1])
        print('end val')
        print(end_value)

        output_array.append(end_value)

        return output_array



