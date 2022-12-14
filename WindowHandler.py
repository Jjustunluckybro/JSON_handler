import tkinter
import json

from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox


def compare_jsons(json1: dict, json2: dict) -> dict:
    """"""
    counter = 0
    answer = {}
    keys_not_compare = []

    for k, v in json1.items():
        if k in json2:
            pass
        else:
            counter += 1
            keys_not_compare.append(k)

    if counter == 0:
        answer['is_equal'] = True
    else:
        answer['is_equal'] = False
        answer['keys_not_equal'] = keys_not_compare
    return answer


def fill_json(json_to_fill: dict, json_from_fill=None) -> dict:
    """"""

    if json_from_fill is None:
        with open("data/root_json_to_fill.json", "r") as file:
            json_from_fill = json.load(file)

    answer = {}
    for k in json_to_fill.keys():
        if k in json_from_fill:
            answer[k] = json_from_fill[k]
        else:
            pass

    return answer


class WindowHandler:
    window = Tk()

    label_1: Label
    label_2: Label

    back_to_main_btn: Button
    choose_mode_btn: Button
    start_fill_json_btn: Button
    compare_btn: Button

    input_box: scrolledtext.ScrolledText
    input_box_2: scrolledtext.ScrolledText
    compare_input_1: scrolledtext.ScrolledText
    compare_input_2: scrolledtext.ScrolledText
    answer_scr: scrolledtext.ScrolledText = None

    mods_selector: Combobox

    def __init__(self):

        self.last_row = 0
        self.all_start_widgets = []
        self.all_active_non_start_widgets = []

    def start(self):
        self.window.geometry('700x400')
        self.create_start_widgets()
        self.set_start_widgets()
        self.window.mainloop()

    def create_start_widgets(self):
        self.choose_mode_btn = Button(
            self.window,
            text='Choose mode',
            command=self.click_choose_mode_btn
        )

        self.mods_selector = Combobox(self.window)
        self.mods_selector['value'] = ("Fill JSON", "Compare JSON's keys")
        self.mods_selector.current(0)

        self.all_start_widgets.append(self.choose_mode_btn)
        self.all_start_widgets.append(self.mods_selector)

    def set_start_widgets(self):
        self.mods_selector.grid(column=0, row=self.last_row)
        self.last_row += 1

        self.choose_mode_btn.grid(column=0, row=self.last_row)
        self.last_row += 1

    def remove_start_widgets(self):
        for widget in self.all_start_widgets:
            widget.grid_remove()

    def create_fill_json_widgets(self):

        # Create answer box
        self.answer_scr = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )

        # Create two labels
        self.label_1 = Label(
            self.window,
            text='JSON FROM FILL'
        )

        self.label_2 = Label(
            self.window,
            text='JSON TO FILL'
        )

        # Create two input boxes
        self.input_box = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )

        self.input_box_2 = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )

        # Create two buttons
        self.start_fill_json_btn = Button(
            self.window,
            text='Fill JSON',
            command=self.click_fill_json_btn
        )

        self.back_to_main_btn = Button(
            self.window,
            text='back to choose',
            command=self.click_back_to_main
        )

    def set_fill_json_widgets(self):

        # Set two labels
        self.label_1.grid(column=1, row=self.last_row)
        self.label_2.grid(column=0, row=self.last_row)
        self.last_row += 1
        self.all_active_non_start_widgets.append(self.label_1)
        self.all_active_non_start_widgets.append(self.label_2)

        # Set two input boxes
        self.input_box.grid(column=0, row=self.last_row)
        self.all_active_non_start_widgets.append(self.input_box)

        self.input_box_2.grid(column=1, row=self.last_row)
        self.all_active_non_start_widgets.append(self.input_box_2)
        self.last_row += 1

        # Set two buttons
        self.start_fill_json_btn.grid(column=0, row=self.last_row)
        self.all_active_non_start_widgets.append(self.start_fill_json_btn)

        self.back_to_main_btn.grid(column=1, row=self.last_row)
        self.all_active_non_start_widgets.append(self.back_to_main_btn)
        self.last_row += 1

    def fill_json(self):
        self.create_fill_json_widgets()
        self.set_fill_json_widgets()
        self.remove_start_widgets()

    def create_compare_widgets(self):
        self.compare_input_1 = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )

        self.compare_input_2 = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )

        self.back_to_main_btn = Button(
            self.window,
            text='back to choose',
            command=self.click_back_to_main
        )

        self.compare_btn = Button(
            self.window,
            text='Compare',
            command=self.click_compare_btn
        )

    def set_compare_widgets(self):
        self.compare_input_1.grid(column=0, row=self.last_row)
        self.all_active_non_start_widgets.append(self.compare_input_1)
        self.compare_input_2.grid(column=1, row=self.last_row)
        self.all_active_non_start_widgets.append(self.compare_input_2)

        self.last_row += 1

        self.compare_btn.grid(column=0, row=self.last_row)
        self.all_active_non_start_widgets.append(self.compare_btn)
        self.back_to_main_btn.grid(column=1, row=self.last_row)
        self.all_active_non_start_widgets.append(self.back_to_main_btn)
        self.last_row += 1

    def compare_widgets(self):
        self.create_compare_widgets()
        self.set_compare_widgets()
        self.remove_start_widgets()

    def click_back_to_main(self):
        self.set_start_widgets()
        self.remove_all_active_non_start_widgets()

    def click_choose_mode_btn(self):
        mods = {
            "Fill JSON": self.fill_json,
            "Compare JSON's keys": self.compare_widgets
        }

        choose = self.mods_selector.get()
        mods[choose]()

    def click_fill_json_btn(self):

        json1_txt = self.input_box.get('1.0', END)
        json2_txt = self.input_box_2.get('1.0', END)

        if self.answer_scr is not None:
            self.answer_scr.grid_remove()
        self.answer_scr = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )
        self.answer_scr.grid(column=0, row=self.last_row)
        self.last_row += 1
        self.all_active_non_start_widgets.append(self.answer_scr)

        try:
            json1: dict = json.loads(json1_txt)
            if json2_txt == '\n':
                answer = fill_json(json1)
            else:
                json2: dict = json.loads(json2_txt)
                answer = fill_json(json1, json2)

            self.answer_scr.insert(INSERT, str(answer).replace("'", '"'))
        except json.decoder.JSONDecodeError as error:
            self.answer_scr.insert(INSERT, f"{error}\nCheck JSON!")


    def click_compare_btn(self):
        json1_txt = self.compare_input_1.get('1.0', tkinter.END)
        json2_txt = self.compare_input_2.get('1.0', tkinter.END)

        if self.answer_scr is not None:
            self.answer_scr.grid_remove()

        self.answer_scr = scrolledtext.ScrolledText(
            self.window,
            width=40,
            height=10
        )
        self.answer_scr.grid(column=0, row=self.last_row)
        self.last_row += 1
        self.all_active_non_start_widgets.append(self.answer_scr)

        try:
            json1: dict = json.loads(json1_txt)
            json2: dict = json.loads(json2_txt)

            answer = compare_jsons(json1, json2)
            if 'keys_not_equal' in answer:
                self.answer_scr.insert(
                    INSERT,
                    f"JSON's is equal - {answer['is_equal']}\nkeys not equal - {answer['keys_not_equal']}"
                )
            else:
                self.answer_scr.insert(INSERT, f"JSON's is equal - {answer['is_equal']}")

        except json.decoder.JSONDecodeError as error:
            self.answer_scr.insert(INSERT, f"{error}\nCheck JSON!")

    def remove_all_active_non_start_widgets(self):
        for widget in self.all_active_non_start_widgets:
            widget.grid_remove()

        self.all_active_non_start_widgets = []
