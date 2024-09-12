def send_email(message,recipient,sender = "univerity.help@gmail.com"):
    if("@"and(".com"or".ru"or".net")) not in (recipient or sender) or("@" or(".com"or"ru"or".net")) not in (recipient or sender):
        # создаём  1 условие
        print(f"Невозможно отправить письмо с адреса {sender}на адрес {recipient}")
    elif recipient == sender:
        # создём 2 условие
        print("Нельзя отправить письмо самому себе!")
        # создаём 3 условие
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
        # создаём 4 условие
    elif sender !="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        # вывод результата
        send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
        send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
                   sender='urban.info@gmail.com')
        send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
        send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')