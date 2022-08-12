# the code library to be used for all filesystem operations
import tempfile, os
import Resources.Constants as Constants
# Read
def readSeasonFromCSV():
    pass

def readFromFilesystem():
    pass

# Write

"""
THis will output a given season to a text file
"""
def outputSeasonToTxt(seasonToOutput):
    pass

"""
This will iterate through a season and output to a CSV file
"""
def outputSeasonToCSV(seasonToOutput):
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

# Validation

"""
This will check if the string is valid, similar to isStringValidFilepath but this will additionally return a valid string 
"""
def validateStringForFilepath(stringToValidate) -> str:
    for invalidChar in Constants.DISABLED_FILEPATH_CHARS:
        if invalidChar in stringToValidate:

            #split string on invalid char
            print("invalid char:"+ invalidChar +" found within "+ stringToValidate)
            validString = ""
            splitString = stringToValidate.split(invalidChar, -1) #Should change -1 (max no of splits) to max filename size (-1 denotes as many as possible)
            
            #return string together
            for innerString in splitString:
                validString += innerString

            return validateStringForFilepath(validString) # not very efficient
    # The string is already valid
    print("String: \""+stringToValidate+"\" already valid")
    return stringToValidate


"""
takes a string and checks that it does not contain any invalid characters set in Resources.Constants.DISABLED_FILEPATH_CHARS
"""
def isStringValidFilepath(stringToValidate) -> bool:
    if(stringToValidate):
        for invalidChar in Constants.DISABLED_FILEPATH_CHARS:
            if invalidChar in stringToValidate:
                return False
        return True
    return False