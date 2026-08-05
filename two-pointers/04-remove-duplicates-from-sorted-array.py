# Problem: Remove Duplicates from Sorted Array
# Pattern: Two Pointers


# -------------------------
# Brute Force Approach
# Time: O(n) average
# Space: O(n)
# -------------------------

def remove_duplicates_brute(nums):
    unique = set()

    for num in nums:
        unique.add(num)

    return list(unique)


# -------------------------
# Optimal Approach - Two Pointers
# Time: O(n)
# Space: O(1)
# -------------------------

def remove_duplicates_optimal(nums):
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write
