'''
Практическое задание № 1

Эмпирическая оценка алгоритмов на Python
'''

import timeit
import random
import cProfile


'''3.3  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы'''

SIZE = 1_000_000

'''1 Вариант'''

n = []

for i in range(SIZE):
    random_ = random.randint(0, 99)
    n.append(random_)

#print(n)


def first_example():
    max_ = 0
    min_ = 0
    for i in range(len(n)):

        if n[i] > n[max_]:
            max_ = i
        elif n[i] < n[min_]:
            min_ = i

    n[max_], n[min_] = n[min_], n[max_]

    return n


#print(first_example())

print(timeit.timeit('first_example()', number=100, globals=globals())) # SIZE 10, 0.00011560000007193594
print(timeit.timeit('first_example()', number=100, globals=globals())) # SIZE 100, 0.0009262999999464228
print(timeit.timeit('first_example()', number=100, globals=globals())) # SIZE 1000, 0.010326200000008612
print(timeit.timeit('first_example()', number=100, globals=globals())) # SIZE 100000, 0.894484299999931
print(timeit.timeit('first_example()', number=100, globals=globals())) # SIZE 1000000, 9.329238400000008

cProfile.run('first_example()')

'''
         5 function calls in 0.138 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.138    0.138 <string>:1(<module>)
        1    0.138    0.138    0.138    0.138 homework_4_1.py:27(first_example)
        1    0.000    0.000    0.138    0.138 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''




'''2 Вариант'''

def second_example():

    n[n.index(max(n))], n[n.index(min(n))] = n[n.index(min(n))], n[n.index(max(n))]
    return n

#print(second_example())
print()
print(timeit.timeit('second_example()', number=100, globals=globals())) # SIZE 10, 0.0001260000000229411
print(timeit.timeit('second_example()', number=100, globals=globals())) # SIZE 100, 0.00046499999996285624
print(timeit.timeit('second_example()', number=100, globals=globals())) # SIZE 1000, 0.003298599999993712
print(timeit.timeit('second_example()', number=100, globals=globals())) # SIZE 100000, 0.3074466000000484
print(timeit.timeit('second_example()', number=100, globals=globals())) # SIZE 1000000, 3.187567700000045

cProfile.run('second_example()')

'''
         12 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.032    0.032 <string>:1(<module>)
        1    0.000    0.000    0.032    0.032 homework_4_1.py:70(second_example)
        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
        2    0.017    0.008    0.017    0.008 {built-in method builtins.max}
        2    0.015    0.007    0.015    0.007 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''

'''3 Вариант'''

new = [random.randint(0, 99) for i in range(SIZE)]
#print(new)


def third_example():

    maxi_ = new[new.index(sorted(new)[-1])]
    mini_ = new[new.index(sorted(new)[0])]

    new[new.index(maxi_)], new[new.index(mini_)] = new[new.index(mini_)], new[new.index(maxi_)]

    return new

#print(third_example())
print()
#print(timeit.timeit('third_example()', number=100, globals=globals())) # SIZE 10, 0.00012309999874560162
#print(timeit.timeit('third_example()', number=100, globals=globals())) # SIZE 100, 0.0008511000050930306
#print(timeit.timeit('third_example()', number=100, globals=globals())) # SIZE 1000, 0.01411270000244258
#print(timeit.timeit('third_example()', number=100, globals=globals())) # SIZE 100000, 1.7038792000021203
#print(timeit.timeit('third_example()', number=100, globals=globals())) # SIZE 1000000, 16.956531899995753

cProfile.run('third_example()')

'''
12 function calls in 0.168 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.168    0.168 <string>:1(<module>)
        1    0.003    0.003    0.168    0.168 homework_4_1.py:86(third_example)
        1    0.000    0.000    0.168    0.168 {built-in method builtins.exec}
        2    0.165    0.083    0.165    0.083 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''


'''
Наиболее оптимальным и простым решением является 2-ой пример с использованием max() и min(), т.к. в отличие от 
остальных примеров каждый вызов этой функции займет наименьшее время для ее выполнения (0.031 сек при вызове 12 функций)
'''


