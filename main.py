from pygame import mixer
from pynput.keyboard import Key, Listener, Controller
import threading
from tkinter import *


class Detector:
    def __init__(self):
        mixer.init()
        self.sound_fire = mixer.Sound("sounds/winchester.mp3")
        self.sound_reload_1 = mixer.Sound("sounds/winchester_reload_part1.mp3")
        self.sound_reload_2 = mixer.Sound("sounds/winchester_reload_part2.mp3")
        self.sound_order = 0

    def show(self, key):



        if key == Key.esc:
            # Stop listener
            return False
        elif key == Key.enter or key == Key.tab or key == Key.delete or key == Key.backspace:
            self.sound_fire.play()
        else:
            if self.sound_order == 0:
                self.sound_reload_1.play()
                self.sound_order = 1
            elif self.sound_order == 1:
                self.sound_reload_2.play()
                self.sound_order = 0
            else:
                self.sound_order = 0

    def detect(self):
        with Listener(on_press=self.show) as listener:
            listener.join()


def main():
    screen = Tk()  # initialize
    screen.geometry("500x500")  # pixels
    screen.title("Sound Key")
    screen.configure(bg='white')  # hex colors or normal colors
    running_label = Label(screen, text="Sound Key\n is running !", font=("Courrier", 44))
    running_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    quit_info_label = Label(screen, text="For stop Sound Key, just close this window")
    quit_info_label.pack(side=BOTTOM)
    screen.mainloop()


if __name__ == '__main__':
    exit_flag = False
    detector_thread = threading.Thread(target=Detector().detect)
    detector_thread.start()
    main()
    keyboard = Controller()
    keyboard.press(Key.esc)
