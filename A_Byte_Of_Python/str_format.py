age = 26
name = "Swaroop"

print("Возраст {0} -- {1} год.".format(name,age))
print("Почему {0} забавляется с этим Python?".format(name))

#десятичное число (.) с точностью в 3 знака для плавающих:
print("{0:.3}".format(1/3))
#заполните подчеркиваниями(_) с центровкой текста (^) по ширине 11:
print("{0:_^11}".format("hello"))
#по ключевым словам:
print("{name} написал {book}".format(name = "Swaroop", book = "A Byte of Python"))