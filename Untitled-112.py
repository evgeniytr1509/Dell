message = "Hello my little friend!"

print(message.find("li", 5, 15))  # 9
print(message.find("li", 10, 15))  # -1
print(message.find("li"))  # 9


articles = "An ocean that cannot be crossed."
#print (articles_dict)

#for item in articles_dict:
print(articles.find("c"))

def find_articles(key, letter_case=False):
    new_dict = []
    for item in articles_dict:
        if item == key:
            new_dict.append(articles_dict.get(item))
            
    return new_dict 


    def find_articles(key, letter_case=False):
    result = []
    for item in articles_dict:
        if (articles_dict.find("Ocean")) != 0:
            result.append(articles_dict.get(item))
          
    return result 