class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for pair in points:
            distance = math.sqrt((pair[0] ** 2) + (pair[1]**2))
            distances.append(distance)
            
        ordered = [x for _, x in sorted(zip(distances, points))]
        output = []
        for i in range(k):
            output.append(ordered[i])
        return output