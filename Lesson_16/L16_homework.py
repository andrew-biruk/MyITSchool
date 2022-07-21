# Два метода в классе, один принимает в себя строку либо число.
# Если передана строка: вывести гласные, если произведение гласных и согласных
# меньше либо равно длине слова, иначе - согласные.
# Если передано число: вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class MyClass:
    # method takes string or number (natural or real) and works with conditions
    # name space remains empty since requirements don't specify if it should store attributes:
    def method1(self, data):
        if isinstance(data, str):
            c, v = "", ""
            for i in data:
                if i.lower() in "aeiou":
                    v += i
                else:
                    c += i
            print([c, v][len(c) * len(v) <= self.method2(data)])
        else:
            data = str(data).replace(".", "")
            print(sum(int(i) for i in data if not int(i) % 2) * self.method2(data))

    # method2 returns len of string or number:
    @staticmethod
    def method2(x):
        return [len(str(x).replace(".", "")), len(x)][isinstance(x, str)]


test = MyClass()
for w in ("Cat", "Toto", "Tatoo", "Computer", 1234, 123.5):
    test.method1(w)
    # print(test.__dict__)   # line shows there aren't attributes inside instances
