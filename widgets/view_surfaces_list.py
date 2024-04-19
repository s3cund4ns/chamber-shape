from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QMenu

from cshape_objects.surfaces.surface import SurfacesTypes
from project_data.view import View


class ViewSurfacesList(View):
    def __init__(self):
        super().__init__()

        self.surfaces_list_widget = QListWidget()
        self.surfaces_list_widget.setDragEnabled(True)
        self.surfaces_list_widget.itemClicked.connect(self.notify_view_models_select)
        self.surfaces_list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.surfaces_list_widget.customContextMenuRequested.connect(self.show_context_menu)

    def add_item(self, *args):
        index, item_text, item = args
        self.surfaces_list_widget.insertItem(index, item_text)

    def notify_view_models_select(self):
        sender = self.surfaces_list_widget.sender().currentRow()
        self.view_model.select_item_in_models(sender)

    def select_item(self, item_index, item):
        self.surfaces_list_widget.setCurrentRow(item_index)

    def change_item(self, item_index, value, item_text):
        self.surfaces_list_widget.currentItem().setText(self.list_to_str(item_text, ' '))

    def notify_view_models_delete(self):
        self.view_model.delete_item_in_models()

    def delete_item(self, index):
        self.surfaces_list_widget.takeItem(index)

    def clear(self):
        self.surfaces_list_widget.clear()

    def show_context_menu(self, pos):
        context_menu = QMenu(self.surfaces_list_widget)
        add = context_menu.addMenu('Add')
        add.setObjectName('Add')
        for surface_type in SurfacesTypes.get(SurfacesTypes):
            add.addAction(surface_type)

        delete = context_menu.addAction("Delete")
        delete.triggered.connect(self.notify_view_models_delete)
        selected_action = context_menu.exec_(self.surfaces_list_widget.mapToGlobal(pos))
        if selected_action and (selected_action.text() != 'Delete'):
            selected_item_name = selected_action.parent().objectName()
            select_action_name = selected_action.text()
            self.view_model.add_item_to_models(self.surfaces_list_widget.count(), select_action_name)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
