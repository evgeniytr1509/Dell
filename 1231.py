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