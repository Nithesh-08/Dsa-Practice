# Problem: Squares of a Sorted Array
# Pattern: Two Pointers


# -------------------------
# Brute Force Approach
# Time: O(n log n)
# Space: O(n)
# -------------------------

def sorted_squares_brute(nums):
    result = []

    for num in nums:
        result.append(num ** 2)

    result.sort()

    return result


# -------------------------
# Optimal Approach - Two Pointers
# Time: O(n)
# Space: O(n) for output array
# -------------------------

def sorted_squares_optimal(nums):
    n = len(nums)

    left = 0
    right = n - 1
    pos = n - 1

    result = [0] * n

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result
