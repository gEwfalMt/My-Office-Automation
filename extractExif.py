import exifread
import os

filesRoot = r'C:\Users\Adjutant_013\Desktop\test'
filesList = os.listdir(filesRoot)
for i in filesList:
    picFile = open(filesRoot + '/' + i, 'rb')
    picExifInfo = exifread.process_file(picFile)
    picFile.close()
    originalDateTime = str(picExifInfo['Image DateTime'])
    changedDateTime1 = originalDateTime.replace(':', '')
    changedDateTime2 = changedDateTime1.replace(' ', '_')

    oldFileName = filesRoot + '/' + i
    newFileName = filesRoot + '/' + 'IMG_' + changedDateTime2 + oldFileName[oldFileName.index('.'):]

    print(newFileName)
    os.rename(oldFileName, newFileName)
