"""

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked
"""


## guess(num) -- > 0,1,-1 is an implemented API

# Approach 1:
"""
- Loop through each number and check for the output of the API
   -  if 0 - return number
   - 
"""


def guessNumber(self, n: int) -> int:
    for num in range(1, n+1):
        g = guess(num)
        if g==0:
            return num
        
# T(n) - O(n)
# S(n) - O(1)





# Approach 2

"""
l=1, h=n and comapre mid element with guess
if result is 0 --> return mid
else if result is 1 --> l =mid+1
if rsult is -1 --> h= mid-1

"""

def guessNumberOpt(n):
    l = 1
    h = n
    while l <= h:
        mid = (l + h)//2
        g = guess(mid)
        if g == 0:
            return mid
        elif g==1:
            l=mid+1
        else:
            h=mid-1

# T(n) - O(logn)
# S(n) - O(1)