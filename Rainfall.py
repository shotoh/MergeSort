def highest(dictionary):
    result = 0
    dict_max = 0
    for x, y in dictionary.items():
        if y > dict_max:
            result = x
            dict_max = y
    return result


def lowest(dictionary):
    result = 0
    dict_min = 1000 # todo replace w/ max
    for x, y in dictionary.items():
        if y < dict_min:
            result = x
            dict_min = y
    return result


def mean(dictionary):
    dict_sum = 0
    for y in dictionary.values():
        dict_sum += y
    return dict_sum / len(dictionary)


def greater_than_mean(dictionary):
    dict_mean = mean(dictionary)
    dict_num = 0
    for y in dictionary.values():
        if y > dict_mean:
            dict_num += 1
    return dict_num


def bubble_sort(dictionary):
    length = len(dictionary)
    arr = [*dictionary.values()]
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] < arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr


def convert_to_centimeter(inches):
    return inches * 2.54


if __name__ == '__main__':
    rainfall = {
        1: 133.5,
        2: 64.3,
        3: 104.4,
        4: 86.3,
        5: 48.5,
        6: 35.4,
        7: 55.3,
        8: 84.9,
        9: 104.5,
        10: 104.4,
        11: 122.6,
        12: 119.5
    }
    print(f"Month with highest rainfall is {highest(rainfall)}")
    print(f"Month with lowest rainfall is {lowest(rainfall)}")
    print(f"The mean value of rainfall is {convert_to_centimeter(mean(rainfall))} cm")
    print(f"The number of months with rainfall greater than mean is {greater_than_mean(rainfall)}")
    print(f"Bubble sorted values is {bubble_sort(rainfall)}")
