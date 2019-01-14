#task_3
#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, то надо вывести число 6843.
def rever(n):
    result = ''
    for i in str(n):
        result = i + result
    return result

#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12)"
#100 loops, best of 3: 0.591 usec per loop - 12
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123)"
#100 loops, best of 3: 0.756 usec per loop - 123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234)"
#100 loops, best of 3: 0.889 usec per loop - 1234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345)"
#100 loops, best of 3: 0.915 usec per loop - 12345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456)"
#100 loops, best of 3: 0.869 usec per loop - 123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567)"
#100 loops, best of 3: 0.843 usec per loop - 1234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678)"
#100 loops, best of 3: 1.02 usec per loop - 12345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789)"
#100 loops, best of 3: 1.23 usec per loop - 123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891)"
#100 loops, best of 3: 1.2 usec per loop - 1234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912)"
#100 loops, best of 3: 1.66 usec per loop - 12345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123)"
#100 loops, best of 3: 1.94 usec per loop - 123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234)"
#100 loops, best of 3: 1.64 usec per loop - 1234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345)"
#100 loops, best of 3: 1.86 usec per loop - 12345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456)"
#100 loops, best of 3: 1.82 usec per loop - 123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567)"
#100 loops, best of 3: 1.85 usec per loop - 1234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678)"
#100 loops, best of 3: 1.92 usec per loop - 12345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789)"
#100 loops, best of 3: 5.26 usec per loop - 123456789123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567891)"
#100 loops, best of 3: 2.54 usec per loop - 1234567891234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678912)"
#100 loops, best of 3: 2.27 usec per loop - 12345678912345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789123)"
#100 loops, best of 3: 4.08 usec per loop - 123456789123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567891234)"
#100 loops, best of 3: 2.09 usec per loop - 1234567891234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678912345)"
#100 loops, best of 3: 2.56 usec per loop - 12345678912345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789123456)"
#100 loops, best of 3: 2.69 usec per loop - 123456789123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567891234567)"
#100 loops, best of 3: 2.77 usec per loop - 1234567891234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678912345678)"
#100 loops, best of 3: 3.22 usec per loop - 12345678912345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789123456789)"
#100 loops, best of 3: 3.04 usec per loop - 123456789123456789123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567891234567891)"
#100 loops, best of 3: 3.02 usec per loop - 1234567891234567891234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678912345678912)"
#100 loops, best of 3: 3.5 usec per loop - 12345678912345678912345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789123456789123)"
#100 loops, best of 3: 2.64 usec per loop - 123456789123456789123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567891234567891234)"
#100 loops, best of 3: 3.17 usec per loop - 1234567891234567891234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678912345678912345)"
#100 loops, best of 3: 3.17 usec per loop - 12345678912345678912345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789123456789123456)"
#100 loops, best of 3: 2.69 usec per loop - 123456789123456789123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(1234567891234567891234567891234567)"
#100 loops, best of 3: 3.22 usec per loop - 1234567891234567891234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(12345678912345678912345678912345678)"
#100 loops, best of 3: 2.72 usec per loop - 12345678912345678912345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_2" "task_3_2.rever(123456789123456789123456789123456789)"
#100 loops, best of 3: 2.9 usec per loop - 123456789123456789123456789123456789
#import cProfile
#cProfile.run('rever(12)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_2.py:4(rever)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('rever(123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_2.py:4(rever)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('rever(123456789123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_2.py:4(rever)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('rever(123456789123456789123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_2.py:4(rever)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('rever(123456789123456789123456789123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_2.py:4(rever)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#Измерение времени исполнения task_3_1, task_3_2, task_3_3, от n, скорее всего, имеет линейный характер, 
#т. е. линейную сложность - O(n). См. task_3 вкладку файла 5thlesson.xlsx. 
#При этом угол наклона прямой, описываемой зависимость времени от n уменьшается в ряду task_3_1, task_3_2, task_3_3, 
#т.е. время испонения task_3_3 в наименьшей степени завизит от n на отрезке n [12, 123456789123456789123456789123456789]. 
