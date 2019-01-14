#task_4
#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#Количество элементов (n) вводится с клавиатуры.

def sum_of_seq(n):
    sum = 0
    element = 1
    for i in range(n):
        sum += element
        element/= -2
    return sum

     
       
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(10)"
#100 loops, best of 3: 1.29 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(100)"
#100 loops, best of 3: 8.3 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(1000)"
#100 loops, best of 3: 91.6 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(10000)"
#100 loops, best of 3: 1.14 msec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(100000)"
#100 loops, best of 3: 10.9 msec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(1000000)"
#100 loops, best of 3: 122 msec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(10000000)"
#100 loops, best of 3: 1.22 sec per loop
    
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(10)"
#100 loops, best of 3: 1.23 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(100)"
#100 loops, best of 3: 9.78 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(1000)"
#100 loops, best of 3: 77.8 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(10000)"
#100 loops, best of 3: 840 usec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(100000)"
#100 loops, best of 3: 10.6 msec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(1000000)"
#100 loops, best of 3: 118 msec per loop
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\2nd_lesson>python -m timeit -n 100 -s "import task_4" "task_4.sum_of_seq(10000000)"
#100 loops, best of 3: 1.21 sec per loop
    
#import cProfile
#cProfile.run('sum_of_seq(10)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_of_seq(100)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_of_seq(1000)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_of_seq(10000)')
#         4 function calls in 0.001 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_of_seq(100000)')
#         4 function calls in 0.009 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#        1    0.009    0.009    0.009    0.009 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_of_seq(1000000)')
#         4 function calls in 0.092 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.091    0.091 <string>:1(<module>)
#        1    0.091    0.091    0.091    0.091 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    0.092    0.092 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_of_seq(10000000)')
#         4 function calls in 1.208 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.208    1.208 <string>:1(<module>)
#        1    1.208    1.208    1.208    1.208 task_4.py:5(sum_of_seq)
#        1    0.000    0.000    1.208    1.208 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
#Согласно измерению времени исполнения алгоритма в файле task_4 с помощью модуля timeit,
#алгоритм task_4 имеет на отрезке n [10, 10000000] линейную сложность - O(n),
#т.е. происходит линейное увеличение времени исполнения алгоритма в зависимости от количества элементов (n).
#Увеличение количества элементов в 10 раз приводит примерно к 10-кратному увеличению времени исполнения алгоритма.
#На отрезке n [10000, 10000000] результаты измерения работы алгоритма с помощью модуля timeit 
#согласуются с результатами измерения работы алгоритма с помощью модуля cProfile.
#На интервале (10, 10000) чувствительность измеренения времени работы алгоритма с помощью cProfile
#недостаточна для суждении о зависимости времени исполнения алгоритма от n. По-видимому,  является менее чувствителнымым 
#(нет даже шумового изменения).
#Время работы алгоритма task_4_4 не зависит от количества элементов (n),
#т.е. уровень сложности - O(1). Согласно измерению времени исполнения алгоритма task_4_4 с помощью модуля timeit
#и на отрезке n (10, 10000000) не происходит изменения времени исполнения алгоритма в зависимости от количества элементов (n). 
#См. task_4 вкладку файла 5thlesson.xlsx.
#Т.к. скорость исполнения алгоритма task_4_4 не зависит от времени и скорость достаточно высока,
#то алгоритм task_4_4 является предпочтительным.     