

'''A function that returns checks whether a pair in the array returns the target sum or not'''
def triplets(array = [12, 3, 1, 2, -6, 5, -8, 6],target_sum = 0):
    '''Function passes an array and a integer value.

    Parameters:
        array -- A keyword arguement that passes an array.
        target_sum -- A keyword arguement that passes an integer.

    Returns: a boolean condition.

    Time complexity: O(n^3)
    '''
    for x in range(len(array)):
         for y in range(x + 1, len(array)):
             for z in range(y + 1):
                if array[x] + array[y] + array[z] == target_sum:
                    return print(array[x],array[y],array[z])
    return False

triplets()