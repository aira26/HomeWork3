class Quicksort(object):
    def __init__(self):
        self.mylist1 = []
        self.size = 0

    def add(self, value):
        self.mylist1.append(value)
        self.size += 1

    def quick_sort(self):
        if len(self.mylist1) > 1:
            pivot = self.mylist1[0]
            self.left = Quicksort()
            self.right = Quicksort()

            for i in range(1, len(self.mylist1)):
                if (self.mylist1[i] < pivot):
                    self.left.add(self.mylist1[i])
                else:
                    self.right.add(self.mylist1[i])

            return self.left.quick_sort() + [pivot] + self.right.quick_sort()

        else:
            return self.mylist1

    def get_min(self):
        new = self.quick_sort()
        return new[0]

    def get_max(self):
        new = self.quick_sort()
        leng = self.size - 1
        return new[leng]

    def get_list(self):
        return self.mylist1


c = Quicksort()
c.add(5)
c.add(2)
c.add(4)
print(c.get_max())
print(c.get_min())
print(c.quick_sort())
print(c.mylist1)

import random
for r in range(100):
    num = random.randint(0,1000)
    c.add(num)
    my_min = c.get_min()
    my_max = c.get_max()

import time
import matplotlib.pyplot as plt



def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


if __name__ == '__main__':
    a = Quicksort()
    a.add(5)
    print(a.mylist1, a.get_min(), a.get_max())
    a.add(7)
    print( a.mylist1, a.get_min(), a.get_max())
    a.add(3)
    print(a.mylist1, a.get_min(), a.get_max())
    a.add(9)
    print(a.mylist1, a.get_min(), a.get_max())

    repetitions = 5
    max_operations = 500
    step = 100

    values_heap_add, values_heap_min, values_heap_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 500))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0

        for repetition in range(5):
           a = Quicksort()
           myadd, mymin, mymax = measure_time(a, this_list)
           tot_time_add += myadd
           tot_time_min += mymin
           tot_time_max += mymax

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)


    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Quicksort Solution")
    plt.show()