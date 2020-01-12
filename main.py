
"""
folder1/foder11.pyの内容を呼び出す
"""
from folder1 import folder11
from folder2 import folder21

print(folder11.folder11var)
print(folder11.folder11method())

folder11class = folder11.folder11class()
print(folder11class.folder11class_method())

folder21_class = folder21.folder21class()
print(folder21_class.folder21method())