

'''A function that returns checks whether a pair in the array returns the target sum or not'''
def quad(array = [7, 6, 4, -1, 1, 2], target_sum  = 16):
    '''Function passes an array and a integer value.

    Parameters:
        array -- A keyword arguement that passes an array.
        target_sum -- A keyword arguement that passes an integer.

    Returns: a boolean condition.

    Time complexity: O(n^4)
    '''
    for x in range(len(array)):
         for y in range(x + 1, len(array)):
             for z in range(y + 1):
                 for w in range(z + 1):
                    if array[x] + array[y] + array[z] + array[w] == target_sum:
                        return print(array[x],array[y],array[z],array[w])
    return False

quad()