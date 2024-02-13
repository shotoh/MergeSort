def highest(dictionary):
    if len(dictionary) == 0:
        return None
    result = list(dictionary.keys())[0]
    dictionary_max = dictionary.get(result)
    for key, value in dictionary.items():
        if value > dictionary_max:
            result = key
            dictionary_max = value
    return result


def lowest(dictionary):
    if len(dictionary) == 0:
        return None
    result = list(dictionary.keys())[0]
    dictionary_min = dictionary.get(result)
    for key, value in dictionary.items():
        if value < dictionary_min:
            result = key
            dictionary_min = value
    return result


def mean(dictionary):
    dictionary_sum = 0
    for value in dictionary.values():
        dictionary_sum += value
    return dictionary_sum / len(dictionary)


def greater_than_mean(dictionary):
    result = 0
    dictionary_mean = mean(dictionary)
    for value in dictionary.values():
        if value > dictionary_mean:
            result += 1
    return result


def bubble_sort(dictionary):
    length = len(dictionary)
    result = [*dictionary.values()]
    for i in range(length):
        for j in range(0, length - i - 1):
            if result[j] < result[j + 1]:
                temp = result[j + 1]
                result[j + 1] = result[j]
                result[j] = temp
    return result


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
    print(f"Bubble sorted values is {list(map(convert_to_centimeter, bubble_sort(rainfall)))}")
