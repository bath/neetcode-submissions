class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # similar to a binary search of a list, find if a target exists in a matrix m*n size
        
        # previous solution wasn't really log(mn) time... it was o (m) + log (n) since it would travese the whole row
            # the only way you can get log(X) time is to cut the sizing of the row through some kind of searching pattern... not iterating through all the options
    
        # pretend its a giant sorted list.. the fact the single list is in multiple sub arrays is just an annoyance not really a problem

        # how to go through a 2d array .. ?

        # some kind of while loop instead of for ... although for loop could work because we know it should be ... half the length of the array?

        # while i think is easier to keep track / better abstraction?
        # oh... we might not always need to take n/2 times. we could cut out really early and should if the conditions are sorted right

        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        r = (rows * columns) - 1

        while l <= r:

            # middle index in a 2d array?
            # aka the middle value of two numbers... so add them together and cut in half to find the midpoint
            mid = (l + r) // 2

            # find where that number actually is in a 2d array
            # to find which row you would need to know how many items per sub array...
            # matrix would be 
            #   column
            # [[1,2,3], row
            #  [4,5,6],
            #  [7,8,9]]        

            row = mid // columns
            # how tf do you determine the column
            # divide to determine which bucket, MODULUS will determine where in the bucket (offset)
            column = mid % columns

            mid_val = matrix[row][column]

            if mid_val > target:
                # mid is too big
                r = r - 1 # or should be the middle of the r and mid??
            elif mid_val < target:
                # mid dis too small
                l = l + 1
            else:
                return True
        
        return False

        






