import tkinter
import json

from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox

from JsonFillerWindow import *

def main():
    window = Tk()
    json_filler_window = JsonFillerWindow(
        window=window,
        window_resolution="1000x1000",
        input_json_boxes_resolution=(40, 20)
    )
    json_filler_window.start()


if __name__ == '__main__':
    main()
