# 735. Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            while stack and stack[-1]>0 and ast<0:
                if abs(ast) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast)
        return stack

