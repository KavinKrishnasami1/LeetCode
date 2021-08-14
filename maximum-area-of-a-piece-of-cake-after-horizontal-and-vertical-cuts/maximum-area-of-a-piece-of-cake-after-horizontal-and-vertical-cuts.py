class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(h)
        horizontalCuts.append(0)
        horizontalCuts.sort()
        
        verticalCuts.append(w)
        verticalCuts.append(0)
        verticalCuts.sort()
        
        maxHeight = 0
        for i in range(len(horizontalCuts) - 1):
            height = horizontalCuts[i + 1] - horizontalCuts[i]
            if height > maxHeight:
                maxHeight = height
        
        maxWidth = 0
        for i in range(len(verticalCuts) - 1):
            width = verticalCuts[i + 1] - verticalCuts[i]
            if width > maxWidth:
                maxWidth = width
                
        return (maxHeight * maxWidth) % (10**9 + 7)