from model.view_model import ViewModel, Operations


class ViewModelProperties(ViewModel):
    def __init__(self):
        super().__init__()
        self.current_object = None

    def notify_model(self, operation, parameter):
        self.model.change_data(operation, parameter)

    def notify_views(self, item_index, item, current_object, operation: Operations):
        if operation == 'Select':
            self.current_object = current_object

    def add_item_to_models(self, *args):
        pass

    def add_item_to_views(self, *args):
        pass

    def select_item_in_models(self, *args):
        pass

    def select_item_in_views(self, *args):
        item_index, item = args
        item = item.get_data()
        for view in self.views:
            view.select_item(item_index, item)

    def change_item_in_models(self, *args):
        pass

    def delete_item_in_models(self):
        pass

    def delete_item_in_views(self, index):
        pass

# class ViewModelSurfaceProperties(ViewModelProperties):
#     def __init__(self):
#         super().__init__()
#
#
# class ViewModelMaterialProperties(ViewModelProperties):
#     def __init__(self):
#         super().__init__()
