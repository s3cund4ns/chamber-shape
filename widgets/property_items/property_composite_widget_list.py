from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QComboBox, QMenu, QWidget, QHBoxLayout

from widgets.property_items.property_item import PropertyItem


class PropertyCompositeWidgetList(PropertyItem):
    def __init__(self):
        super().__init__()
        self.widget_component_types: dict = {
            'label': QLabel,
            'combo_box': QComboBox
        }
        self.widget_components: list = []
        self.all_items_in_menu: list = []
        self.editable_items: list = []
        self.composite_widgets: list = []
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel()
        self.composite_widget_list = QWidget()
        self.composite_widget_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.vertical_layout.addWidget(self.label_name)
        self.vertical_layout.addWidget(self.composite_widget_list)
        self.context_menu = QMenu(self.composite_widget_list)

    def set_default_values(self, *args):
        widget_component_keys = args[0]
        print(widget_component_keys)
        for widget_component_key in widget_component_keys:
            self.widget_components.append(self.widget_component_types[widget_component_key])

    def set_data(self, data: list):
        name, *values = data
        self.label_name.setText(name)
        self.all_items_in_menu = values[1]
        print(values[0])
        composite_widgets = values[0]
        self.button_add_composite_widget = QPushButton(self)
        self.button_add_composite_widget.setText('Add')
        self.button_add_composite_widget.setMenu(self.context_menu)
        self.add_items_to_menu()
        self.vertical_layout.addWidget(self.button_add_composite_widget)
        for composite_widget_info in composite_widgets:
            composite_widget = QWidget(self.composite_widget_list)
            composite_widget_layout = QHBoxLayout(composite_widget)
            for info_element in composite_widget_info:
                widget_component_index = composite_widget_info.index(info_element)
                print(self.widget_components)
                print(widget_component_index)
                widget_component = self.create_widget_component(widget_component_index)
                if type(widget_component) is QLabel:
                    widget_component.setText(info_element)
                    composite_widget_layout.addWidget(widget_component)
                elif type(widget_component) is QComboBox:
                    widget_component.addItem('In')
                    widget_component.addItem('Out')
                    widget_component.setCurrentText(info_element)
                    widget_component.currentTextChanged.connect(self.change_item)
                    composite_widget_layout.addWidget(widget_component)
                    self.editable_items.append(widget_component)

            button_delete_composite_widget = QPushButton(self)
            button_delete_composite_widget.setText('-')
            button_delete_composite_widget.clicked.connect(self.delete_item)
            composite_widget_layout.addWidget(button_delete_composite_widget)
            self.vertical_layout.addWidget(composite_widget)
            self.composite_widgets.append(composite_widget)

    def add_item(self):
        composite_widget = QWidget(self.composite_widget_list)
        composite_widget_layout = QHBoxLayout(composite_widget)
        composite_widget_info: list = self.str_to_list(self.sender().text(), ' ')
        for info_element in composite_widget_info[1:]:
            widget_component_index = composite_widget_info[1:].index(info_element)
            widget_component = self.create_widget_component(widget_component_index)
            widget_component.setText(info_element)
            composite_widget_layout.addWidget(widget_component)

        widget_component = self.create_widget_component(len(self.widget_components) - 1)
        widget_component.addItem('In')
        widget_component.addItem('Out')
        widget_component.currentTextChanged.connect(self.change_item)
        composite_widget_layout.addWidget(widget_component)
        self.editable_items.append(widget_component)

        button_delete_composite_widget = QPushButton(self)
        button_delete_composite_widget.setText('-')
        button_delete_composite_widget.clicked.connect(self.delete_item)
        composite_widget_layout.addWidget(button_delete_composite_widget)

        self.vertical_layout.addWidget(composite_widget)

        self.composite_widgets.append(composite_widget)

        self.properties_view.apply_values_changes(('Add', [int(composite_widget_info[0]),
                                                           widget_component.currentText()]))

        self.delete_item_from_menu(self.sender().text())

    def create_widget_component(self, widget_component_index):
        return self.widget_components[widget_component_index](self)

    def add_items_to_menu(self):
        for item_in_menu in self.all_items_in_menu:
            action = self.context_menu.addAction(item_in_menu)
            action.triggered.connect(self.add_item)

    def delete_item_from_menu(self, text):
        for action in self.context_menu.actions():
            if action.text() == text:
                self.context_menu.removeAction(action)

    def change_item(self):
        sender_parent = self.sender().parent()
        index = self.composite_widgets.index(sender_parent)
        value = self.sender().currentText()
        self.properties_view.apply_values_changes(('SurfaceSide', [index, value]))

    def delete_item(self):
        sender = self.sender().parent()
        index = self.composite_widgets.index(sender)
        self.properties_view.apply_values_changes(('Delete', index))
        layout = sender.layout()
        while layout.count() > 0:
            element = layout.takeAt(0)
            element.widget().deleteLater()
        self.widget_components.remove(sender)

    @staticmethod
    def str_to_list(str_item: str, delimiter: str) -> list:
        list_item = str_item.split(delimiter)
        return list_item