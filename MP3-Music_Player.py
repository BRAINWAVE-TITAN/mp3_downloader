from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class mp:
    def __init__(self,unicompiler):
        unicompiler.geometry("500x300")
        unicompiler.title("MP3 Music Player")
        unicompiler.resizable(0,0)
        
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        
        load_btn = Button(unicompiler, text='Load',width=10,command=self.load)
        load_btn.place(x=180,y=160)
        
        play_btn = Button(unicompiler, textvariable=self.play_restart,width=10,command=self.play)
        play_btn.place(x=180,y=190)
        
        pause_btn = Button(unicompiler, textvariable=self.pause_resume,width=10,command=self.pause)
        pause_btn.place(x=180,y=220)
        
        stop_btn = Button(unicompiler, text='Stop',width=10,command=self.stop)
        stop_btn.place(x=180,y=250)
        
        self.music_file = False
        self.playing_state = False
        
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print('Loaded Successfully',self.music_file)
        self.play_restart.set('Play')
    
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')
    
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause') 
    
    def stop(self):
        mixer.music.stop()
        

        
root = Tk()
photo = PhotoImage(file='image.png')
mp_label = Label(image=photo)
mp_label.pack()
mp(root)
root.mainloop()
