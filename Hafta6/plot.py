import numpy as np
import matplotlib.pyplot as plt
import random
import time


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]


def selection_sort(items):
    for i in range(len(items) - 1, 0, -1):
        posOfMax = 0

        for j in range(1, i + 1):
            if items[i] > items[posOfMax]:
                posOfMax = i

        temp = items[i]
        items[i] = items[posOfMax]
        items[posOfMax] = temp


def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1


def quick_sort(items):
    if len(items) > 1:
        pivot_index = int(len(items) / 2)
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items


if __name__ == '__main__':
    x = np.array([20, 40, 60, 80])

    one = random.sample(range(-500, 500), k=x[0])
    two = random.sample(range(-5000, 5000), k=x[1])
    three = random.sample(range(-50000, 50000), k=x[2])
    four = random.sample(range(-500000, 500000), k=x[3])

    plt.plot(x, x)
    plt.plot(x, x * np.log(x))
    plt.plot(x, x ** 2)

    plt.xticks(x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['n', 'nlogn', 'n2'], loc='upper left')
    plt.savefig('func.png', dpi=250)

    circle = {'1': one,
              '2': two,
              '3': three,
              '4': four}
    times = {}
    for key in circle:
        print(key)
        print(circle[key], times, time.time())
        print(key)

        start = time.time()
        bubble_sort(circle[key])
        times['b' + key] = time.time() - start

        start = time.time()
        selection_sort(circle[key])
        times['s' + key] = time.time() - start

        start = time.time()
        insertion_sort(circle[key])
        times['i' + key] = time.time() - start

        start = time.time()
        quick_sort(circle[key])
        times['q' + key] = time.time() - start

    bubble = np.array([times['b1'],
                       times['b2'],
                       times['b3'],
                       times['b4']])
    selection = np.array([times['s1'],
                          times['s2'],
                          times['s3'],
                          times['s4']])
    insertion = np.array([times['i1'],
                          times['i2'],
                          times['i3'],
                          times['i4']])
    quick = np.array([times['i1'],
                      times['i2'],
                      times['i3'],
                      times['i4']])

    plt.plot(x, bubble)
    plt.plot(x, selection)
    plt.plot(x, insertion)
    plt.plot(x, quick)

    plt.xticks(x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['bubble', 'selection', 'insertion', 'quick'], loc='upper left')
plt.savefig('sort.png', dpi=250)