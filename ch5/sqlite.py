import sqlite3
import csv


def execute_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    conn.commit()
    conn.close()


def select_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    rows = c.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    db_name = 'db.sqlite'
    print('建立資料庫及資料表')
    cmd = 'CREATE TABLE record (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, shop TEXT)'
    execute_db(db_name, cmd)
    input()
    print('插入測試資料')
    cmd = 'INSERT INTO record (item, price, shop) VALUES ("PS4測試機", 1000, "測試賣家")'
    execute_db(db_name, cmd)
    input()
    print('更新資料')
    cmd = 'UPDATE record SET shop="hahow 賣家" where shop="測試賣家"'
    execute_db(db_name, cmd)
    input()
    print('插入多筆資料')
    with open('ezprice.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cmd = 'INSERT INTO record (item, price, shop) VALUES ("%s", %d, "%s")' % (row['品項'], int(row['價格']), row['商家'])
            execute_db(db_name, cmd)
    input()
    print('選擇資料')
    cmd = 'SELECT * FROM record WHERE shop="GOHAPPY"'
    for row in select_db(db_name, cmd):
        print(row)
