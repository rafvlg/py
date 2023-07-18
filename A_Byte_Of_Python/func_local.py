x = 50 
def func(x):
    print("x равен", x)#     x = 2 
    print("Замена локального x на", x)    
func(x)
print("x по-прежнему", x)

# При первом выводе значения, присвоенного имени x, в первой строке функции
# Python использует значение параметра, объявленного в основном блоке, выше определения функции.
# Далее мы назначаем x значение 2. Имя x локально для нашей функции. 
# Поэтому когда мы заменяем значение x в функции, x, объявленный в основном# блоке, 
# остаётся незатронутым.
# Последним вызовом функции print мы выводим значение x, указанное 
# в основном блоке, подтверждая таким образом, что оно не изменилось 
# при локальном присваивании значения в ранее вызванной функции.