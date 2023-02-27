# ключ - 1 2 3, значения one two three
# numbers = [{
#     1: "one",
#     2: "two",
#     7: "seven",
# },
# {
#     7: "seven",
#     5: "five",
#     6: "six"
# },
# {
#     7: "seven",
#     8: "eith",
#     9: "nine"
# },]

# result = []
# for articles in numbers:
#     for value in articles.values():
#         if (value.find("ev") != -1):
#             result.append(articles)
#         continue
# print (result)





articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

result = []
for articles in articles_dict:
    for key, value in articles.items():
        if type(value) == int:
            continue       
        if (value.find("cean")) != -1:
            result.append(articles)
            continue
print (result)
        


