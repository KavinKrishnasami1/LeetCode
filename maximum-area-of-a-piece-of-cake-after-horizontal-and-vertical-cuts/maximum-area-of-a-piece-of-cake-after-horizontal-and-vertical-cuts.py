class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        
        maxHoriz = 0
        for i in range(len(horizontalCuts) - 1):
            horiz = horizontalCuts[i + 1] - horizontalCuts[i]
            if horiz > maxHoriz:
                maxHoriz = horiz
        
        maxVert = 0
        for i in range(len(verticalCuts) - 1):
            vert = verticalCuts[i + 1] - verticalCuts[i]
            if vert > maxVert:
                maxVert = vert
                
        return (maxHoriz * maxVert) % (10 ** 9 + 7)