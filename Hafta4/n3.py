from time import time
import random


def max_sub_sum1(my_vector):
    max_sum = 0
    for i in range((len(my_vector))):

        for j in range(i, len(my_vector)):
            this_sum = 0
            for k in range(i, j):
                this_sum += my_array[k]
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum


my_array = [int(1000 * random.random()) for i in range(1000)]
t0 = time()
print(max_sub_sum1(my_array))
t1 = time()
print("İşlem %.5f saniyede bitti" % (t1 - t0))
