Т.к. было написано про 2 дополнительные реализации, а в задании 4 из урока 2 у меня их только 1 (в дополнении к исходной сделанной), то дополнительно проведён анализ для задания 3 урока 2.
Согласно измерению времени исполнения алгоритма в файле task_4 с помощью модуля timeit,
алгоритм task_4 имеет на отрезке n [10, 10000000] линейную сложность - O(n),
т.е. происходит линейное увеличение времени исполнения алгоритма в зависимости от количества элементов (n).
Увеличение количества элементов в 10 раз приводит примерно к 10-кратному увеличению времени исполнения алгоритма.
На отрезке n [10000, 10000000] результаты измерения работы алгоритма с помощью модуля timeit 
согласуются с результатами измерения работы алгоритма с помощью модуля cProfile.
На интервале (10, 10000) чувствительность измеренения времени работы алгоритма с помощью cProfile
недостаточна для суждении о зависимости времени исполнения алгоритма от n. По-видимому,  является менее чувствителнымым 
(нет даже шумового изменения).
Время работы алгоритма task_4_4 не зависит от количества элементов (n),
т.е. уровень сложности - O(1). Согласно измерению времени исполнения алгоритма task_4_4 с помощью модуля timeit
и на отрезке n (10, 10000000) не происходит изменения времени исполнения алгоритма в зависимости от количества элементов (n). 
См. task_4 вкладку файла 5thlesson.xlsx.
Т.к. скорость исполнения алгоритма task_4_4 не зависит от времени и скорость достаточно высока,
то алгоритм task_4_4 является предпочтительным.
Измерение времени исполнения task_3_1, task_3_2, task_3_3, от n, скорее всего, имеет линейный характер, 
т. е. линейную сложность - O(n). См. task_3 вкладку файла 5thlesson.xlsx. 
При этом угол наклона прямой, описываемой зависимость времени от n, уменьшается в ряду task_3_1, task_3_2, task_3_3, 
т.е. время испонения task_3_3 в наименьшей степени завизит от n на отрезке n [12, 123456789123456789123456789123456789] и выше по скорости. 
