import networkx as nx
import matplotlib.pyplot as plt

def draw_Graf(sum_NER_dict, matrix_chance):
    #Получаем список ключей из словаря
        list_key=list(sum_NER_dict.keys())
        #Создаём граф
        weighted_graph=nx.Graph()
        #Добавляем вершины графа
        weighted_graph.add_nodes_from(list_key)
        #Создаём список tuple чтобы добавить связи
        tuples=[]
        for i in range(len(matrix_chance)):
            for j in range(len(matrix_chance[0])):
                if matrix_chance[i][j]!=0:
                    tuples.append((list_key[i],list_key[j],matrix_chance[i][j]))
        #Создаём связи
        weighted_graph.add_weighted_edges_from(tuples)
        #Визуализация графа
        #Метод позиционирование вершин
        pos = nx.spring_layout(weighted_graph)
        edge_labels = {(u, v): d['weight'] for u, v, d in weighted_graph.edges(data=True)}
        nx.draw(weighted_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue", font_size=8, font_color="black", edge_color="gray")
        nx.draw_networkx_edge_labels(weighted_graph, pos, edge_labels=edge_labels)
        plt.title("Weighted Graph NER")
        #Показываем граф
        plt.show()
        return