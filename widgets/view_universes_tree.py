from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidget, QMenu, QTreeWidgetItem

from widgets.view import View


class ViewUniversesTree(View):
    def __init__(self):
        super().__init__()

        self.universes_tree_widget = QTreeWidget()

        self.universes_tree_widget.itemClicked.connect(self.notify_view_models_select)
        self.universes_tree_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.universes_tree_widget.customContextMenuRequested.connect(self.show_context_menu)

        self.universes_tree_widget.clear()
        self.universes_tree_widget.setColumnCount(2)
        self.universes_tree_widget.setHeaderLabels(['Element', 'Name'])

    def notify_view_model_add(self):
        sender = self.universes_tree_widget.sender()
        self.view_model.add_item_to_models(self.universes_tree_widget.topLevelItemCount())

    def notify_view_models_select(self):
        selected_item = self.universes_tree_widget.currentItem()
        self.view_model.select_item_in_models(selected_item)

    def notify_view_model_delete(self):
        self.view_model.delete_item_in_models()

    def add_item(self, *args):
        parent, item_text = args
        parent_item = None
        if parent == 'root':
            parent_item = self.universes_tree_widget
        else:
            parent_item = self.universes_tree_widget.currentItem()
        item = QTreeWidgetItem(parent_item)
        element, name = item_text
        item.setText(0, element)
        item.setText(1, name)
        self.view_model.set_node_value(item)

    def delete_item(self, key):
        index = self.universes_tree_widget.currentIndex().row()
        item = self.universes_tree_widget.takeTopLevelItem(index)
        del item

    def show_context_menu(self, pos):
        context_menu = QMenu(self.universes_tree_widget)
        add = context_menu.addMenu('Add')
        add.setObjectName('Add')
        for universe_element in ['Universe', 'Cell', 'Pin']:
            add.addAction(universe_element)

        add_lattice = add.addMenu('Lattice')
        add_lattice.setObjectName('Lattice')
        for lattice_type in ['Square', 'X Hexagonal', 'Y Hexagonal']:
            add_lattice.addAction(lattice_type)

        delete = context_menu.addAction("Delete")
        delete.triggered.connect(self.notify_view_model_delete)
        selected_action = context_menu.exec_(self.universes_tree_widget.mapToGlobal(pos))
        if selected_action and (selected_action.text() != 'Delete'):
            selected_item_name = selected_action.parent().objectName()
            select_action_name = selected_action.text()
            if selected_item_name == 'Lattice':
                self.view_model.add_item_to_models((selected_item_name, select_action_name))
            else:
                self.view_model.add_item_to_models(select_action_name, '')
