# the code library to be used for all filesystem operations
import tempfile, os

def outputSeasonToTxt():
    pass

def outputSeasonToCSV():
    print(os.path)
    pass

"""

"""
def createFolder(parent_path, foldername, filesToAdd):
    path = os.path.join(os.getcwd(), parent_path, foldername)
    os.mkdir(path) #Format the title (remove |)


"""

""" 
def writeCalendarToDisk(calendar):
    directory = tempfile.mkdtemp()
    f= open(os.path.join(directory, 'example.ics'), 'wb')
    f.write(calendar.to_ical())
    f.close()
# createFolder(Resources.Constants.SEASONS_FOLDER, "Round 1")
print(os.getcwd())