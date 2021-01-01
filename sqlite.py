import sqlite3
from mimesis import Generic
generic = Generic('en')


def create_table():
    conn = sqlite3.connect('twitter.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE if not exists twitterusers(id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(40) NOT NULL, displayname VARCHAR(40) NOT NULL,  password VARCHAR(40) NOT NULL)")
    cursor.close()
    conn.close()


def data_entry():
    conn = sqlite3.connect('twitter.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE twitterusers SET displayname='steviethewonderdude' where displayname='steve-o'")
    cursor.execute(
        "UPDATE twitterusers SET displayname='DMG' where displayname='davey'")
    conn.commit()
    cursor.close()
    conn.close()


def insert_users(count=500, locale='en'):
    conn = sqlite3.connect('twitter.db')
    cursor = conn.cursor()

    for _ in range(count):
        insert_query = "INSERT INTO twitterusers(username, password, displayname)VALUES('"+generic.person.username() + \
            "','"+generic.person.password().replace("'", "")+"', '" + \
            generic.person.full_name().replace("'", "")+"')"
        print(insert_query)
        cursor.execute(insert_query)
    conn.commit()
    cursor.close()
    conn.close()


create_table()
insert_users()
data_entry()
