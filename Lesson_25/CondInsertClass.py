"""
Создайте метод класса для работы с БД.
Если передан 1 аргумент (любой) - вставить в таблицу БД запись с числом 3.
Если переданы 2 аргумента и второй является числом - удалить из таблицы запись 1.
Если переданы 3 аргумента и третий является числом (значения первых двух неизвестны) - обновить запись 3 на число 77.
"""
import sqlite3


class CondInsert:
    cx = sqlite3.connect(":memory:")
    cu = cx.cursor()
    cu.execute("CREATE TABLE tmp_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 INTEGER)")
    cx.commit()

    @classmethod
    def insert(cls, *args):
        x = len(args)
        if 1 <= x <= 3 and isinstance(args[x - 1], object if x == 1 else int):
            cls.cu.execute(["DELETE FROM tmp_tab WHERE id=1",
                            "UPDATE tmp_tab set col1=77 WHERE id=3",
                            "INSERT INTO tmp_tab(col1) VALUES(3)"][x - 2])
        cls.cx.commit()

    @classmethod
    def show_n_close(cls):
        print("TABLE:")
        print(*cls.cu.execute("SELECT * FROM tmp_tab"), sep="\n")
        cls.cx.close()


# TESTS:
for i in range(3):                # 1st condition met
    CondInsert.insert(i)

CondInsert.insert(6, "5")         # 2nd condition isn't met
CondInsert.insert("6", 5)         # 2nd condition met

CondInsert.insert("88", 88, "5")  # 3rd condition isn't met
CondInsert.insert("88", 88, 5)    # 3rd condition met

CondInsert.show_n_close()
