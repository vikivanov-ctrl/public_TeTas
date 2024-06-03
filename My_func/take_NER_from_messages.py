from natasha import( 
    Segmenter, 
    MorphVocab, 
    NewsEmbedding,
    NewsMorphTagger, 
    NewsSyntaxParser,
    NewsNERTagger,
    NamesExtractor, 
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,
    Doc
)

#Функция извлечения и нормализации NER
def NER_from_messages(all_messages) -> dict:
    #Словарь для NER
    dict_NER={}
    #Список для их хранения
    list_dict_NER=[]
    #Начальные настройки
    segmenter=Segmenter()
    morph_vocab=MorphVocab()

    emb=NewsEmbedding()
    morph_tagger=NewsMorphTagger(emb)
    syntax_parser=NewsSyntaxParser(emb)
    ner_tagger=NewsNERTagger(emb)

    #Экстракторы для дальнейшего увеличения функционала
    name_extractor=NamesExtractor(morph_vocab)
    dates_extractor=DatesExtractor(morph_vocab)
    money_extractor=MoneyExtractor(morph_vocab)
    addr_extractor=AddrExtractor(morph_vocab)
    #Находим NER в каждом сообщении в отдельности
    for messages in all_messages:
        for message in messages:
            doc=Doc(message)
            doc.segment(segmenter)
            doc.tag_morph(morph_tagger)
            doc.parse_syntax(syntax_parser)
            doc.tag_ner(ner_tagger)
            for token in doc.tokens:
                token.lemmatize(morph_vocab)
            for span in doc.spans:
                span.normalize(morph_vocab)
                if span.normal not in dict_NER:
                    dict_NER[span.normal]=1
                else:
                    dict_NER[span.normal]+=1
        list_dict_NER.append(dict_NER)
        #Чистим словарь
        dict_NER={}    
    return list_dict_NER

#Функция подсчёта общего количества употребления одного NER
def sum_NER(dict_NER_list):
    sum_dict={}
    for dict in dict_NER_list:
        for key in dict:
            if key not in sum_dict:
                sum_dict[key]=dict[key]
            else:
                sum_dict[key]+=1
    return sum_dict
