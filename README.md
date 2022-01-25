
# TTS-batch-import
A Tabletop Simulator script to batch import custom tokens or figures for online multiplayer games.  Normally, TTS only lets you import one custom object at a time, which can be very slow and frustrating.

This can be used with the output of TTS_RoomTokenizer - another project I've worked on

## Components
There are several components to this project, and unfortunately there are several steps to use it.  This method is still much faster than importing a large number of custom objects manually.  

**fileLister.py** 
Because TTS doesn't want Lua scripts to be able to affect other files on your hard drive, we can't use the Lua script to get a list of files from a given folder.  This simple Python script is used to generate a list of images that is copied and pasted into the Lua script

**global_template.lua**
This is the Lua script used for the global script in TTS.  It requires user modification before it can be used.

## Usage Instructions

* Collect desired images into a folder
* Modify the `FOLDER` variable at line 4 of `fileLister.py` to include the location of the folder
  * Forward slash or backslash is fine as a folder separator - but remember to double up on backslashes
  * Ending the string with a folder separator is optional
* Run the Python script.  It generates a file called `ImageList.txt`
* Copy the contents of `ImageList.txt` and paste them into `global_template.lua`
	* Overwrite the `imageList` and `imageNames` variables
* (Optional) Fill in the contents of the newly replaced `imageNames` variable
	* These are the strings that will appear in the tooltip when you hover over the generated object in TTS
	* The order of strings matches the order of the file names in `imageList`
* Open TTS and open an existing saved game
	* Alternatively, create a new game and save it.  A save file must exist to use TTS scripting
* Open the Script Editor by clicking Modding -> Scripting
* In the `Global` script, paste the contents of the `global_template.lua` file
	* This assumes there are no global scripts already included.  If there are, you can paste the contents of your `global_template.lua` file after them (as long as there isn't already an `onScriptingButtonUp` function
* Click `Save & Play` in the top left corner of the scripting window
* Now you can spawn your custom objects - press Numpad 4 to create Tokens or Numpad 6 to create Figures
	* If your computer doesn't have a Numpad, you can open Menu -> Configuration -> Controls and rebind `Scripting 4` and `Scripting 6` to different keys
* After spawning the objects, upload them all to your Steam Cloud by clicking Modding -> Cloud Manager -> Upload All Loaded Files 
	* "Upload All Loaded Files" is the arrow pointing upwards to the right of the search box
	* Cloud Manager will prompt you for a folder name to store your files in
* Save the game.  At this point you invite other players or open it later
	* It is important to save the game.  If you don't, the next time you reload it, the custom objects will still point to their location on your hard drive, and online players won't be able to see them.

## Future Improvements
* Have `fileLister.py` generate the entire `global_template.lua` file
* Generate the Lua file in the location so that it's already linked to the desired save in TTS
  * Unlikely.  Seems like a lot of work and probably won't make things any easier for the user
* Combine with TTS_RoomTokenizer in some way
