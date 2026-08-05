# Problem: Two Sum II - Input Array Is Sorted
# Pattern: Two Pointers (Opposite Direction)


# ---------------- BRUTE FORCE ----------------
# Approach: Check every possible pair using nested loops.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def two_sum_brute(numbers, target):
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


# ---------------- OPTIMAL ----------------
# Approach: Use pointers at both ends and move them based on the current sum.
# Time Complexity: O(n)
# Space Complexity: O(1)

def two_sum_optimal(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        cur_sum = numbers[left] + numbers[right]

        if cur_sum > target:
            right -= 1
        elif cur_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]
