from project_data.view import View
from widgets.input_data_editor import InputDataEditor


class ViewInputData(View):
    def __init__(self, input_data_editor: InputDataEditor):
        super().__init__()
        self.input_data_editor = input_data_editor

    def add_item(self, input_data: list):
        text = ''
        for cshape_object_data in input_data:
            text += self.list_to_str(cshape_object_data, '')

        self.input_data_editor.set_text(text)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item