# f = open('file2.txt', 'r')
# print(f.name)

# f.close()

# with open('file1.txt', 'r') as f:
#     content = f.read()
#     print(content)

"""
1. Taslim
2. Windows
3. Blades
5. Random
"""

# with open('file1.txt', 'r') as f:
#     content = f.readlines()
#     print(content)

"""
['1. Taslim\n', '2. Windows\n', '3. Blades\n', '5. Random\n']
"""

# with open('file1.txt', 'r') as f:
#     content = f.readline()
#     print(content)

"""
1. Taslim
"""

# with open('file1.txt', 'r') as f:
#     content = f.readline()
#     print(content, end="")

#     content = f.readline()
#     print(content, end="")

"""
1. Taslim

2. Windows

# with end=""
1. Taslim
2. Windows
"""

# with open('file1.txt', 'r') as f:
#     for line in f:
#         print(line, end="")

"""
1. Taslim
2. Windows
3. Blades
5. Random
"""

# with open('file1.txt', 'r') as f:
#     content = f.read(13)
#     print(content)

#     print(f.read(13))
#     print(f.read(23))
#     print(f.read(13))

"""
# reads first 13 characters, reads another 13 characters
# reads what's left and stops reading when it reaches the end of the file
# prints an empty string if ran again

1. Taslim
2.
Windows
3. Bl
ades
5. Random


"""

# with open('file1.txt', 'r') as f:
#     size = 5
#     content = f.read(size)
#     iter_x  = 0
#     while len(content) > 0:
#         # print(f"\nlength: {len(content)}\n",content, end="")
#         print(content, end="")
#         # print("\n", f.tell())
#         content = f.read(size)
#     #     iter_x += 1
#     # print('iterations: ', iter_x)

"""
1. Taslim
2. Windows
3. Blades
5. Random
"""

# with open('file1.txt', 'r') as f:
#     content = f.read(13)
#     print(content, end="")
#     f.seek(12)
#     content = f.read(7)
#     print(content)

"""
# seek reads 13 characters and seeks to the 12th character, then reads 7 characters."
1. Taslim
2. . Windo
"""


# w -write
# with open('file3.txt', 'w') as f:
#     pass
"""writes a new file if it doesn't already exist however."""

# with open('file2.txt', 'w') as f:
#     new_content = f.write('Hi,\nThis is Taslim!')

"""
# file2.txt

Hi,
This is Taslim!
"""

# with open('file2.txt', 'w') as f:
#     new_content = f.write("Hi!\nThis is Taslim!")
#     x = f.seek(0)
#     f.write("Again, Hi!")

"""
# Overwrites from the 0th position.
Again, Hi!is Taslim!
"""

# with open('file2.txt', 'w') as f:
#     new_content = f.write("Hi!\nThis is Taslim!")
#     x = f.seek(0)
#     cont_2 = f.write("Again, Hi!")
#     # f.seek(cont_2)
#     x = cont_2
#     # print(x)
#     while x < new_content+1:
#         f.seek(x)
#         f.write("\n")
#         x+=1

"""
writes a new line for every character replaced
"""

# with open('file1.txt', 'r') as rf:
#     with open('file3.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

"""Copies file 1 into file 3"""



# working with pictures
"""we're going to have to open our file in binary mode"""
# with open('download.jpg', 'rb') as rf:
#     with open('img_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

"""copies the entire image into the copy file."""

# with open('download.jpg', "rb") as rf:
#     with open('copy2.jpg', 'wb') as wf:
#         chunk_size = 4000
#         read_chunk = rf.read(chunk_size)
#         while len(read_chunk) > 0:
#             wf.write(read_chunk)
#             read_chunk = rf.read(chunk_size)

""""""