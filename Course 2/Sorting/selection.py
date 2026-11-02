def selection_sort(array):
    for i in range(len(array)-1):
        smallest = array[i]
        smallest_index = i
        for j in range(i+1, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallest_index = j
        if smallest_index != i:
            (array[i], array[smallest_index]) = (array[smallest_index], array[i])  


arr = [7,9,2,11]
selection_sort(arr)
print(arr)

def time_sort(algo, n):
    import time, random

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

print(time_sort(selection_sort, 1000))


