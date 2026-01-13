import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar, simpledialog, ttk

# Audio Storage Folder
sounds_folder = "sounds"

# Creating the main window
root = tk.Tk()
root.title("SongScape")
root.geometry("700x500")
root.iconbitmap("logo.ico")

root.tk.call("source", "Forest-ttk-theme-master/forest-dark.tcl")

style = ttk.Style(root)
style.theme_use("forest-dark")

# Track Listing & Sticky Tracks
tracks = []
pinned_tracks = []

# File list update function
def update_file_list():
    file_list.delete(0, tk.END)
    # Add pinned tracks first
    for track in pinned_tracks:
        if track in tracks:  # Make sure that the track is in the general list
            file_list.insert(tk.END, f"[FIXED] {track}")
    # Then add the remaining tracks that are not pinned
    for track in tracks:
        if track not in pinned_tracks:
            file_list.insert(tk.END, track)

# File Upload
def upload_file():
    filepath = filedialog.askopenfilename(
        title="Select Music File",
        filetypes=[("MP3 файлы", "*.mp3")]
    )
    if filepath:
        try:
            filename = os.path.basename(filepath)  # Getting the file name
            shutil.copy(filepath, sounds_folder)
            tracks.append(filename)  # Adding to the general list
            messagebox.showinfo("Success", "File uploaded successfully!")
            update_file_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload file: {e}")

# Playing the selected file
def play_selected():
    selected = file_list.curselection()
    if selected:
        filename = file_list.get(selected[0]).replace("[FIXED] ", "")  # Removing the label
        full_path = os.path.join(sounds_folder, filename)
        os.startfile(full_path)

# Deleting the selected music
def delete_selected():
    selected = file_list.curselection()
    if selected:
        filename = file_list.get(selected[0]).replace("[FIXED] ", "")
        full_path = os.path.join(sounds_folder, filename)
        try:
            os.remove(full_path)
            tracks.remove(filename)  # Removing from the general list
            if filename in pinned_tracks:  # If it was fixed, remove from the fixed
                pinned_tracks.remove(filename)
            messagebox.showinfo("Удалено", f"Удален: {filename}")
            update_file_list()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить файл: {e}")

# Rename the selected track
def rename_track():
    selected = file_list.curselection()
    if selected:
        filename = file_list.get(selected[0]).replace("[FIXED] ", "")
        new_name = simpledialog.askstring("Renaming", f"New name for {filename} (no extension):")
        if new_name:
            old_path = os.path.join(sounds_folder, filename)
            new_filename = new_name + ".mp3"
            new_path = os.path.join(sounds_folder, new_filename)
            try:
                os.rename(old_path, new_path)
                if filename in tracks:
                    tracks.remove(filename)
                    tracks.append(new_filename)  # Adding a new name to the shared list
                if filename in pinned_tracks:
                    pinned_tracks.remove(filename)
                    pinned_tracks.append(new_filename)  # We change the name in the fixed
                messagebox.showinfo("Renamed", f"{filename} renamed to {new_filename}")
                update_file_list()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename: {e}")
    else:
        messagebox.showwarning("Select file", "Please select a file to rename.")

# Docking or undocking the selected track
def toggle_pin():
    selected = file_list.curselection()
    if selected:
        filename = file_list.get(selected[0]).replace("[ЗАКРЕПЛЁН] ", "")
        if filename in pinned_tracks:
            pinned_tracks.remove(filename)
            messagebox.showinfo("Unpinned", f"{filename} no longer pinned.")
        else:
            pinned_tracks.append(filename)
            messagebox.showinfo("Pinned", f"{filename} pinned.")
        update_file_list()
    else:
        messagebox.showwarning("select file", "Please select a file to pin.")

# creating buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

upload_button = ttk.Button(button_frame, text="Load music", command=upload_file)
upload_button.pack(side=tk.LEFT, padx=5)

play_button = ttk.Button(button_frame, text="Play", command=play_selected)
play_button.pack(side=tk.LEFT, padx=5)

delete_button = ttk.Button(button_frame, text="Delete", command=delete_selected)
delete_button.pack(side=tk.LEFT, padx=5)

rename_button = ttk.Button(button_frame, text="Rename", command=rename_track)
rename_button.pack(side=tk.LEFT, padx=5)

pin_button = ttk.Button(button_frame, text="Pin/Unpin", command=toggle_pin)
pin_button.pack(side=tk.LEFT, padx=5)

# Creating a scrollable list
list_frame = ttk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

file_list = Listbox(list_frame,
                    yscrollcommand=scrollbar.set, height=15)
file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=file_list.yview)

# Refresh the list on startup
# Loading existing tracks from the folder
for filename in os.listdir(sounds_folder):
    if filename.endswith(".mp3"):
        tracks.append(filename)

update_file_list()

# Start Interface
root.mainloop()
