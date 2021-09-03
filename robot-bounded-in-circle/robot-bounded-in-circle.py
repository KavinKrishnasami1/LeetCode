class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        
        for char in instructions:
            if char == 'G':
                x += dx
                y += dy
            elif char == 'L':
                dx, dy = -dy, dx
            elif char == 'R':
                dx, dy = dy, -dx
                
        return (x == 0 and y == 0) or (dy != 1)