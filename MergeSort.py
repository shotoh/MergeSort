def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = 0
    curr = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[curr] = left[i]
            i += 1
        else:
            arr[curr] = right[j]
            j += 1
        curr += 1

    while i < len(left):
        arr[curr] = left[i]
        i += 1
        curr += 1

    while j < len(right):
        arr[curr] = right[j]
        j += 1
        curr += 1

    return arr


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])


if __name__ == '__main__':
    arr = [4, 13, 9, 55, 27, 5, 3, 19, 7, 34]
    merge_sort(arr)
    print("Printing sorted array:")
    print_arr(arr)
