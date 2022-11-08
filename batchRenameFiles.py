import os

folderpath = r'C:\Users\Adjutant_013\下载\test'
filelist = os.listdir(folderpath)
for files in filelist:
    newfilename = files + '.jpg'
    os.rename(folderpath+'/'+files, folderpath+'/'+newfilename)
    print(files, '--->', newfilename)
