import timeit
import random

for i in range(10000, 1000000, 20000): # i = 10000, i < 1000000, i += 20000
    t = timeit.Timer("x[random.randrange(%d)]" % i, "from __main__ import random, x")
    x = list(range(i))
    index_time = t.timeit(number=1000)
    print("%d, %.4f" % (i, index_time))
