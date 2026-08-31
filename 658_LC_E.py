# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cord = [0, 0] # [x,y]
        movement = {'U':1, 'D':-1, 'R':1, 'L':-1}
        for move in moves:
            if move in "UD":
                cord[1] += movement[move]
            else:
                cord[0] += movement[move]
        return True if cord[0]==0 and cord[1]==0 else False
    
#---------Other Solution-------------#

class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')