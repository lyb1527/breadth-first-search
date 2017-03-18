'''
Given a 2D grid, each is either a wall 2, a zombie 1, or people 0.
zombies can turn the nearest people(up/down/left/right) into zombies every day.
but cannnot through wall. how long will it take to turn all people into zombies?
Return -1 if cannot turn all people into zombies

Example
Given a matrix:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0

return 2
'''

class Solution:
    # @param, a 2D integer grid
    # @return, an integer

    def zombie(self, grid):
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        if m == 0:
            return 0

        q = []
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    q.append((i, j))

        d= [[0, -1], [0, 1], [-1, 0], [1, 0]]
        days = 0
        while q:
            days += 1
            new_q = []
            for node in q:
                for k in xrange(4):
                    x = node[0] + d[k][0]
                    y = node[1] + d[k][1]
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 0:
                        grid[x][y] = 1
                        new_q.append((x, y))
            q = new_q

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    return -1

        return days - 1
