'''
Практическое задание № 2

Эмпирическая оценка алгоритмов на Python
'''
import timeit
import cProfile

def without_eratosthenes(N):
    counter = 1
    prime = [2]
    num = 1

    if indx == 1:
        return 2

    while counter < indx:
        num += 2

        for i in prime:
            if num %  i == 0:
                break
        else:
            counter += 1
            prime.append(num)

    return prime[-1]


def eratosthenes_sieve(N):
    a = [i for i in range(N + 1)]

    a[1] = 0
    i = 2

    while i < N ** 0.5:
        if a[i] != 0:
            j = i ** 2
            while j <= N:
                a[j] = 0
                j = j + i

        i = i + 1

    a = [i for i in a if a[i] != 0]

    # print(a)

    if indx < len(a):
        if indx == 1:
            return a[0]
        else:
            for i in range(len(a)):
                if indx == i:
                    return a[i - 1]

    else:
        return 'Ошибка! Увеличивайте параметр длины списка N'




N = 1_000_000

indx = int(input('Введите индекс простого числа: '))


print(f'Введеннвый индекс {indx} простого числа - {without_eratosthenes(N)}')
print(f'Введеннвый индекс {indx} простого числа с помощью Решето Эратосфена - {eratosthenes_sieve(N)}')

print(timeit.timeit('without_eratosthenes(N)', number=1, globals=globals())) # N = 1_000_000, 1.8979672999994364
print(timeit.timeit('eratosthenes_sieve(N)', number=1, globals=globals())) # N = 1_000_000, 0.21380409999983385

cProfile.run('without_eratosthenes(N)')
'''
10003 function calls in 1.949 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.949    1.949 <string>:1(<module>)
        1    1.948    1.948    1.949    1.949 homework_4_2.py:9(without_eratosthenes)
        1    0.000    0.000    1.949    1.949 {built-in method builtins.exec}
     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
cProfile.run('eratosthenes_sieve(N)')
'''
8 function calls in 0.226 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.226    0.226 <string>:1(<module>)
        1    0.156    0.156    0.224    0.224 homework_4_2.py:30(eratosthenes_sieve)
        1    0.034    0.034    0.034    0.034 homework_4_2.py:31(<listcomp>)
        1    0.033    0.033    0.033    0.033 homework_4_2.py:45(<listcomp>)
        1    0.000    0.000    0.226    0.226 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''

'''
Наиболее оптимальным кодом вычисления простых чисел является решение алгоритма «Решето Эратосфена», так как кол-во
вызова функций в отличие от другого решения (10003 function calls in 1.949 seconds) составляет только -
8 function calls in 0.226 seconds, например, при поиске индекса простых чисел - 10_000.
'''