number = 23
guess = int(input("Введите целое число: "))

if guess == number:
    print("Поздравляю, Вы угадали, ") # Начало нового блока
    print("(хотя и не выиграли никакого приза!)") # Конец нового блока
elif guess < number:
    print("Нет, загаданное число немного больше этого.") # Eщё один блок
    # Внутри блока Вы можете выполнять всё, что угодно ... 
else:
    print("Нет загаданное число немного меньше этого.")
    # чтобы попасть сюда, guess должно быть больше чем number
print("Завершено")
# Это последнее выражение выполняется всегда после выполнения оператора if

# Как это работает:
# В этой программе мы принимаем варианты от пользователя и проверяем, совпадают ли они с заранее заданным числом. Мы устанавливаем переменной
# number значение любого целого числа, какого хотим. Например, 23. После
# этого мы принимаем вариант числа от пользователя при помощи функции
# input(). Функции – это всего-навсего многократно используемые фрагменты программы. Мы узнаем о них больше в следующей главе.
# Мы передаём встроенной функции input строку, которую она выводит на
# экран и ожидает ввода от пользователя. Как только мы ввели что-нибудь и нажали клавишу Enter, функция input() возвращает строку, которую мы ввели. Затем мы преобразуем полученную строку в число при помощи int(),
# и сохраняем это значение в переменную guess. Вообще-то, int – это класс,
# но на данном этапе вам достаточно знать лишь, что при помощи него можно
# преобразовать строку в целое число (предполагая, что строка содержит целое
# число).
# Далее мы сравниваем число, введённое пользователем, с числом, которое мы
# выбрали заранее. Если они равны, мы печатаем сообщение об успехе. Обратите внимание, что мы используем соответствующие уровни отступа, чтобы
# указать Python, какие выражения относятся к какому блоку. Вот почему отступы так важны в Python. Я надеюсь, вы придерживаетесь правила «постоянных
# отступов», не так ли?
# Обратите внимание, что в конце оператора if стоит двоеточие – этим мы по
# казываем, что далее следует блок выражений.
# После этого мы проверяем, верно ли, что пользовательский вариант числа
# меньше загаданного, и если это так, мы информируем пользователя о том,
# что ему следует выбирать числа немного больше этого. Здесь мы использовали выражение elif, которое попросту объединяет в себе два связанных if
# else-if else выражения в одно выражение if-elif-else. Это облегчает
# чтение программы, а также не требует дополнительных отступов.
# Выражения elif и else также имеют двоеточие в конце логической строки,
# за которым следуют соответствующие блоки команд (с соответствующим числом отступов, конечно).
# Внутри if-блока оператора if может быть другой оператор if и так далее – это
# называется вложенным4 оператором if.
# Помните, что части elif и else не обязательны. Минимальная корректная
# запись оператора if такова:
# if True:
# print('Да, это верно.')
# После того, как Python заканчивает выполнение всего оператора if вместе с
# его частями elif и else, он переходит к следующему выражению в блоке,
# содержащем этот оператор if. В нашем случае это основной блок программы
# (в котором начинается выполнение программы), а следующее выражение –
# это print('Завершено'). После этого Python доходит до конца программы и
# просто выходит из неё.