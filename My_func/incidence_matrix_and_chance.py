import numpy as np
def incidence_matrix(sum_dict_NER, all_dict_NER):
    #Создаем матрицу заполненую нулями
    matrix=np.zeros((len(sum_dict_NER),len(sum_dict_NER)))

    #Получаем список ключей из словаря
    list_key=list(sum_dict_NER.keys())
    #Заполняем матрицу инцидентности
    for dict in all_dict_NER:
        for i in range(len(sum_dict_NER)):
            for j in range(i+1,len(sum_dict_NER)):
                if (list_key[i] in dict) and (list_key[j] in dict):
                    matrix[i][j]=matrix[i][j]+float(1)
                    matrix[j][i]=matrix[i][j]
    return matrix

def chance(matrix_incidence, len_all_NER):
    #Копируем массив инцидентности
    matrix_chance=np.copy(matrix_incidence)
    #Вычисляем вероятность употребления двух NER в одном сообщении
    for i in range(len(matrix_chance)):
        for j in range(len(matrix_chance[0])):
            matrix_chance[i][j]=matrix_chance[i][j]/len_all_NER
    #Округляем массив
    matrix_chance=np.round(matrix_chance, decimals=2) 
    return matrix_chance