import sqlite3 as sql


def delete_user(id):
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.executescript("""
            DELETE FROM users
            WHERE id == '{}'  
        """.format(id))
        con.commit()


def clear_db():
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.executescript("""
            DELETE FROM users  
        """.format(id))
        con.commit()


def set_date(id, date_from):  # устанавливает дату с которой не курит конкретный id
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM users
            WHERE id == '{}'  
        """.format(id))
        records = cur.fetchall()
        if len(records) == 0:
            cur.executescript("""
            INSERT INTO users (id, date_from) VALUES ('{}', '{}')  
            """.format(id, date_from))
        else:
            cur.executescript("""
            UPDATE users
            SET date_from='{}'
            WHERE id == '{}' 
            """.format(date_from, id))
        con.commit()


def get_from(id):  # получение даты конкретного id
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT date_from FROM users
            WHERE id == '{}'  
        """.format(id))
        records = cur.fetchall()
        return records[0][0].split(' ')[0]


def get_users():  # возвращает список id
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT id FROM users 
        """.format(id))
        records = cur.fetchall()
        return [i[0] for i in records]


def notification():
    print("[INFO] Start sending notifications")
    # возвращает список с id пользователей, которые сейчас участвуют
    ids = get_users()
    for id in ids:
        pass
