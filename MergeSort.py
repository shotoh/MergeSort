import random


def merge_sort(array):
    # base case for recursion
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # use recursion
    merge_sort(left)
    merge_sort(right)

    i = j = 0
    curr = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[curr] = left[i]
            i += 1
        else:
            array[curr] = right[j]
            j += 1
        curr += 1

    # when one tail is empty, append the other tail
    while i < len(left):
        array[curr] = left[i]
        i += 1
        curr += 1

    while j < len(right):
        array[curr] = right[j]
        j += 1
        curr += 1

    return array


def print_array(array):
    for x in array:
        print(x)


if __name__ == '__main__':
    array_to_sort = []
    for _ in range(10):
        array_to_sort.append(random.randint(0, 100))
    print("Unsorted array:")
    print_array(array_to_sort)
    merge_sort(array_to_sort)
    print("Sorted array:")
    print_array(array_to_sort)
