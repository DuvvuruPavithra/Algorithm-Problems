'''
1.starting with the first element(index=0) compare the current element with the next element of the array
2.if the current element is greater than the next element of the array swap them
3.if the current element is less than the next element move to next element.repeat step 1
'''


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    data = [9, 1, 8, 4, 7, 6, 3, 5]
    print("Array before sorting", data)
    print("Array After sorting", bubble_sort(data))
