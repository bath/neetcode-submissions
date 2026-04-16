class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given a list of nums and an int k, return the k most frequent value(s) in nums

        # hmm. for loops seems like it could work, but probably not idea.
        # maybe a hashmap in combination of a for loop? we go through the list and 
            # put a number of occurances for each item.
        counted_nums = Counter(nums) # maybe this should be converted into a touple? probably doesnt make sense ... just sort it?
        output_list = []
        for i in range(k):
            most_common_value = max(counted_nums, key=counted_nums.get)
            output_list.append(most_common_value)
            counted_nums.pop(most_common_value)
        # print(highest_keys)
        return output_list

        # how to sort / get the most frequent numbers in a dict?
