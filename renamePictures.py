import exifread
import os


def renameFromDatetime(filesRoot, filesList):
    j = 1
    for i in filesList:
        picFile = open(filesRoot + '/' + i, 'rb')
        picExifInfo = exifread.process_file(picFile)
        picFile.close()
        try:
            originalDateTime = str(picExifInfo['EXIF DateTimeOriginal'])
        except:
            continue
        else:
            changedDateTime1 = originalDateTime.replace(':', '')
            changedDateTime2 = changedDateTime1.replace(' ', '_')

        oldFileName = filesRoot + '/' + i
        newFileName = filesRoot + '/' + 'IMG_' + changedDateTime2 + oldFileName[oldFileName.index('.'):]

        print(newFileName)
        try:
            os.rename(oldFileName, newFileName)
        except:
            newFileNameChange = filesRoot + '/' + 'IMG_' + changedDateTime2 + '（' + str(j) + '）' + oldFileName[oldFileName.index('.'):]
            j = j + 1
            os.rename(oldFileName, newFileNameChange)


def renameWithCustomizePattern(filesRoot, filesList, customizePattern):
    for i in filesList:
        oldFileName = filesRoot + '/' + i
        newFileName = filesRoot + '/' + i[:i.index('.')] + '_' + customizePattern + i[i.index('.'):]
        print(oldFileName, '->', newFileName)
        os.rename(oldFileName, newFileName)


foldPath = input('输入文件夹路径：')
filesList = os.listdir(foldPath)
selectedFunction = input('选择批量修改的方式：\na、按拍摄时间修改\nb、添加自定义后缀\n请选择：')
if selectedFunction == 'a':
    renameFromDatetime(foldPath, filesList)
else:
    customizePattern = input('输入自定义后缀：')
    renameWithCustomizePattern(foldPath, filesList, customizePattern)
