import os
from os import listdir

FOLDER = "C:/Users/acarp/Desktop/Temporary"     # This must use foward slashes and not end with a slash
OUTPUT_FILE = "image_list.txt"
IMAGE_FILES = ["png", "jpg"]  # No gif or bmp allowed

# Write the start of the arrays
imageFilenameListString = "imageList = \n{\n"
imageNameString = "imageNames = \n{\n"


# Get the list of files
fileList = os.listdir(FOLDER)
for name in fileList:
    # Create the full path
    # Assume forward slash.  It's probably not "correct", but it makes things easier
    combinedPath = FOLDER + "/" + name
    # Get the file type
    fileType = name[-3:]
    # Only save the file if it's an image
    if fileType in IMAGE_FILES:
        #print(combinedPath)
        imageFilenameListString += "    \"" + combinedPath + "\",\n"
        imageNameString += "    \"\", -- Description for file \'" + name + "\'\n"

# Close the array
imageFilenameListString += "}\n\n"
imageNameString += "}"

# Open the output file
with open(OUTPUT_FILE, "w") as outFile:
    outFile.write(imageFilenameListString)
    outFile.write(imageNameString)