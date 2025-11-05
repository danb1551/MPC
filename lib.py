import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0
        self.paused = False

    def add_folder_to_playlist(self, dir: str = "test"):
        for items in os.listdir(dir):
            if items.endswith(".mp3") or items.endswith(".wav"):
                self.add_to_playlist(os.path.join(dir, items))

    def get_playlist(self, start: int = 0, end: int = None):
        if end is None:
            end = len(self.playlist)
        return self.playlist[start:end]
    
    def add_to_playlist(self, file):
        self.playlist.append(file)

    def load_current(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])

    def play(self):
        if not self.playlist:
            return
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.load_current()
            pygame.mixer.music.play()

    def pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False

    def next(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def set_actual_time(self, seconds):
        if self.playlist:
            pygame.mixer.music.play(start=seconds)
            self.paused = False

    def current_song(self):
        if self.playlist:
            return self.playlist[self.current_index]
        return None

def _test():
    player = MusicPlayer()
    player.add_folder_to_playlist("test")
    player.play()
    input("Enter for next...")
    player.next()
    input("Enter for next...")
    player.next()
    input("Enter for next...")
    player.next()
    input("Enter for next...")
    player.next()
    input("Enter for next...")
    player.next()
    input("Enter for next...")
    player.next()

if __name__ == "__main__":
    _test()