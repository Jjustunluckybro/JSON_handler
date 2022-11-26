from tkinter import *

from JsonFillerLayout import *


def main():
    window = Tk()

    json_filler_window = JsonFillerLayout(
        window=window,
        window_resolution="900x1000",
        input_json_boxes_resolution=BoxesResolution(height=28, width=50)
    )
    json_filler_window.start()


if __name__ == '__main__':
    main()
