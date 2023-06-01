import os
import re


foldPath = input('输入文件夹路径：')
dirList = os.listdir(foldPath)
pattern = re.compile('[\S].+[[|【]')
for fold in dirList:
    newName = re.search(pattern, fold)
    if newName:
        newFoldName = newName.group()[:-1]
        os.rename(foldPath+'/'+fold, foldPath+'/'+newFoldName)
        print(fold, '--->', newFoldName)
