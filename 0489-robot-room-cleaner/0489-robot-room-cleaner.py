# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())
    
    def dfs(self, robot, x, y, xDirection, yDirection, visited):
        robot.clean()
        visited.add((x, y))
        
        for k in range(4):
            neighborX = x + xDirection
            neighborY = y + yDirection
            
            if (neighborX, neighborY) not in visited and robot.move():
                self.dfs(robot, neighborX, neighborY, xDirection, yDirection, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            xDirection, yDirection = -yDirection, xDirection