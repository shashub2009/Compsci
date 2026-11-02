def seq_search(key, array):
    found = False
    index = 0
    while not found and index < len(array):
        if array[index] == key:
            found = True
        index += 1
    return found

def time_search(algo, n, /, sort_data=False):
    import random, time

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)
    if sort_data: data.sort()
    key = n # never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

def bin_search(key, array):
    found = False
    lo = 0
    hi = len(array)-1
    while lo <= hi and not found:
        mid = (lo+hi)//2
        print(array[mid])
        if array[mid] == key:
            found = True
        elif array[mid] < key:
            lo = mid+1
        else: 
            hi = mid-1
    return found

c = [-2,9,11,12,13,14,15,22,142]
print(bin_search(15, c))
names = ['aa', 'bb', 'cc']
rooms = [111,123,132]

class Reservation:
    def __init__(self, name, room):
        self.name = name
        self.room = room
reservations = [Reservation('aa',111), Reservation('bb',123), Reservation('cc', 132)]


key = 'bb'
index = 0
found = False
while not found and index < len(reservations):
    if reservations[index].name == key:
        found = True
    else:
        index += 1
if found:
    print(reservations[index].room)
else:
    print(f'{key} not a guest here')
