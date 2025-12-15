class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start_pos, cur_pos = [0, 0], [0, 0]
        directions = {
            'U': (-1, 0),
            'D': (1,0),
            'L': (0,-1),
            'R': (0,1)
        }

        for move in moves:
            r, c = directions[move]
            cur_pos = [cur_pos[0] + r, cur_pos[1]+c]

        if cur_pos == start_pos:
            return True
        return False

print(Solution().judgeCircle("UD"))
print(Solution().judgeCircle("LL"))
