"""

Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1


"""

# Approach 1

"""
 - You go through all the elements of the list :
    - If the element is equal to "target" --> return the element's index
    - else return -1 (the target is not in the list)
"""


def binarySearch(nums,target):
    for ix, element in enumerate(nums):
        if element == target:
            return ix
    return -1


# T(n) - O(n)
# S(n) - O(1)

# Approach 2

"""
- l,m,h --> 0, middle, last index of the list
- We compare the middle element with the target:
  - if target is equal to the middle element(m) - return the index of the middle element
  - else we compare whether the target is less or more than the middle(m) element:
    -  if middle(m) element > target --> move the high pointer to index one less than middle(m)
    -  else we move the l pointer to one index higher than the middle (m)

    
    

"""


def binarySearch2(nums, target):
    l,h = 0,len(nums)-1
    while l <= h:
        m = l+h//2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m+1
        else:
            h = m-1
    return -1

# T(n) - O(logn)
# S(n) - O(1)

 

     







