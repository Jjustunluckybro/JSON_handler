from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from Handlers.JsonHandlers import filler
from utils.DataTypes import Settings
from utils.DataTypes import BoxesResolution

import pyperclip


class JsonFillerLayout:
    start_button = None
    copy_button = None
    clear_json_to_fill_button = None
    help_button = None
    input_json_box_json_to_fill = None
    input_json_box_json_from_fill = None
    output_result_json_box = None
    available_height_position = 550

    def __init__(
            self,
            window: Tk,
            window_resolution: str,
            input_json_boxes_resolution: BoxesResolution,
            height_intend_btw_labels: int = 25
    ):
        # IntVars for checkboxes
        self.is_date_format_checkbox_intvar = IntVar()
        self.is_format_contract_intvar = IntVar()
        self.is_format_primary_account_number_intvar = IntVar()

        self.height_intend_btw_labels = height_intend_btw_labels
        self.window_resolution = window_resolution
        self.window = window
        self.input_json_boxes_resolution = input_json_boxes_resolution

    def start(self):
        """ Create window and widgets. Start mainloop"""

        self.window.geometry(self.window_resolution)
        self.__create_widgets()
        self.__set_all_widgets()
        self.window.mainloop()

    def __create_widgets(self):
        # Create buttons widgets
        self.start_button = Button(
            self.window,
            text='Start',
            command=self.__press_start
        )
        self.copy_button = Button(
            self.window,
            text='Copy result',
            command=self.__press_copy
        )
        self.clear_json_to_fill_button = Button(
            self.window,
            text='Clear JSON to fill field',
            command=self.__pres_clear_json_to_fill_field
        )
        self.clear_json_from_fill_button = Button(
            self.window,
            text='Clear JSON from fill field',
            command=self.__pres_clear_json_from_fill_field
        )
        self.clear_result_json_field_button = Button(
            self.window,
            text='Clear result JSON field',
            command=self.__press_clear_result_json_field
        )
        self.save_account_number_button = Button(
            self.window,
            text='?????????????????? ??????????',
            command=self.__press_save_account_number
        )
        self.clear_account_numbers_button = Button(
            self.window,
            text='?????????????? ????????????',
            command=self.__press_clear_account_numbers
        )
        self.save_contact_id_button = Button(
            self.window,
            text='?????????????????? ID',
            command=self.__press_save_contact_id
        )
        self.clear_contact_id_button = Button(
            self.window,
            text="?????????????? ?????? ID",
            command=self.__press_clear_contact_id
        )

        # Create labels widgets
        self.label_json_from_fill = Label(self.window, text="JSON from fill")
        self.label_json_to_fill = Label(self.window, text="JSON to fill")
        self.label_product_type = Label(self.window, text="PRODUCT_TYPE:")
        self.label_account_number = Label(self.window, text="ACCOUNT_NUMBER:")
        self.label_result_json = Label(self.window, text="Result JSON")
        self.divider_label = Label(
            self.window,
            text="-----------------------------------------------------------"
        )
        self.label_contact_id = Label(self.window, text="CONTACT_ID:")
        self.label_settings = Label(self.window, text='??????????????????:(???????????????? ???????????????? ???????????? ?????? ?????????????????? ??????????????????)*')
        self.label_communication_type = Label(self.window, text="COMMUNICATION_TYPE:")

        # Create combobox widget
        self.product_type_combobox = Combobox(self.window)
        self.product_type_combobox['value'] = (
            "??????????_????_??????????????????_JSON'a",
            "?????????????????? ??????????",
            "??????\\????"
        )
        self.product_type_combobox.current(0)

        self.input_account_number = Combobox(self.window)
        self.input_account_number['value'] = "??????????_????_??????????????????_JSON'a"
        self.input_account_number.current(0)

        self.input_contact_id = Combobox(self.window)
        self.input_contact_id['value'] = "??????????_????_??????????????????_JSON'a"
        self.input_contact_id.current(0)

        self.combobox_communication_type = Combobox(self.window)
        self.combobox_communication_type['value'] = (
            "??????????_????_??????????????????_JSON'a",
            "????????????",
            "??????"
        )
        self.combobox_communication_type.current(0)

        # Create input and output box window widgets
        self.input_json_box_json_to_fill = scrolledtext.ScrolledText(
            self.window,
            width=self.input_json_boxes_resolution.width,
            height=self.input_json_boxes_resolution.height
        )
        self.input_json_box_json_from_fill = scrolledtext.ScrolledText(
            self.window,
            width=self.input_json_boxes_resolution.width,
            height=self.input_json_boxes_resolution.height
        )
        self.output_result_json_box = scrolledtext.ScrolledText(
            self.window,
            width=self.input_json_boxes_resolution.width,
            height=self.input_json_boxes_resolution.height
        )

        # Create checkboxes widgets

        self.is_date_format_checkbox = Checkbutton(
            self.window,
            text="?????????????????????????? ?????? Date&Time ?? Date?",
            variable=self.is_date_format_checkbox_intvar
        )
        self.is_format_contract_checkbox = Checkbutton(
            self.window,
            text='?????????????????? "PRIMARY_CONTRACT_NUMBER" ??????????????????\n ?????????????????? "ACCOUNT_NUMBER"',
            variable=self.is_format_contract_intvar
        )
        self.is_format_primary_account_number = Checkbutton(
            self.window,
            text='?????????????????? "PRIMARY_ACCOUNT_NUMBER" ??????????????????\n ?????????????????? "ACCOUNT_NUMBER"',
            variable=self.is_format_primary_account_number_intvar
        )

    def __set_all_widgets(self):

        self.__set_work_widgets()
        self.__set_settings_widgets()

    def __set_work_widgets(self):

        # Set labels widgets
        self.label_json_to_fill.place(x=180, y=5)
        self.label_json_from_fill.place(x=630, y=5)
        self.label_result_json.place(x=630, y=480)

        # Set all input and output box window widgets
        self.input_json_box_json_to_fill.place(x=10, y=28)
        self.input_json_box_json_from_fill.place(x=450, y=28)
        self.output_result_json_box.place(x=450, y=502)

        # Set all buttons widgets
        self.start_button.place(x=10, y=490)
        self.copy_button.place(
            x=50,
            y=self.start_button.place_info()['y']
        )

        self.clear_json_to_fill_button.place(x=145, y=490)
        self.clear_json_from_fill_button.place(x=275, y=490)
        self.clear_result_json_field_button.place(x=450, y=960)

    def __set_settings_widgets(self):

        # Set label
        self.label_settings.place(x=50, y=self.__calc_height_position())

        self.label_product_type.place(x=50, y=self.__calc_height_position())

        # Set account_number widgets
        self.label_account_number.place(x=50, y=self.__calc_height_position())

        self.save_account_number_button.place(x=135, y=self.__calc_height_position())
        self.clear_account_numbers_button.place(
            x=250,
            y=self.save_account_number_button.place_info()['y']
        )
        self.is_format_contract_checkbox.place(x=50, y=self.__calc_height_position())
        self.is_format_primary_account_number.place(x=50, y=self.__calc_height_position(10))

        # Set Contact id widgets
        self.label_contact_id.place(x=50, y=self.__calc_height_position(15))

        self.save_contact_id_button.place(x=160, y=self.__calc_height_position())
        self.clear_contact_id_button.place(
            x=260,
            y=self.save_contact_id_button.place_info()['y']
        )

        self.label_communication_type.place(x=50, y=self.__calc_height_position(5))

        # Set combobox widget
        self.product_type_combobox.place(
            width=200,
            x=150,
            y=self.label_product_type.place_info()['y']
        )
        self.input_account_number.place(
            width=180,
            x=170,
            y=self.label_account_number.place_info()['y']
        )
        self.input_contact_id.place(
            width=220,
            x=130,
            y=self.label_contact_id.place_info()['y']
        )
        self.combobox_communication_type.place(
            width=170,
            x=195,
            y=self.label_communication_type.place_info()['y']
        )

        self.divider_label.place(x=50, y=self.__calc_height_position())

        # Set checkboxes widgets
        self.is_date_format_checkbox.place(x=50, y=self.__calc_height_position())

    def __press_start(self):

        settings = self.read_settings()
        result: str = filler(
            to_fill_str=self.input_json_box_json_to_fill.get('1.0', END),
            from_fill_str=self.input_json_box_json_from_fill.get('1.0', END),
            settings=settings
        )
        self.__set_new_output_message(result)

    # Button Press
    def __press_copy(self):
        text = self.output_result_json_box.get('1.0', END)
        pyperclip.copy(text)

    def __pres_clear_json_to_fill_field(self):
        self.input_json_box_json_to_fill.delete('1.0', END)

    def __pres_clear_json_from_fill_field(self):
        self.input_json_box_json_from_fill.delete('1.0', END)

    def __press_clear_result_json_field(self):
        self.output_result_json_box.delete('1.0', END)

    def __press_help_button(self):
        pass

    def __press_save_account_number(self):
        account_number = self.input_account_number.get()
        current_values: tuple = self.input_account_number['values']
        if account_number in current_values:
            pass
        else:
            current_value_list: list = list(current_values)
            current_value_list.append(account_number)
            current_values = tuple(current_value_list)
            self.input_account_number['values'] = current_values

    def __press_clear_account_numbers(self):
        self.input_account_number['value'] = (
            "??????????_????_??????????????????_JSON'a"
        )

    def __press_save_contact_id(self):
        contact_id: str = self.input_contact_id.get()
        current_values: tuple = self.input_contact_id['values']
        if contact_id in current_values:
            pass
        else:
            current_values_list: list = list(current_values)
            current_values_list.append(contact_id)
            current_values = tuple(current_values_list)
            self.input_contact_id['values'] = current_values

    def __press_clear_contact_id(self):
        self.input_contact_id['values'] = "??????????_????_??????????????????_JSON'a"

    # Utils
    def __calc_height_position(self, custom_intend: int | None = None) -> int:
        """
        Return current available position to label
        Then increment it and save
        """
        height_position = self.available_height_position

        if custom_intend is None:
            self.available_height_position += self.height_intend_btw_labels
        else:
            height_position += custom_intend
            self.available_height_position = height_position + self.height_intend_btw_labels
        return height_position

    def __set_new_output_message(self, message: str, is_delete_previous_msg: bool = True):
        if is_delete_previous_msg:
            self.__press_clear_result_json_field()
        self.output_result_json_box.insert(INSERT, message)

    # def __inputs_strings_to_dicts_data(self) -> Type[DictsData]:
    #
    #     to_fill: str = self.input_json_box_json_to_fill.get('1.0', END)
    #     from_fill: str = self.input_json_box_json_from_fill.get('1.0', END)
    #     try:
    #         dicts = convert_string_to_dict(to_fill, from_fill)
    #         print(dicts.dict1, dicts.dict2)  # TODO: Delete debug print
    #         return dicts
    #     except CanNotReedJsons:
    #         error_msg = "???????????????????????? JSON'??"
    #         self.__set_new_output_message(error_msg)

    def read_settings(self) -> Settings:

        settings = Settings(
            product_type=self.product_type_combobox.get(),
            account_number=self.input_account_number.get(),
            contact_id=self.input_contact_id.get(),
            communication_type=self.combobox_communication_type.get(),
            is_date_format=bool(self.is_date_format_checkbox_intvar.get()),
            is_format_contract=bool(self.is_format_contract_intvar.get()),
            is_format_primary_account_number=bool(
                self.is_format_primary_account_number_intvar.get()
            )
        )

        return settings
