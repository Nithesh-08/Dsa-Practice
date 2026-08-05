# Problem:Valid Palindrome
# Pattern:Two Pointers(opposite direction)
# Approach:start from both ends,compare characters,and move both pointers inward 
# Time Complexity:O(n)
# Space Complexity:O(1)
def is_Palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
  
