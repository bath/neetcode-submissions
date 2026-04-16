class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solved this earlier with a Counter (aka take a list turn it into a dict with char as key and count of char as value)

        # for a list of strings, make sub lists for all strings that are anagrams
        # on initial reading here, seems like it should have a pretty similar solution for the previous anagram?
        # make a Counter for each ... then go through each dict and compare to each other? if === then put into a list together / append?

        # i think you need to "Counter" each of the strings in the list then go through the Counter list again and compare them all?
        # not sure how to avoid going over the list twice / doing it in memory? should be able to i would think though...

        if len(strs) < 2:
            return [strs]

        # list of all the dicts / counters to compare current string to past ones
        list_of_counters = []

        # if there is a match, we need to know what strings in the OG list to group together
        # should we create a secondary structure to hold the mapping of the Counter to where it is in the output array?
            # i think this is the only way forward i have for now
        mapping_dict = {} # key is the index of `strs` and value is the index of the output array

        output_array = []

        i = 0
        for string in strs:
            counter = Counter(string)
            if counter in list_of_counters:
                # we know the current string has a match to a previous string...
                
                # find the appropriate output subarray using out mapping_dict
                # since list of counters is always added we know the position in list_of_counters is the same as the OG strs
                index = list_of_counters.index(counter)
                output_array_location = mapping_dict[index]
                output_array[output_array_location].append(string)

                # update the mapping_dict after
                mapping_dict[i] = index

                # add this last so we don't interrupt out previous index find
                list_of_counters.append([Counter(string)]) # i think we need to could keep track of it in the counter list?


            else:
                # otherwise - its something new and needs its own distinct sub array
                # create it in a new sub list?
                list_of_counters.append(Counter(string))

                # create new subarray in output array
                output_array.append([string]) # its the last item in the array

                # update the mapping array in case a future Counter matches
                mapping_dict[i] = len(output_array) - 1
            i = i + 1

        print(list_of_counters)
        print("newline")
        print(mapping_dict)
        print("another one")
        print(output_array)
        return output_array

        # figured out after the fact we should just sorrt the list / compare all the strings but thats boring