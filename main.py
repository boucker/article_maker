from bullshit import generator
title = input("title:")
length = int(input("length:"))
content = generator(title, length)
print(title)
print(content)
