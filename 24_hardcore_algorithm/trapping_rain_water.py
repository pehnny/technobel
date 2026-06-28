def trapping_rain_water(heights: list[int]) -> int:
    if len(heights) < 3:
        return 0

    # max_left: list[int] = []
    # max_height = 0
    # for height in heights:
    #     max_height = max(max_height, height)
    #     max_left.append(max_height)

    # max_right: list[int] = []
    # max_height = 0
    # for height in reversed(heights):
    #     max_height = max(max_height, height)
    #     max_right.append(max_height)
    
    # water = 0
    # for i, height in enumerate(heights):
    #     left = max_left[i]
    #     right = max_right[len(heights) - 1 - i]
    #     water += max(min(left, right) - height, 0)
    # return water
    
    water = 0
    left = 0
    right = len(heights)-1
    max_left = 0
    max_right = 0
    while left < right:
        max_left = max(max_left, heights[left])
        max_right = max(max_right, heights[right])
        if heights[left] <= heights[right]:
            water += max(max_left - heights[left], 0)
            left += 1
        else:
            water += max(max_right - heights[right], 0)
            right -= 1
    return water

