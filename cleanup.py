import shutil, os, constant
downloads = "C:\\Users\\" + constant.USER + "\\Downloads"
#----------------------------------------------------------
audio = downloads + "\\Audio"
docs =  downloads + "\\Docs"
images = downloads + "\\Images"
install = downloads + "\\Install"
misc = downloads + "\\Misc"
videos = downloads + "\\Videos"

directories = ["Audio", "Docs", "Images", "Install", "Misc", "Videos"]
#----------------------------------------------------------

def isAudio(name):
    for x in constant.AUDIO_EXT:
        if name.endswith(x):
            return True
    return False

def isDirectory(name):
    for x in directories:
        if name == x:
            return True
    return False

def isDocument(name):
    for x in constant.DOC_EXT:
        if name.endswith(x):
            return True
    return False

def isImage(name):
    for x in constant.IMAGE_EXT:
        if name.endswith(x):
            return True
    return False

def isInstall(name):
    for x in constant.INSTALL_EXT:
        if name.endswith(x):
            return True
    return False

def isVideo(name):
    for x in constant.VIDEO_EXT:
        if name.endswith(x):
            return True
    return False

#----------------------------------------------------------
files = os.listdir(downloads)

# Ensure the required folders exist before we start sorting
for x in directories:
    if (not os.path.exists(downloads + "\\" + x)):
        os.makedirs(downloads + "\\" + x)

for filename in files:
    print(type(filename))
    destPath = downloads
    if isAudio(filename):
        destPath = audio
    elif isDocument(filename):
        destPath = docs
    elif isImage(filename):
        destPath = images
    elif isInstall(filename):
        destPath = install
    elif isVideo(filename):
        destPath = videos
    elif (not isDirectory(filename)):
        destPath = misc
    else:
        continue
    sourcePath = os.path.join(downloads, filename)
    destPathComplete = destPath + "\\" + filename
    print(destPathComplete)
    if (os.path.exists(destPathComplete)):
        try:
            shutil.copy(sourcePath, destPath)
            print("File copied successfully.")
  
        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
  
        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")
  
        # For other errors
        except:
            print("Error occurred while copying file.")
        os.remove(sourcePath)
    else:
        try: 
            shutil.move(sourcePath, destPath)
            print("File moved successfully")
        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
  
        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")
        except:
            print("Error occurred while moving file.")

