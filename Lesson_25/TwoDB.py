"""
Создать 2 таблицы в Базе Данных
Одна будет хранить текстовые данные (1 колонка), другая числовые (1 колонка).
Есть список, состоящий из чисел и слов.
1) Если элемент списка - слово, то записать его в соответствующую таблицу,
затем посчитать длину слова и записать её в числовую таблицу
2) Если элемент списка число, то записать его в таблицу чисел, если оно чётное;
или записать во вторую таблицу слово: «нечётное», если число нечётное.
3) Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
Если меньше, то обновить 1 запись в первой таблице на «hello».
"""
import sqlite3
from itertools import zip_longest


cx = sqlite3.connect(":memory:")
cu = cx.cursor()
cu.executescript("""
    CREATE TABLE tab1(id INTEGER PRIMARY KEY AUTOINCREMENT, col INTEGER);
    CREATE TABLE tab2(id INTEGER PRIMARY KEY AUTOINCREMENT, col TEXT);
    """)
cx.commit()

for i in [5, "banana", 7, "apple", 3, 4, 9, "orange", "chery"]:
    if isinstance(i, int):
        cu.execute("""
        INSERT INTO {0}(col) 
        VALUES('{1}');
        """.format(*[('tab1', i), ('tab2', 'odd')][i % 2]))
    elif isinstance(i, str):
        cu.executescript(f"""
        INSERT INTO tab2(col) VALUES('{i}');
        INSERT INTO tab1(col) VALUES('{len(i)}');
        """)

cu.execute(
    ["UPDATE tab2 SET col='hello' WHERE id=1;",
     "DELETE FROM tab2 WHERE id=1;"][cu.execute("SELECT COUNT(*) FROM tab1").fetchone()[0] > 5])

print("TAB1 / TAB2")
for i in zip_longest(cu.execute("SELECT * FROM tab1").fetchall(),
                     cu.execute("SELECT * FROM tab2").fetchall(),
                     fillvalue='(    )'):
    print(*i)
cx.close()
