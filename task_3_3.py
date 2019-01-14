#task_3
#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, то надо вывести число 6843.

def rever2(n):
    n1 = str(n)
    result = n1[::-1]
    return result

#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12)"
#100 loops, best of 3: 0.416 usec per loop - 12
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123)"
#100 loops, best of 3: 0.452 usec per loop - 123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234)"
#100 loops, best of 3: 0.437 usec per loop - 1234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345)"
#100 loops, best of 3: 0.422 usec per loop - 12345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456)"
#100 loops, best of 3: 0.478 usec per loop - 123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567)"
#100 loops, best of 3: 0.37 usec per loop - 1234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678)"
#100 loops, best of 3: 0.406 usec per loop - 12345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789)"
#100 loops, best of 3: 0.411 usec per loop - 
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891)"
#100 loops, best of 3: 0.422 usec per loop - 1234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912)"
#100 loops, best of 3: 0.447 usec per loop - 12345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123)"
#100 loops, best of 3: 0.468 usec per loop - 123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234)"
#100 loops, best of 3: 0.473 usec per loop - 1234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345)"
#100 loops, best of 3: 0.514 usec per loop - 12345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456)"
#100 loops, best of 3: 0.529 usec per loop - 123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567)"
#100 loops, best of 3: 0.555 usec per loop - 1234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678)"
#100 loops, best of 3: 0.478 usec per loop - 12345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789)"
#100 loops, best of 3: 0.514 usec per loop - 123456789123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567891)"
#100 loops, best of 3: 0.54 usec per loop - 1234567891234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678912)"
#100 loops, best of 3: 0.458 usec per loop - 12345678912345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789123)"
#100 loops, best of 3: 0.581 usec per loop - 123456789123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567891234)"
#100 loops, best of 3: 0.493 usec per loop - 1234567891234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678912345)"
#100 loops, best of 3: 0.601 usec per loop - 12345678912345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789123456)"
#100 loops, best of 3: 0.663 usec per loop - 123456789123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567891234567)"
#100 loops, best of 3: 0.535 usec per loop - 1234567891234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678912345678)"
#100 loops, best of 3: 0.493 usec per loop - 12345678912345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789123456789)"
#100 loops, best of 3: 1.43 usec per loop - 123456789123456789123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567891234567891)"
#100 loops, best of 3: 0.509 usec per loop - 1234567891234567891234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678912345678912)"
#100 loops, best of 3: 0.601 usec per loop - 12345678912345678912345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789123456789123)"
#100 loops, best of 3: 0.586 usec per loop - 123456789123456789123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567891234567891234)"
#100 loops, best of 3: 0.591 usec per loop - 1234567891234567891234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678912345678912345)"
#100 loops, best of 3: 0.499 usec per loop - 12345678912345678912345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789123456789123456)"
#100 loops, best of 3: 0.627 usec per loop - 123456789123456789123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(1234567891234567891234567891234567)"
#100 loops, best of 3: 0.514 usec per loop - 1234567891234567891234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(12345678912345678912345678912345678)"
#100 loops, best of 3: 0.607 usec per loop - 12345678912345678912345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_3" "task_3_3.rever2(123456789123456789123456789123456789)"
#100 loops, best of 3: 0.73 usec per loop - 123456789123456789123456789123456789
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
#т.е. время испонения task_3_3 в наименьшей степени завизит от n на отрезке n [12, 123456789123456789123456789123456789] и выше по скорости. 


#COMMENT AND CONCLUSION
#Измерение времени исполнения task_3_1, task_3_2, task_3_3, от n, скорее всего, имеет линейный характер, 
#т. е. линейную сложность - O(n). См. task_3 вкладку файла 5thlesson.xlsx. 
#При этом угол наклона прямой, описываемой зависимость времени от n уменьшается в ряду task_3_1, task_3_2, task_3_3, 
#т.е. время испонения task_3_3 в наименьшей степени завизит от n на отрезке n [12, 123456789123456789123456789123456789] и выше по скорости. 

