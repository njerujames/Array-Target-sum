'''A function that returns checks whether a pair in the array returns the target sum or not'''
def pairs(array = [3,5,-4,8,11,1,-1,6],target_sum = 17):
    '''Function passes an array and a integer value.

    Parameters:
        array -- A keyword arguement that passes an array.
        target_sum -- A keyword arguement that passes an integer.

    Returns: a boolean condition.

    Time complexity: O(n^2)
    '''
    for x in range(len(array)):
        for y in range(x + 1, len(array)):
            if array[x] + array[y] == target_sum:
                return print(array[x], array[y])
    return False