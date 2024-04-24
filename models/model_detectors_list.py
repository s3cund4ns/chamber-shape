from cshape_objects.detectors.detector_creator import create_detector
from project_data.model import Model
from cshape_objects.detectors.detector import Detector


class ModelDetectorsList(Model):
    def __init__(self):
        super(ModelDetectorsList, self).__init__()
        self.data: list = []
        self.selected_item_index = -1
        self.materials_model = None

    def add_item(self, index: int, detector_type):
        item: Detector = create_detector(detector_type)
        self.data.insert(index, item)
        item_text = f'{item.get_type()} {item.get_name()}'
        self.view_model.add_item_to_views(index, item_text, item)

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Detector = self.data[self.selected_item_index]
        selected_item.materials = self.materials_model.data
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
