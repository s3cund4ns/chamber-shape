from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QMenu

from project_data.view import View


class ViewMaterialsList(View):
    def __init__(self):
        super().__init__()

        self.materials_list_widget = QListWidget()

        self.materials_list_widget.itemClicked.connect(self.notify_view_models_select)
        self.materials_list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.materials_list_widget.customContextMenuRequested.connect(self.show_context_menu)

    def notify_view_model_add(self):
        self.view_model.add_item_to_models(self.materials_list_widget.count())

    def notify_view_models_select(self):
        sender = self.materials_list_widget.sender().currentRow()
        self.view_model.select_item_in_models(sender)

    def notify_view_model_delete(self):
        self.view_model.delete_item_in_models()

    def add_item(self, *args):
        index, item_text, item = args
        self.materials_list_widget.insertItem(index, item_text)

    def select_item(self, item_index, item):
        self.materials_list_widget.setCurrentRow(item_index)

    def change_item(self, item):
        self.materials_list_widget.currentItem().setText(self.list_to_str(item, ' '))

    def delete_item(self, item):
        self.materials_list_widget.takeItem(item)

    def clear(self):
        self.materials_list_widget.clear()

    def show_context_menu(self, pos):
        context_menu = QMenu(self.materials_list_widget)
        add = context_menu.addAction('Add')
        delete = context_menu.addAction("Delete")
        add.triggered.connect(self.notify_view_model_add)
        delete.triggered.connect(self.notify_view_model_delete)
        selected_action = context_menu.exec_(self.materials_list_widget.mapToGlobal(pos))

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
