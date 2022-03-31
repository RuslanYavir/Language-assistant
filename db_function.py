import sqlite3


def createTables():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS vocabulary(id INTEGER, word TEXT, translate TEXT, topic INTEGER) """)
        cursor.execute(""" CREATE TABLE IF NOT EXISTS topics(id INTEGER, name TEXT) """)


def checkLastId(table):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM {table} WHERE ROWID IN ( SELECT max( ROWID ) FROM {table} )")
        lastID = cursor.fetchone()
        if lastID == None:
            return -1
        else:
            return lastID[0]


def addTopic():
    topicName = input("Введіть назву теми: ")
    id = checkLastId("topics") + 1
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(f" INSERT INTO topics(id, name) VALUES(?, ?) ", (id, topicName))


def allTopics():
    all = ""
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute("""SELECT * from topics""")
        records = cursor.fetchall()
        for row in records:
            all += str(row[0]) + " - " + str(row[1]) + "\n"
    return all


def addWord():
    word = input("Введіть слово: ")
    translate = input("Введіть переклад: ")
    id = checkLastId("vocabulary") + 1
    topics = allTopics()
    topic = input(f"Теми: \n {topics} \n Виберіть тему: ")
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(f" INSERT INTO vocabulary(id, word, translate, topic) VALUES(?, ?, ?, ?) ", (id, word, translate, topic))


def printAllVocabulary():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(""" SELECT * FROM vocabulary """)
        records = cursor.fetchall()

        for record in records:
            print(record)

def Test(topic):
    c = 0
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(f""" SELECT * FROM vocabulary WHERE topic == {topic} and id >= 50""")
        records = cursor.fetchall()
        l = len(records)

        for record in records:
            print(record[1])
            testtranslate = input()
            if record[2] == testtranslate:
                print("Правильно!")
                c += 1
            else:
                print(record[2])

        print(f"Результат: {c}/{l}")