from models.object_creator import create_object
from project_data.model import Model
from cshape_objects.surfaces.surface import Surface


class ModelSurfacesList(Model):
    def __init__(self):
        super(ModelSurfacesList, self).__init__()
        self.data: list = []
        self.selected_item_index = -1

    def add_item(self, index: int, surface_type):
        item: Surface = create_object(surface_type)
        self.data.insert(index, item)
        item_text = f'{item.get_type()} {item.get_name()}'
        self.view_model.add_item_to_views(index, item_text, item)

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Surface = self.data[self.selected_item_index]
        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views(self.selected_item_index, value,
                                             [self.data[self.selected_item_index].get_type(),
                                              self.data[self.selected_item_index].get_name()])
        # self.notify_view_models(self.selected_item_index, value, 'Change')