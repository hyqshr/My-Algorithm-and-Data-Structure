import sys


# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
def eggDrop(n, k):
    if (k == 1 or k == 0):
        return k

#就一个蛋，那么只能把楼梯全部试过去
    if (n == 1):
        return k

    min = float('inf')

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):

        res = max(eggDrop(n - 1, x - 1),eggDrop(n, k - x))
        if (res < min):
            min = res

    return min + 1


egg

if __name__ == "__main__":
    n = 2
    k = 10
    print("Minimum number of trials in worst case with",
          n, "eggs and", k, "floors is", eggDrop(n, k))

# This code is contributed by ita_c