# f = open('abhi.txt', 'w')

# contents = f.write("i am not in delhi right now")
# print(contents)

with open('abhi.txt', 'w') as f:
    content1 = f.write('i am 28 years old right now in 2026')
print(content1)


with open('abhi.txt', 'r') as f:
    content2 = f.read()
print(content2)