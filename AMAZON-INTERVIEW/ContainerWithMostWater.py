class MostWater:
    def Container(self, height):
        left, right = 0, len(height) - 1
        maxarea = 0

        while left <= right:
            area = min(height[left], height[right]) * (right - left)
            maxarea = max(maxarea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
    
sol = MostWater()
height = [1,8,6,2,5,4,8,3,7]
print(sol.Container(height))