class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        dx, dy = 0, 1
        
        for letter in instructions:
            if letter == "G":
                x += dx
                y += dy
            elif letter == "L":
                dx, dy = -dy, dx
            elif letter == "R":
                dx, dy = dy, -dx
                
        return (not x and not y) or (dy != 1)