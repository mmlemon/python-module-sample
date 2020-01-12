"""
	folder1内、同一階層を参照する
"""
import folder11

def folder12method():
	return "folder12method"

def folder12method_folder11call():
	folder11class = folder11.folder11class()
	return 'folder11.var:{}, method:{}, class_method:{}'.format(folder11.folder11var, folder11.folder11method(), folder11class.folder11class_method())

if __name__ == "__main__":
	# 同一階層のfolder11.pyの内容を呼ぶ
	print(folder12method_folder11call())