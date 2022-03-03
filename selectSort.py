def selectSort(array):
    n = len(array)
    print(array)

    for i in range(n-1):
        min = i
        for j in range(i, n-1):
            if (array[j] < array[min]):
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp

    print(array)


array = [1, 5, 4, 3, 9]
selectSort(array)