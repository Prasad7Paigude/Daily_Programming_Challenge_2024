"""
Problem : Trapping Rain Water
You are given an array height[] of non-negative integers where each element represents the height of a bar in a histogram-like structure. These bars are placed next to each other, and the width of each bar is 1 unit. When it rains, water gets trapped between the bars if there are taller bars on both the left and right of the shorter bars. The task is to calculate how much water can be trapped between these bars after the rain.

Input :
An integer array height[] where each element represents the height of a bar in the histogram.
Example : 
height[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Output :
* An integer representing the total units of water that can be trapped between the bars.
Example
Output: 6
"""
# Answer -
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1
    return water_trapped

# Test Case 1
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap(height)
print("Total water trapped:", result,"\n")

# Test Case 2
height = [4, 2, 0, 3, 2, 5]
result = trap(height)
print("Total water trapped:", result,"\n")

# Test Case 3
height = [1, 1, 1]
result = trap(height)
print("Total water trapped:", result,"\n")

# Test Case 4
height = [5]
result = trap(height)
print("Total water trapped:", result,"\n")

# Test Case 5
height = [2, 0, 2]
result = trap(height)
print("Total water trapped:", result,"\n")


