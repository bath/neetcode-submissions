class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # lock, 4 wheels ... ?
            # each wheel has 10 slots
        # sounding like a probability problem... 

        # its infinite / wraps around

        # you can only turn the wheel one time per move (either way?)

        # deadends - avoid cases

        # a node or state is the current reading of a lock
        # each wheel has only 2 options / edges
            # up or down
        # up or down is a movement that we register and return

        # BFS since we need to know all options at a poition 
            # 4 * 2 = 8 possible moves at a given combination
                # HINT: create a helper method to determine what these values are
        # BFS uses queues, 

        # base case
        if target == "0000":
            return 0
        
        if "0000" in deadends:
            return -1

        # assume the initial state starts at "0000"

        start = "0000"

        q = collections.deque()
        q.append((start, 0)) # the combinations and then the number of moves we've mad so we can compare them
        visited = set([start]) # we dont need number of moves in the visited, just the combination to keep track of

        # while there is work todo:
        while q:
            curr_comb, turns = q.popleft()

            if curr_comb == target:
                return turns

            # if its not a hit then we want to look at our next possible options and add each to the queue
            for combo in self.combos(curr_comb):
                if combo not in visited and combo not in deadends:
                    visited.add(combo)
                    q.append((combo, turns + 1))
            
            # what to do with deadends?
        
        return -1

    def combos(self, curr_comb):
        # up or down for each one
        # its a string

        combos = []

        for i in range(4): # starts at 0 and goes to 3
            wheel = int(curr_comb[i])

            # can go up one or down one...
                # the edge case here is 0 and 9
                    # all the inbetween values 2 - 8 are safe from either operation overflowing
            
            # define the moves
            moves = [-1, 1]

            for move in moves:
                # get the up and down of the current int
                digit = wheel + move
                new_combo = curr_comb
                if digit == -1:
                    # bind to 9
                    digit = 9
                elif digit == 10:
                    # bind to 0
                    digit = 0

                new_combo = curr_comb[:i] + str(digit) + curr_comb[i + 1:]
                combos.append(new_combo)
        return combos
                    



