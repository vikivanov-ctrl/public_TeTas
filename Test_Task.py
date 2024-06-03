#Библиотеки питона

#Мои функции
from My_func.telegram_take_message import start_client, take_message
from My_func.filter_for_messages import filt_all_message
from My_func.take_NER_from_messages import NER_from_messages, sum_NER
from My_func.incidence_matrix_and_chance import incidence_matrix, chance
from My_func.draw_graf import draw_Graf

#Глобальные переменные

#Инструкция по получению : https://telegra.ph/Instrukciya-po-polucheniyu-Api-id-i-Api-hash-11-03

#Telegram_api phone / вставить своё
phone_number=

#Telegram_api id / вставить своё
api_id = 

#Telegram_api hash / вставить своё
api_hash = 

#Telegram_api title / вставить своё
api_name =

#Начало 
def main():
    #Список для сбора всех сообщений
    all_messages=[]

    #Сколько сообщений берём из одного канала
    limit_messages=1

    #Список 30 новостных каналов/нужно быть подписаным на них
    news_canals=["КОНТЕКСТ", "Срочно, Сейчас","Раньше всех. Ну почти.",
                "Хлам 18+", "Москвич | Москва и новости столицы", "Кровавая барыня", 
                "ЖЕСТЬ ВИДЕО | ЧП 18+", "Топор 18+","Прямой Эфир",
                "РИА Новости", "Mash", "ЧП Сегодня | Россия",
                "Travel media","Русская Община ZOV", "Новости Москвы",
                "Медуза — LIVE","BBC News | Русская служба","Varlamov News",
                "Осторожно, новости", "Baza", "Ньюсач/Двач",
                "SHOT","BRIEF","Readovka",
                "РБК","Коммерсантъ","СОЛОВЬЁВ",
                "RT на русском", "Рыбарь","ТАСС"
                ]

    # Запуск асинхронной функции для сбора новостей из канала
    client=start_client(api_id, api_hash, api_name)

    #Сбор сообщений / каждое сообщение - отдельный список в общем списке
    all_messages=client.loop.run_until_complete(take_message(limit_messages,news_canals,all_messages,phone_number,client))
   
    #Передаём полученные сообщения функции фильтрации текста в сообщениях
    all_messages=filt_all_message(all_messages) 

    #Получаем словари NER списком
    NER_list=NER_from_messages(all_messages)

    #Принты
    # print("Все NER:")
    # print(NER_list)

    #Считаем сколько раз NER было употреблено 
    sum_NER_dict=sum_NER(NER_list)

    #Принты
    # print("Уникальные NER:")
    # print(sum_NER_dict)

    #Матрица инцидентности
    matrix_incidence=incidence_matrix(sum_NER_dict, NER_list)
    
    # #Принты
    # print("Матрица инцидентности:")
    # for row in matrix_incidence:
    #     print(row)

    #Матрица вероятности употребления
    matrix_chance=chance(matrix_incidence, len(NER_list))

    #Принты
    print("Матрица вероятностей:")
    for row in matrix_chance:
        print(row)

    #Построение графа
    draw_Graf(sum_NER_dict, matrix_chance)

if __name__=="__main__":
    main()