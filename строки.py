message = "Hello my little friend!"

print(message.find("li", 5, 15))  # 9
print(message.find("li", 10, 15))  # -1
print(message.find("li"))  # 9

print ("*************")
message1 = "Hello my little friend!"

print(message1.index("li", 5, 15))
print(message1.index("li", 5, 15))

print ("*************")

message = "Hello, my little fr1iend. Today is a v1ery good day."
words = message.split(" ")
sentences = message.split(". ")
print(words)
print(sentences)

print ("*************")
words = [
    "Hello,",
    "my",
    "little",
    "friend.",
    "Today",
    "is",
    "a",
    "very",
    "good",
    "day.",
]
sentences = ["Hello, my little friend", "Today is a very good day."]

message_from_words = " ".join(words) #" " символ в промежутках между словами
message_from_sentences = ". ".join(sentences)

print(message_from_words)  # Hello, my little friend. Today is a very good day.
print(message_from_sentences)  # Hello, my little friend. Today is a very good day.

print ("******************")
message = "В темной комнате все кошки черные (наверное)"
square_brackets = message.replace("(", "[").replace(")", "]")
clear_brackets = message.replace("(", "").replace(")", "") # замена на пробел

print(square_brackets)  # В темной комнате все кошки черные [наверное]
print(clear_brackets)  # В темной комнате все кошки черные наверное

print ("******************")
print('TestHook'.removesuffix('Hook'))  # Test
print('TestHook'.removesuffix('Test'))  # TestHook