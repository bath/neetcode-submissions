class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a palindrome can be read forwards and backwards and is the same word

        # since we are basically putting a mirror in the word and making sure both sides are equal
            # it can be solved in a number of different ways
            # we can use two pointers
            # we can use a splitter then inverse one of the sides and compare equality
            # maybe a third solution?

        # the splitter with an inverse seems like a simpler code implementation

        # if its an even string then you just compare both halves
        # if its an odd string then you ignore the middle value and compare both halfs

        # need to clean the string first
        # make it lowercase and remove spaces

        s_smashed = s.replace(" ", "")
        s_lower = s_smashed.lower()
        # remove any non alphanumeric or 0-9
        s_fin = re.sub(r'[^a-zA-Z0-9]', '', s_lower)
        print('super clean')
        print(s_fin)

        if len(s_fin) % 2 == 0:
            # even string
            # millim <- length 6 so 6 / 2 = 3 which is mill so should be len(s) - 1 for the parting the two
            fh = s_fin[:(len(s_fin) // 2)]
            print("fh")
            print(fh)

            sh = s_fin[(len(s_fin) // 2):]

            print("sh")
            print(sh)

            return fh == sh[::-1]
        
        # otherwise its an odd length
        # wasitacar | o | racatisaw


        fh = s_fin[:(len(s_fin) // 2)]
        print("fh")
        print(fh)
        print(s_fin)

        sh = s_fin[(len(s_fin) // 2) + 1:]


        return fh == sh[::-1]

        
        print("sh")
        print(sh)
        print('mil')


        # racecar <- length 7
            #
        