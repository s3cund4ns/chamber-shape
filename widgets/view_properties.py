from cshape_objects.cell import Cell
from cshape_objects.universe import Universe
from widgets.property_items.property_item import PropertyItem
from widgets.property_items.property_item_creator import create_property
from project_data.view import View


class ViewProperties(View):
    def __init__(self, properties_layout):
        super().__init__()
        self.properties_layout = properties_layout

    def clear_properties(self):
        while self.properties_layout.count() > 0:
            current_property = self.properties_layout.takeAt(0)
            current_property.widget().deleteLater()

    def generate_properties(self, default_values, item):
        self.clear_properties()

        for name, value in item.items():
            property_type, values = value
            data = [name]
            if values is None:
                continue
            if type(values) is list:
                for element in values:
                    data.append(element)
            else:
                data.append(values)

            property_item: PropertyItem = create_property(str(property_type))
            property_item.set_properties_view(self)
            property_item.set_default_values(default_values)
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
        self.generate_properties(item_index, item)

    def change_item(self, *args):
        pass

    def delete_item(self, index):
        pass

    def clear(self):
        pass


class ViewSurfaceProperties(ViewProperties):
    def __init__(self, properties_layout):
        super().__init__(properties_layout)


class ViewMaterialProperties(ViewProperties):
    def __init__(self, properties_layout):
        super().__init__(properties_layout)

    def select_item(self, *args):
        item_index, item = args
        self.clear_properties()
        self.generate_properties(['NewNuclide', 0.0], item)


class ViewUniverseProperties(ViewProperties):
    def __init__(self, properties_layout):
        super().__init__(properties_layout)

    def select_item(self, *args):
        item_index, item = args
        item = item[0]
        self.clear_properties()
        if type(item) is Universe:
            self.generate_properties(['Element', 0.0], item.get_data())
        if type(item) is Cell:
            self.generate_properties(['label', 'label', 'combo_box'], item.get_data())

