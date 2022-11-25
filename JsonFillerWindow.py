import tkinter
import json

from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox


class JsonFillerWindow:
    start_button = None
    copy_button = None
    clear_button = None
    help_button = None
    input_json_box_1 = None
    input_json_box_2 = None
    output_json_box = None

    def __init__(
            self,
            window: Tk,
            window_resolution: str,
            input_json_boxes_resolution: tuple
    ):
        self.window_resolution = window_resolution
        self.window = window
        self.input_json_boxes_resolution = input_json_boxes_resolution

    def start(self):
        self.window.geometry(self.window_resolution)
        self.__create_widgets()
        self.__set_all_widgets()
        self.window.mainloop()

    def __create_widgets(self):
        # Create buttons widgets
        self.start_button = Button(
            self.window,
            text='Start',
            command=self.press_start
        )
        self.copy_button = Button(
            self.window,
            text='Copy',
            command=self.press_copy
        )
        self.clear_button = Button(
            self.window,
            text='Clear',
            command=self.pres_clear
        )

        # Create input and output box window widgets
        self.input_json_box_1 = scrolledtext.ScrolledText(
            self.window,
            width=self.input_json_boxes_resolution[0],
            height=self.input_json_boxes_resolution[1]
        )
        self.input_json_box_2 = scrolledtext.ScrolledText(
            self.window,
            width=self.input_json_boxes_resolution[0],
            height=self.input_json_boxes_resolution[1]
        )
        self.output_json_box = scrolledtext.ScrolledText(
            self.window,
            width=self.input_json_boxes_resolution[0],
            height=self.input_json_boxes_resolution[1]
        )

        # Create labels widgets
        self.label_Json_from_fill = Label(self.window, text="json from fill")
        self.label_Json_to_fill = Label(self.window, text="json to fill")
        self.label_product_type = Label(self.window, text="PRODUCT_TYPE")
        self.label_account_number = Label(self.window, text="ACCOUNT_NUMBER")
        self.label_result_json = Label(self.window, text="Result JSON")

        # Create combobox widget
        self.product_type_combobox = Combobox(self.window)

        # Create checkboxes widgets
        self.is_date_format_checkbox = Checkbutton(
            self.window,
            text="Форматировать все Date&Time в Date?"
        )

    def __set_all_widgets(self):

        # Set all buttons widgets
        # self.start_button.grid()
        # self.copy_button.grid()
        # self.clear_button.grid()

        # Set all input and output box window widgets
        self.input_json_box_1.grid(column=0, row=1)
        self.input_json_box_2.grid(column=1, row=1)
        self.output_json_box.grid(column=1, row=3)

        # Set labels widgets
        self.label_Json_from_fill.grid(column=0 , row=0)
        self.label_Json_to_fill.grid(column=1 , row=0)
        self.label_result_json.grid(column=2, row=2)
        self.label_product_type.grid(column=0 , row=4)
        self.label_account_number.grid(column=0 , row=5)


        # Set combobox widget
        self.product_type_combobox.grid()

        # Set checkboxes widgets
        self.is_date_format_checkbox.grid()

    def press_start(self):
        pass

    def press_copy(self):
        pass

    def pres_clear(self):
        pass

    def press_help_button(self):
        pass

"""
    TODO UI:
    1. Заполнение одного json'а другим
        1.1. Форматирование д&т в дату - чекбокс
        1.2. IsTraining - чекбокс
        1.3. поля для предзаполнения переменных
            a. PRODUCT_TYPE - выпадающий список
            b. ACCOUNT_NUMBER - чекбоксы для совместимости с primary, contract
            


"""
