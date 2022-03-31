import db_function

db_function.createTables()

work = True

while work:
    oper = int(input("""Операції:
1 - Добавити слово 
2 - Добавити тему 
3 - Показати весь словник
4 - Тест
5 - Вийти
Виберіть операці: """))
    if oper == 1:
        db_function.addWord()
    elif oper == 2:
        db_function.addTopic()
    elif oper == 3:
        db_function.printAllVocabulary()
    elif oper == 4:
        db_function.Test(0)
    elif oper == 5:
        work = False