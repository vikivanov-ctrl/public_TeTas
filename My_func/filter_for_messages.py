import re
import emoji
#Функция фильтрации
def filt_all_message(all_messages) -> list:
    filt_message=[]
    for messages in all_messages:
        for message in messages:
            #Убираем ссылки на каналы
            message=re.sub(r"\[\s*.*\]\(.*\)","",message)
            #Убираем смайлы
            message=emoji.replace_emoji(message, replace="")
            #Убираем лишние переносы строк
            message=re.sub(r"\n+","\n",message)
            #Делаем просто строку
            message=re.sub(r"\n"," ",message)
            #Убираем жирный текст
            message=re.sub(r"\*\*","",message)
            #Убираем зачёркнутый текст
            message=re.sub(r"~~","",message)
            #Убираем @ каналов
            message=re.sub(r"\@\S*","",message)
            #Добавляем в список
            filt_message.append([message])
        
        #Принт
        #print(message, end="\n\n")
    return(filt_message)