def find_articles(key, letter_case=False):
    result = []
    for item in articles_dict:
        if (articles_dict.find("ocean")) != 0:
            result.append(articles_dict.get(item))
          
    return result 


def find_articles(key, letter_case=False):
    result = []
    for item in articles_dict:
        pos = key.find('title' or 'author')
        if pos == True:
            result.append({'author': article['author'], 'title': article['title'], 'year': article['year] })
    return result 


#def find_articles(key, letter_case=False):
#     new_dict = []
#     for item in articles_dict:
#         if item == key:
#             new_dict.append(articles_dict.get(item))
            
#     return new_dict   