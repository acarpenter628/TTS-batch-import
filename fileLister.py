import os
from os import listdir

FOLDER = "C:\\Users\\[User]\\Desktop\\Temporary\\"     # forward slash or backslash is fine, but remember to double up if you're using backslashes
OUTPUT_FILE = "ImageList.txt"
IMAGE_FILES = ["png", "jpg"]  # No gif or bmp allowed

# Write the start of the arrays
imageFilenameListString = "imageList = \n{\n"
imageNameString = "imageNames = \n{\n"

# Clean up the folder name
FOLDER = FOLDER.replace("\\", "/")
if FOLDER[-1] != "/":
    FOLDER = FOLDER + "/"

# Get the list of files
fileList = os.listdir(FOLDER)
for name in fileList:
    # Create the full path
    combinedPath = FOLDER + name
    # Get the file type
    fileType = name[-3:].lower()
    # Only save the file if it's an image
    if fileType in IMAGE_FILES:
        #print(combinedPath)
        imageFilenameListString += "    \"file:///" + combinedPath + "\",\n"  # If you don't throw "file:///" in there, it will still render in TTS, but won't upload through the cloud manager
        imageNameString += "    \"\", -- Description for file \'" + name + "\'\n"

# Close the array
imageFilenameListString += "}\n\n"
imageNameString += "}"

# Open the output file
with open(OUTPUT_FILE, "w") as outFile:
    outFile.write(imageFilenameListString)
    outFile.write(imageNameString)