import os


# 多个文件夹里的文件改名

def batchManyFoldFiles(fatherFoldPath):
    foldList = os.listdir(fatherFoldPath)
    for fold in foldList:
        sonFolderPath = fatherFoldPath + '/' + fold
        fileList = os.listdir(sonFolderPath)
        for files in fileList:
            newFileName = files + '.jpg'
            os.rename(sonFolderPath+'/'+files, sonFolderPath+'/'+newFileName)
            print(files, '--->', newFileName)


# 单个文件夹里文件改名

def batchOneFoldFiles(folderPath):
    fileList = os.listdir(folderPath)
    for files in fileList:
        newFileName = files + '.jpg'
        os.rename(folderPath+'/'+files, folderPath+'/'+newFileName)
        print(files, '--->', newFileName)



foldPath = input('输入文件夹路径：')
selectedFunction = input('选择批量修改的方式：\na、修改多个文件夹里的文件\nb、修改单个文件夹里文件\n')
if selectedFunction == 'a':
    batchManyFoldFiles(foldPath)
else:
    batchOneFoldFiles(foldPath)
