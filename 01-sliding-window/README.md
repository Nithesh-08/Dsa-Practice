# Sliding Window — DSA Practice

This folder contains my Data Structures and Algorithms practice problems based on the **Sliding Window** technique, implemented in Python.

## 🎯 What Is Sliding Window?

Sliding Window is an algorithmic technique used to process contiguous subarrays or substrings efficiently by maintaining a window over a sequence.

Instead of recalculating values for every possible window, we update the current window as it moves.

## 📚 Patterns

### 1. Fixed-Size Sliding Window
Used when the window size `k` is given.

**Core idea:**
- Add the incoming element.
- Remove the outgoing element.
- Update the result.

### 2. Variable-Size Sliding Window
Used when the window expands or shrinks based on a condition.

**Core idea:**
- Expand the window using `right`.
- Shrink it using `left` when the condition is violated.
- Update the result.

## 📝 Problems

Longest Substring Without Repeating Characters
Minimum Window Substring
Permutation in String
Longest Repeating Character Replacement
Sliding Window Maximum
Find All Anagrams in a String
Maximum Sum Subarray of Size K

## ⏱️ Complexity

- **Time:** Usually `O(n)` for standard sliding-window solutions.
- **Space:** Often `O(1)` for simple numeric windows; frequency maps or sets may require additional space.

Complexity depends on the specific problem.

## 💡 Key Takeaway

Recognize when a problem involves a contiguous subarray or substring. Determine whether the window is fixed-size or variable-size, then define the condition for expanding, shrinking, and updating the result.

**Language:** Python  
**Purpose:** DSA practice and interview preparation.
