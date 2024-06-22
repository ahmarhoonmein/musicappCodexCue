import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
import time

# Function to stop the music
def stopMusic():
    pygame.mixer.music.stop()
    progressbar.set(0)

# Function to set volume
def volume(value):
    pygame.mixer.music.set_volume(float(value))

# Function to go back in the music
def backMusic():
    current_time = pygame.mixer.music.get_pos() / 1000
    pygame.mixer.music.play(start=max(0, current_time - 10))

# Function to forward the music
def forwardMusic():
    current_time = pygame.mixer.music.get_pos() / 1000
    pygame.mixer.music.play(start=current_time + 10)

# Function to pause the music
def pauseMusic():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Function to play the music
def playMusic():
    global current_song_index
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()
    updateCoverImage()
    updateProgressBar()

# Function to play the next song
def playNextSong():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    playMusic()

# Function to update the progress bar
def updateProgressBar():
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000
        progress = current_time / song_length
        progressbar.set(progress)
        root.after(1000, updateProgressBar)
    else:
        playNextSong()

# Function to update the cover image
def updateCoverImage():
    cover_image = Image.open(covers[current_song_index])
    cover_image = cover_image.resize((300, 300), Image.LANCZOS)
    cover_image_tk = ImageTk.PhotoImage(cover_image)
    cover_label.config(image=cover_image_tk)
    cover_label.image = cover_image_tk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Music Player Project (Developed by Ahmar)")
root.geometry("500x500")

# Initialize the pygame mixer to use sounds
pygame.mixer.init()

# Load the song and get its length
songs = ['music/Nahin Milta (Bayaan) - Cover ｜ Ahmar.wav', 'music/guitar.wav']
covers = ['pictures/Cover1.jpg', 'pictures/guitarpic.jpg']
current_song_index = 0
song_length = pygame.mixer.Sound(songs[current_song_index]).get_length()

# Load and display cover image
cover_image = Image.open(covers[current_song_index])
cover_image = cover_image.resize((300, 300), Image.LANCZOS)
cover_image_tk = ImageTk.PhotoImage(cover_image)
cover_label = tkinter.Label(root, image=cover_image_tk)
cover_label.image = cover_image_tk
cover_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

# Create Buttons
playButton = customtkinter.CTkButton(master=root, text="Play", command=playMusic)
playButton.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

pauseButton = customtkinter.CTkButton(master=root, text="  ||  ", command=pauseMusic, width=5)
pauseButton.place(relx=0.7, rely=0.75, anchor=tkinter.CENTER)

skipForwardButton = customtkinter.CTkButton(master=root, text="  >  ", command=forwardMusic, width=5)
skipForwardButton.place(relx=0.8, rely=0.75, anchor=tkinter.CENTER)

skipBackButton = customtkinter.CTkButton(master=root, text="  <  ", command=backMusic, width=5)
skipBackButton.place(relx=0.2, rely=0.75, anchor=tkinter.CENTER)

stopButton = customtkinter.CTkButton(master=root, text="  []  ", command=stopMusic, width=5)
stopButton.place(relx=0.3, rely=0.75, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progressbar.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)

root.mainloop()
