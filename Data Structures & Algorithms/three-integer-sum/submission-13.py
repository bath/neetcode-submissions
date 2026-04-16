class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # what three values sum to 0?

        # loop through using i


        # i + j + k = 0
        # j + k = -i

        # start at i and then j and k are bounded by the forward slice of the array

        sorted_nums = sorted(nums)
        output_array = []

        for i, i_num in enumerate(sorted_nums):
            if i_num > 0:
                # 
                break

            if i > 0 and i_num == sorted_nums[i - 1]:
                continue

            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                poss_answer = i_num + sorted_nums[l] + sorted_nums[r]

                if poss_answer > 0:
                    r = r - 1
                elif poss_answer < 0:
                    l = l + 1
                else:
                    output_array.append([i_num, sorted_nums[l], sorted_nums[r]])
                    l = l + 1
                    r = r - 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l = l + 1



        return output_array