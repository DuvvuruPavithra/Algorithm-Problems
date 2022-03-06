'''
Binary search can be implemented only on a sorted list of items.
If the elements are not sorted already, we need to sort them first.
'''

def binary_search(array, num, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = (high + low) // 2

        if array[mid] == num:
            return mid

        elif array[mid] < num:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
num = 4

result = binary_search(array, num, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Element Not found")





















# recursive method
def binary_search2(array, num, low, high):

    # Repeat until the pointers low and high meet each other
    if low <= high:

        mid = (low + high) // 2

        if array[mid] == num:
            return mid


        elif array[mid] > num:

            return binary_search(array, num, low, high)

            # Else the search moves to the right sublist1

        else:

            return binary_search(array, mid + 1, high, num)

    else:

        # Element is not available in the list1

        return -1


array = [12, 24, 32, 39, 45, 50, 54]
num = 32

result = binary_search2(array, num, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Element Not found")
