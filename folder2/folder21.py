"""
folder1/
	folder11.py <--- 呼ばれる側
folder2/
	folder21.py <--- 呼ぶ側（このファイル）
"""
import sys
sys.path.append("../")
from folder1 import folder11

class folder21class(object):
	def __init__(self):
		return
	def folder21method(self):
		folder11class = folder11.folder11class()
		return 'folder11.var:{}, method:{}, class_method:{}'.format(folder11.folder11var, folder11.folder11method(), folder11class.folder11class_method())

if __name__ == "__main__":
	folder21class = folder21class()
	print(folder21class.folder21method())