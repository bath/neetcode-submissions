class Solution:

    def encode(self, strs: List[str]) -> str:
        # given a list of strings, make it a single string to be encoded
        # could naively iterate over the list in a for loop... but is there a way that is more 
            # efficient to pluck each item out and do something with it?
                # like a map function?
        # like list comprehension or map?
        # encoded_string = ""
        # encoded_string = map(lambda x: x + "," + encoded_string, strs)
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + "OMFG" + s 
        
        print('miller')
        print(encoded_string)
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        # string with `,` in it... split on those
        print('decocer')
        value = s.split("OMFG")
        # drop the last one it will always be empty
        value.pop(0)
        print(value)
        return value