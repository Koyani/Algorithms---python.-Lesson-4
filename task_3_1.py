#task_3
#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, то надо вывести число 6843.

def palindrome(n):
    palindrome = 0
    while n > 0:
        palindrome = palindrome*10 + n%10 
        n = n // 10
    return palindrome
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12)"
#100 loops, best of 3: 0.355 usec per loop - 12
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123)"
#100 loops, best of 3: 0.54 usec per loop - 123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234)"
#100 loops, best of 3: 0.612 usec per loop - 1234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345)"
#100 loops, best of 3: 0.787 usec per loop - 12345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456)"
#100 loops, best of 3: 0.93 usec per loop - 123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567)"
#100 loops, best of 3: 1.34 usec per loop - 1234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678)"
    #100 loops, best of 3: 1.31 usec per loop - 12345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789)"
#100 loops, best of 3: 1.48 usec per loop - 123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891)"
#100 loops, best of 3: 5.01 usec per loop - 1234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912)"
#100 loops, best of 3: 6.34 usec per loop - 12345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123)"
#100 loops, best of 3: 2.15 usec per loop - 123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234)"
#100 loops, best of 3: 2.64 usec per loop - 1234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345)"
#100 loops, best of 3: 2.57 usec per loop - 12345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456)"
#100 loops, best of 3: 2.78 usec per loop - 123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567)"
#100 loops, best of 3: 3.21 usec per loop - 1234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678)"
#100 loops, best of 3: 3.43 usec per loop - 12345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789)"
#100 loops, best of 3: 3.95 usec per loop - 123456789123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567891)"
#100 loops, best of 3: 4.47 usec per loop - 1234567891234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678912)"
#100 loops, best of 3: 5.34 usec per loop - 12345678912345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789123)"
#100 loops, best of 3: 5.49 usec per loop - 123456789123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567891234)"
#100 loops, best of 3: 5.16 usec per loop - 1234567891234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678912345)"
#100 loops, best of 3: 5.16 usec per loop - 12345678912345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789123456)"
#100 loops, best of 3: 6.19 usec per loop - 123456789123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567891234567)"
#100 loops, best of 3: 6.51 usec per loop - 1234567891234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678912345678)"
#100 loops, best of 3: 6.76 usec per loop - 12345678912345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789123456789)"
#100 loops, best of 3: 7.3 usec per loop - 123456789123456789123456789
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567891234567891)"
#100 loops, best of 3: 6.68 usec per loop - 1234567891234567891234567891
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678912345678912)"
#100 loops, best of 3: 7.08 usec per loop - 12345678912345678912345678912
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789123456789123)"
#100 loops, best of 3: 8.37 usec per loop - 123456789123456789123456789123
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567891234567891234)"
#100 loops, best of 3: 27.9 usec per loop - 1234567891234567891234567891234
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678912345678912345)"
#100 loops, best of 3: 9.19 usec per loop - 12345678912345678912345678912345
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789123456789123456)"
#100 loops, best of 3: 9.1 usec per loop - 123456789123456789123456789123456
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(1234567891234567891234567891234567)"
#100 loops, best of 3: 9.37 usec per loop - 1234567891234567891234567891234567
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(12345678912345678912345678912345678)"
#100 loops, best of 3: 9.32 usec per loop - 12345678912345678912345678912345678
#
#C:\Users\molbi\Desktop\geekbrains\algoritms_python\5th_lesson>python -m timeit -n 100 -s "import task_3_1" "task_3_1.palindrome(123456789123456789123456789123456789)"
#100 loops, best of 3: 11 usec per loop - 123456789123456789123456789123456789
##
#import cProfile
#cProfile.run('palindrome(12)')
#
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_1.py:5(palindrome)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('palindrome(123456789)')
#        4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_1.py:5(palindrome)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('palindrome(123456789123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_1.py:5(palindrome)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('palindrome(123456789123456789123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_1.py:5(palindrome)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('palindrome(123456789123456789123456789123456789)')
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_3_1.py:5(palindrome)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#COMMENT AND CONCLUSION
#Измерение времени исполнения task_3_1, task_3_2, task_3_3, от n, скорее всего, имеет линейный характер, 
#т. е. линейную сложность - O(n). См. task_3 вкладку файла 5thlesson.xlsx. 
#При этом угол наклона прямой, описываемой зависимость времени от n уменьшается в ряду task_3_1, task_3_2, task_3_3, 
#т.е. время испонения task_3_3 в наименьшей степени завизит от n на отрезке n [12, 123456789123456789123456789123456789] и выше по скорости. 