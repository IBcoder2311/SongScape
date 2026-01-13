# SongScape — Music Manager and Player (Tkinter)

A lightweight graphical app written in Python for uploading, viewing, renaming, deleting, and playing MP3 files stored locally in a dedicated folder.

## What’s inside

- Tkinter-based UI with a dark Forest theme

- Capabilities:
  - Upload MP3 files into the sounds/ folder
  - View a list of tracks with pinned (fixed) items shown first
  - Play the selected track
  - Rename a track (changes the filename locally)
  - Delete a track from the local folder
  - Pin/Unpin tracks to keep them at the top of the list
  - Main script: main.py (or the name you use for your file)
 
  ## Requirements
- Python 3.x
- Tkinter (usually included with Python’s standard library)
- Operating system: Windows, macOS, or Linux

## Installation
1. Clone or extract the project.
2. Ensure there is a folder named sounds in the project root (or create it):
   - sounds/ will store the MP3 files
3. Install any needed dependencies (usually not required beyond a standard Python install).
   - On some systems you may need to install Tkinter separately.

## How to run
1. pen a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script, for example:
   - `python main.py` or `python3 main.py` depending on your setup
4. The SongScape window will appear.

## How to use
- Click “Load music” to upload a selected MP3 file into the sounds folder and add it to the list.
- In the list:
   - Select a track and click “Play” to play the file (uses the system’s default player via os.startfile on Windows; behavior may vary by OS).
   - “Delete” removes the file from the sounds folder and the list.
   - “Rename” renames the track (you provide a new name without extension; .mp3 is added automatically).
   - “Pin/Unpin” pins or unpins a track. Pinned tracks are shown at the top with a [FIXED] label.
- The list persists for the current session. On the next launch, files already in sounds will appear again in the list.

## Notes and recommendations
- The sounds/ folder must exist in your project directory. Create it manually if needed.
- Only MP3 files are considered (files with .mp3 extension).
- Deleting a file is permanent via the UI; confirm your choice before deleting.
- Consider extending the app with:
  - Saving pinned tracks between sessions (e.g., in a config.json)
  - Cross-platform playback support (e.g., using playsound, pyglet, or a dedicated audio library)
  - Robust error handling for inaccessible folders or missing files

## Project structure example
- main.py (your main application script)
- Forest-ttk-theme-master/forest-dark.tcl (UI theme)
- sounds/ (directory for MP3 files)
- logo.ico (window icon)
