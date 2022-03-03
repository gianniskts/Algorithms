def bubbleSort(array):
    print(array)
    n = len(array)

    for i in range(1, n-1):
        j = n-1
        while j >= i:
            if array[j-1] >= array[j]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            j = j-1

    print(array)


array = [1, 5, 4, 3, 9]
bubbleSort(array)
