# списки
"""List 02"""
from typing import List
text = "Hello world"
ch = 'l'

def indexes_ch(text: str, ch: str):
    result = []
    for index, element in enumerate(text):
        if element == ch:
            result.append(index)
    return result, ch, len(result)

# def indexes_ch(text, ch):
#     result = []
#     for index, element in enumerate(text):
#         if element == ch:
#            result.append(index)
#     return result, ch, len(result)

if __name__ == "__main__":
    text1 = """Consequat suscipit amet ut. Et ipsum cum 
    ea accusam kasd hendrerit lorem dignissim et kasd 
    diam consetetur. Ipsum est amet takimata sit ut 
    amet et illum sadipscing magna aliquam est liber 
    sit feugait duis ullamcorper sanctus. 
    Magna adipiscing gubergren nulla ut et."""
    result = indexes_ch(text1, 's')
    print(f"In text symbol {result[1]} find {result[2]} times")

