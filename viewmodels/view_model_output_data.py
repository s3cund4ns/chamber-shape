from project_data.view_model import ViewModel


class ViewModelOutputData(ViewModel):
    def __init__(self):
        super().__init__()

    def select_calculation_output_in_model(self):
        for model in self.models:
            model.get_calculation_output()

    def get_plot_info_from_model(self):
        for model in self.models:
            model.get_plot_info()

    def select_item_in_views(self, output_data):
        for view in self.views:
            view.select_item(0, output_data)

    def change_item_in_models(self, *args):
        value, = args
        for model in self.models:
            model.change_data(value)

    def change_item_in_views(self, *item_data):
        name, energy_mid_grid, sp_flux, sp_errors = item_data
        for view in self.views:
            view.change_item(name, energy_mid_grid, sp_flux, sp_errors)
