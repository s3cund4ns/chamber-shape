from PySide6.QtWidgets import QSpacerItem

from widgets.property_items.property_item import PropertyItem
from widgets.property_items.property_item_creator import create_property
from widgets.property_items.property_label import PropertyLabel
from widgets.property_items.property_vector3d_float import PropertyVector3DFloat
from widgets.view import View


class ViewProperties(View):
    def __init__(self, properties_layout):
        super().__init__()
        self.properties_layout = properties_layout

    @staticmethod
    def get_property_type(current_property):
        if type(current_property) is list:
            if type(current_property[0]) is list:
                return f'{str(type(current_property))} {str(type(current_property[0]))}'
            return f'{str(type(current_property))} {len(current_property)} {str(type(current_property[0]))}'
        return str(type(current_property))

    def clear_properties(self):
        while self.properties_layout.count() > 0:
            current_property = self.properties_layout.takeAt(0)
            current_property.widget().deleteLater()

    def generate_properties(self, item_index, item):
        self.clear_properties()

        for name, value in item.items():
            data = [name]
            if type(value) is list:
                for element in value:
                    data.append(element)
            else:
                data.append(value)

            property_item: PropertyItem = create_property(self.get_property_type(value))
            property_item.set_properties_view(self)
            property_item.set_data(data)
            self.properties_layout.addWidget(property_item)

    def apply_values_changes(self, sender):
        name, value = sender
        self.view_model.change_item_in_models((name, value))

    def add_item(self, *args):
        pass

    def select_item(self, *args):
        item_index, item = args
        self.clear_properties()
        self.generate_properties(item_index, item.get_data())

    def change_item(self, *args):
        pass

    def delete_item(self, index):
        pass


class ViewSurfaceProperties(ViewProperties):
    def __init__(self, properties_layout):
        super().__init__(properties_layout)


class ViewMaterialProperties(ViewProperties):
    def __init__(self, properties_layout):
        super().__init__(properties_layout)
