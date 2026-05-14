class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # you go up right down and left only
        # do not go diagonally

        # base case - the island is empty?

        if not grid:
            return 0

        # we need to iterate over the entire grid one at a time

        # use a searching method to ensure, once we find a node, we trace it end to end

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                # is the current position already visited?
                # is the current position a 1?
                # if both pass, then we want to record this and explore
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    island_count += 1
                    # explore from this point
                    self.dfs(r, c, grid, visited)

        return island_count

    def dfs(self, r, c, grid, visited):
        # some kind of way to contain the working set we need to iterate on

        # dfs = stack
        # bfs = queue

        paths = [(r,c)]

        while paths:
            r,c = paths.pop()

            # look up down left and right
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            # look at each position
            # if that position has not been visited and is a 1 then we want to capture that too
            for rd, cd in directions:
                row = rd + r
                col = cd + c

                if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == "1" and (row, col) not in visited:
                    # in the grid
                    # is an island
                    # not yet visited

                    visited.add((row,col))
                    # island_count += 1
                    paths.append((row,col))
