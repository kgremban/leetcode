from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Get starting dimensions with max width
        left_wall = 0
        right_wall = len(height) - 1
        
        width = len(height) - 1
        volume = width * min(height[left_wall], height[right_wall])

        max_volume = volume
        
        # Move container walls in towards center, calculating
        # volume as you go and keeping track of max volume
        while left_wall < right_wall:

            # If left_wall is shorter than right wall, move left in
            if height[left_wall] < height[right_wall]:
                left_wall += 1

            # Otherwise, move right in
            else:
                right_wall -= 1

            # Calculate new volume and compare it to max
            volume = (right_wall - left_wall) * min(height[left_wall], height[right_wall])
            if volume > max_volume:
                max_volume = volume

        return max_volume

def main():
    sol = Solution()

    input1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    input2 = [3, 9, 3, 4, 7, 2, 12, 6]
    input3 = [1, 2, 1, 20, 20, 1, 2, 1]
    input4 = [1, 3, 2, 5, 25, 24, 5]

    print(sol.maxArea(input4))

if __name__ == "__main__":
    main()