check if the given array is sorted or not 
## If it is sorted 
use two pointers to get -->optimal approach with TC:O(N) SC:O(1)
use Binary Search to get -->Better aproach with TC:O(NlogN) SC:O(1)
use Nested Loops to get -->Brute force approach with TC:O(N*N) SC:O(1)

## If it is not sorted
use Nested Loops to get -->Brute force approach with TC:O(N*N) SC:O(1)
use sort()+two pointers to get -->Better approach with TC:O(NlogN) SC:O(1)
use HashMap to get -->Optimal approach with TC:O(N) SC:O(N)

PROBLEM
---------------------------
arr = [7, 2, 11, 15]
target = 9

---FOR UNSORTED ARRAY---
BRUTE:
arr = list(map(int, input().split()))
target = int(input())

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):

        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            break

BETTER:

arr = list(map(int, input().split()))
target = int(input())
arr.sort()
left = 0
right = len(arr) - 1
while left < right:
   total = arr[left] + arr[right]

    if total == target:
        print(arr[left], arr[right])
        break

    elif total < target:
        left += 1

    else:
        right -= 1

OPTIMAL:

arr = list(map(int, input().split()))
target = int(input())

seen = set()

for num in arr:

    needed = target - num

    if needed in seen:
        print(needed, num)
        break

    seen.add(num)

---FOR SORTED ARRAY---

BRUTE:

arr = list(map(int, input().split()))
target = int(input())

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):

        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            break

BETTER:

arr = list(map(int, input().split()))
target = int(input())

for i in range(len(arr)):

    needed = target - arr[i]

    left = i + 1
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == needed:
            print(arr[i], arr[mid])
            break

        elif arr[mid] < needed:
            left = mid + 1

        else:
            right = mid - 1

OPTIMAL:

arr = list(map(int, input().split()))
target = int(input())

left = 0
right = len(arr) - 1

while left < right:

    total = arr[left] + arr[right]

    if total == target:
        print(arr[left], arr[right])
        break


    elif total < target:
        left += 1

    else:
        right -= 1
