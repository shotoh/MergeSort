def highest(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element


def lowest(arr):
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element


def mean(arr):
    sum_elements = 0
    for i in range(len(arr)):
        sum_elements += arr[i]
    return sum_elements / len(arr)


def greater_than_mean(arr):
    mean_elements = mean(arr)
    num_elements = 0
    for i in range(len(arr)):
        if arr[i] > mean_elements:
            num_elements += 1
    return num_elements


#def bubble_sort(arr):