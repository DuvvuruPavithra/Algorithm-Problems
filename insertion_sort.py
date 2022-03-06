# creating a function for insertion  
def insertion_sort(array):
    # Outer loop to traverse through 1 to len(list1)
    for i in range(1, len(array)):

        value = array[i]


        # It checks the  greater than value, to one position
        # of their current position
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array
    # Driver code to test above


array = ["P", "A", "V", "I", "T", "R", "A"]
print("The unsorted list is:", array)

print("The sorted list1 is:", insertion_sort(array))