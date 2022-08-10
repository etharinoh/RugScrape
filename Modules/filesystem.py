# the code library to be used for all filesystem operations
import tempfile, os

def outputSeasonToTxt():
    pass

def outputSeasonToCSV():
    print(os.path)
    pass

def createFolder(parent_path, foldername, filesToAdd):
    pass
def writeCalendarToDisk(calendar):
    directory = tempfile.mkdtemp()
    f= open(os.path.join(directory, 'example.ics'), 'wb')
    f.write(calendar.to_ical())
    f.close()
print(os.getcwd())