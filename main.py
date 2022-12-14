from Test import Test

question_test = [
    '''1) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, Г, И, М, Р, Я.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: А — 010, Б — 011, Г — 100.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова МАГИЯ?\n 1 : 12\n 2 : 13\n 3 : 14\n''',

    '''2) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, Г, И, М, Р, Я.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: А — 010, Б — 00, Г — 101.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова МАГИЯ?\n 1 : 14\n 2 : 15\n 3 : 16\n''',

    '''3) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, И, К, Л, О, С.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: А — 001, И — 01, С — 10.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова КОЛОБОК?\n 1 : 21\n 2 : 22\n 3 : 23\n''',

    '''4) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, Г, И, Н, Р, Т.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: Г — 110, И — 01, Т — 10.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова БАРАБАН?\n 1 : 23\n 2 : 24\n 3 : 25\n''',

    '''5) По каналу связи передаются сообщения, содержащие только семь букв: Б — 00, К — 010, Л — 111.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: А — 010, Б — 011, Г — 100.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова АБСЦИССА?\n 1 : 20\n 2 : 21\n 3 : 22\n''',

    '''6) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, Д, Е, И, Н.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: А — 110, Б — 01, И — 000.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова ВВЕДЕНИЕ?\n 1 : 23\n 2 : 24\n 3 : 25\n''',

    '''7) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, Г, Й, К, Л.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: Б — 00, Г — 010, К — 101.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова БАЛАЛАЙКА?\n 1 : 22\n 2 : 23\n 3 : 24\n''',

    '''8) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, Д, О, Р, Т.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: Б — 01, Д — 001, Р — 100.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова ВОДОВОРОТ?\n 1 : 22\n 2 : 23\n 3 : 24\n''',

    '''9) По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, К, Р, Т.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: Б – 010, Т – 011.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова КАТАРАКТА?\n 1 : 19\n 2 : 20\n 3 : 21\n''',

    '''10) По каналу связи передаются сообщения, содержащие только семь букв: А, В, Е, З, И, Н, О, Р.
   Для передачи используется двоичный код, удовлетворяющий условию Фано.
   Кодовые слова для некоторых букв известны: А — 101, В — 010, И — 00.
   Какое наименьшее количество двоичных знаков потребуется для кодирования слова НЕВЕЗЕНИЕ?\n 1 : 23\n 2 : 24\n 3 : 25\n''',
]
questions = [
    Test(question_test[0], "14"),
    Test(question_test[1], "15"),
    Test(question_test[2], "23"),
    Test(question_test[3], "23"),
    Test(question_test[4], "22"),
    Test(question_test[5], "23"),
    Test(question_test[6], "23"),
    Test(question_test[7], "24"),
    Test(question_test[8], "20"),
    Test(question_test[9], "23"),
]
def run_test(questions):
    count = 0
    for question in questions:
        print(question.vopros)
        otvet = input("Введите номер правильного ответа: ")
        if otvet == question.otvet:
            count += 1
            print("Правильно!")
        else:
            print("Неправильно")
        print('\n')
    if count <= 4:
        print("Оценка: неудовлетворительно, " + str(count) + " из " + str(len(questions)))
    if count == 5 or count == 6:
        print("Оценка: удовлетворительно, " + str(count) + " из " + str(len(questions)))
    if count == 7 or count == 8:
        print("Оценка: хорошо, " + str(count) + " из " + str(len(questions)))
    if count == 9 or count == 10:
        print("Оценка: отлично, " + str(count) + " из " + str(len(questions)))

run_test(questions)