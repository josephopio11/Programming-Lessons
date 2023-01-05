# Import the necessary modules
from guizero import App, Text, PushButton
from pygame import mixer

# Create the main application window
app = App()

# Create the widgets

# Create the label for the currently playing song
song_label = Text(app, text="No song currently playing")

# Create the buttons for controlling the music player
play_button = PushButton(app, text="Play", command=play_song)
stop_button = PushButton(app, text="Stop", command=stop_song)
choose_button = PushButton(app, text="Choose Song", command=choose_song)

# Set the layout

# Add the song label and buttons to the window
song_label.grid(row=0, column=0, columnspan=3)
play_button.grid(row=1, column=0)
stop_button.grid(row=1, column=1)
choose_button.grid(row=1, column=2)

# Start the event loop
app.display()


# Helper functions

# Helper function to play a song
def play_song():
    # Check if there is a song currently loaded
    if not mixer.music.get_busy():
        # If not, show an error message
        song_label.value = "No song currently loaded"
        return

    # Play the song
    mixer.music.play()


# Helper function to stop the song
def stop_song():
    # Stop the song
    mixer.music.stop()


# Helper function to choose a song
def choose_song():
    # Use the filedialog module to open a file chooser
    # and allow the user to select a song
    song_file = filedialog.askopenfilename(initialdir=".",
                                           title="Choose a song",
                                           filetypes=(("mp3 files", "*.mp3"),))

    # Check if a song was selected
    if not song_file:
        # If not, return without doing anything
        return

    # Stop the currently playing song (if any)
    stop_song()

    # Load the selected song
    mixer.music.load(song_file)

    # Update the song label with the song file name
    song_label.value = song_file
