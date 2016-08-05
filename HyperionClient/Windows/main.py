import win32api
import win32gui

processHandle = -1
NowPlaying = ""

VK_MEDIA_NEXT_TRACK = 0xB0      # Next Track key
VK_MEDIA_PREV_TRACK = 0xB1      # Previous Track key
VK_MEDIA_PLAY_PAUSE = 0xB3      # Play/Pause Media key

def prettyprintProcesses(titles):
    i = 0
    output = []

    for title in titles:
        if len(title[0]) == 0:
            pass
        else:
            i += 1
            print str(i) + ": " + title[0]
            output.append((i, title[1]))

    print ""
    return output

def printHeader():
    print "\n#########################################################"
    print "# Hyperion Client - Collaborative playlists on the fly! #"
    print "#########################################################\n"

def printMenu():
    print "1: Current Song"
    print "2: Play/Pause"
    print "3: Next"
    print "4: Previous\n"


def getAllWindowTitles():
    titles = []

    def callback(handle, lParam):
        if win32gui.IsWindowVisible(handle):
            titles.append((win32gui.GetWindowText(handle), handle))

    win32gui.EnumWindows(callback, 0)
    return titles


def getWindowTitle(handle):
    return win32gui.GetWindowText(handle)



def setup():
    printHeader()
    print "Please select Spotify from the following list of processes.\n"

    titles = getAllWindowTitles()
    options = prettyprintProcesses(titles)

    userChoice = raw_input("Process: ")

    for option in options:
        if int(option[0]) == int(userChoice):
            global processHandle
            processHandle = option[1]

            print "\nSetup Complete!"
            break

def getCurrentSong():
    title = getWindowTitle(processHandle)

    if title == "Spotify":
        return "No Song Playing"
    else:
        return title

def simPlayPause():
    hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)

def simNextSong():
    hwcode = win32api.MapVirtualKey(VK_MEDIA_NEXT_TRACK, 0)
    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, hwcode)

def simPrevSong():
    hwcode = win32api.MapVirtualKey(VK_MEDIA_PREV_TRACK, 0)
    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0)

if __name__ == '__main__':
    setup()

    while True:
        printHeader()
        printMenu()

        userChoice = int(raw_input("Hyperion :~ "))

        if userChoice == 1:
            print "\n" + getCurrentSong()
        elif userChoice == 2:
            simPlayPause()
        elif userChoice == 3:
            simNextSong()
        elif userChoice == 4:
            simPrevSong()
        else:
            print "[Error} Invalid Command."







