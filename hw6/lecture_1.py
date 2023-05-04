# a = open('test.txt', 'w+', encoding='utf-8')
# a.write("""читати дані
# записувати дані
# дописувати дані
# """)
# a.seek(0)
# l = a.readlines()
# print(a.tell())
# print(l)
# a.close()

# CONTEXT MANEGER
# with open('test.txt', 'r+', encoding='utf-') as f:
#     print(f.read(5))
#     f.seek(0)
#     f.write("Testing")
#     print(f.read())
#     print(f.closed)

# print(f.closed)ч

# casefold

# import shutil

# path_to_archive = shutil.make_archive("backup", "zip", "hw6")

# shutil.unpack_archive(path_to_archive, "/hw6")
