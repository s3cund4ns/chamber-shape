from project_data.view import View
from widgets.input_data_editor import InputDataEditor


class ViewInputData(View):
    def __init__(self, input_data_editor: InputDataEditor):
        super().__init__()
        self.input_data_editor = input_data_editor
        self.input_data_text: str = ''

    def add_item(self, input_data: list):
        text = ''
        for cshape_object_data in input_data:
            text += self.list_to_str(cshape_object_data, '')

        self.input_data_text = text
        self.input_data_editor.set_text(text)

    def get_input_data(self):
        return self.input_data_text

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item