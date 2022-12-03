from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from enum import Enum
from typing import NamedTuple

from JsonFillerLayout import JsonFillerLayout


class States(Enum):
    MAIN_MENU = 'Mian'
    JSON_FILLER = 'Filler'


class RootWindow:
    window: Tk
    resolution: str
    current_state: States

    def __init__(self, resolution: str):
        self.current_state = States.MAIN_MENU
        self.resolution = resolution
        self.window = Tk()

    def start(self):
        self.window.geometry(self.resolution)

    def new_layout(self):
        pass
