def insertionSort(array):
    n = len(array)
    print(array)

    for i in range(1, n):
        j = i-1
        while j >= 0 and array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            j = j-1
    print(array)

array = [1, 5, 4, 3, 9]
insertionSort(array)