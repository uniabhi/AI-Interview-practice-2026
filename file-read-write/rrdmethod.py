# import os

# # f = open('abhi.txt', 'r')
# # while True:
# #     line = f.readline()
# #     print(line)
# #     if not line:
# #         print(line, type(line))
# #         break


# f = open("abhi.txt", 'w')
# lines = ['Line 1\n', 'Line 2 \n', 'Line 3 \n']
# f.writelines(lines)
# f.close()

def process(chunk):
    # Yahan apna asli kaam likho
    pass

with open("dressage-analysis.mp4", "rb") as f:
    while chunk:= f.read(8192):
        process(chunk)