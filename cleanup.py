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
    if isAudio(filename):
        shutil.move(os.path.join(downloads, filename), audio)
    elif isDocument(filename):
        shutil.move(os.path.join(downloads, filename), docs)
    elif isImage(filename):
        shutil.move(os.path.join(downloads, filename), images)
    elif isInstall(filename):
        shutil.move(os.path.join(downloads, filename), install)
    elif isVideo(filename):
        shutil.move(os.path.join(downloads, filename), videos)
    elif (not isDirectory(filename)):
        shutil.move(os.path.join(downloads, filename), misc)
    else:
        continue
