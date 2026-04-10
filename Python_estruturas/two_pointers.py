# Here's some pseudocode illustrating the concept:

function fn(arr):
    left = 0
    right = arr.length - 1

    while left < right:
    #     Do some logic here depending on the problem
    #     Do some more logic here to decide on one of the following:
     left++
     right--
    #  Both left++ and right--


# The strength of this technique is that we will never have more than 
# O(n) O(n) iterations for the while loop because the pointers start 
# n n away from each other and move at least one step closer in every iteration. Therefore, if we can keep the work inside each iteration at 
# O (1)
# O(1), this technique will result in a linear runtime, which is usually the best possible runtime. Let's look at some examples.

