"""
Создать таблицу в Базе Данных с тремя колонками (id, 2 -text, 3 - text).
Заполнить её с помощью INSERT данными (3 записи).
Удалить с помощью DELETE 2 запись.
Обновить значения 3-ей записи на: hello world с помощью UPDATE.
Записать данные с таблицы в файл в три колонки.
"""
import sqlite3

cx = sqlite3.connect(":memory:")
cu = cx.cursor()
cu.executescript("""
    CREATE TABLE tab1(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 TEXT, col2 TEXT);
    INSERT INTO tab1 (col1, col2) VALUES ("Robot", "says");
    INSERT INTO tab1 (col1, col2) VALUES ("all", "humans");
    INSERT INTO tab1 (col1, col2) VALUES ("must", "die!");
    DELETE FROM tab1 WHERE id=2;
    UPDATE tab1 SET col1="hello", col2="world" WHERE id=3;
    """)
cx.commit()

with open("fromDB.txt", "w") as txt:
    for row in cu.execute("SELECT * FROM tab1"):
        print(*map(str, row), file=txt)

cx.close()
