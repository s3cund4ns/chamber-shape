from cshape_objects.detectors.detector_creator import create_detector
from models.model_calculation_parameters import ModelCalculationParameters
from models.model_input_data import ModelInputData
from models.model_lattices_list import ModelLatticesList
from models.model_materials_list import ModelMaterialsList
from models.model_output_data import ModelOutputData
from project_data.model import Model
from cshape_objects.detectors.detector import Detector, DetectorsTypes


class ModelDetectorsList(Model):

    def __init__(self):
        super(ModelDetectorsList, self).__init__()
        self.data: list = []
        self.selected_item_index = -1
        self.materials_model: ModelMaterialsList | None = None
        self.lattices_model: ModelLatticesList | None = None
        self.input_data_model: ModelInputData | None = None
        self.calculation_parameters_model: ModelCalculationParameters | None = None
        self.output_data_model: ModelOutputData | None = None

    def add_item(self, index: int, detector_type):
        item: Detector = create_detector(detector_type)
        self.data.insert(index, item)
        item_text = f'{item.get_type()} {item.get_name()}'
        self.view_model.add_item_to_views(index, item_text, item)
        item_type = item.get_type()
        match item_type:
            case DetectorsTypes.MaterialDetector:
                self.input_data_model.update_detectors_data(self.dump_data(), self.calculation_parameters_model.data[2], self.materials_model.data)
            case DetectorsTypes.LatticeDetector:
                self.input_data_model.update_detectors_data(self.dump_data(), self.calculation_parameters_model.data[2], self.lattices_model.data)

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Detector = self.data[self.selected_item_index]
        selected_item.energy_grid = self.calculation_parameters_model.data[2]
        item_type = selected_item.get_type()
        match item_type:
            case DetectorsTypes.MaterialDetector:
                selected_item.all_materials = self.materials_model.data
            case DetectorsTypes.LatticeDetector:
                selected_item.all_lattices = self.lattices_model.data

        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views(self.selected_item_index, value,
                                             [self.data[self.selected_item_index].get_type(),
                                              self.data[self.selected_item_index].get_name()])
        item_type = self.data[self.selected_item_index].get_type()
        match item_type:
            case DetectorsTypes.MaterialDetector:
                self.input_data_model.update_detectors_data(self.dump_data(), self.calculation_parameters_model.data[2], self.materials_model.data)
            case DetectorsTypes.LatticeDetector:
                self.input_data_model.update_detectors_data(self.dump_data(), self.calculation_parameters_model.data[2], self.lattices_model.data)

    def set_output_data(self, output_data: tuple):
        selected_item: Detector = self.data[self.selected_item_index]
        selected_item.set_output_data(output_data)

    def get_output_data(self):
        selected_item: Detector = self.data[self.selected_item_index]
        return selected_item.get_output_data()

    def show_plot(self):
        selected_item: Detector = self.data[self.selected_item_index]
        detector_name = selected_item.get_name()
        if selected_item.is_output_data_empty():
            output_data = self.output_data_model.output_data_writer.get_plot_output(detector_name)
            selected_item.set_output_data(output_data)
        energy_mid_grid, sp_flux, sp_errors = selected_item.get_output_data()
        self.output_data_model.translate_plot_info(detector_name, energy_mid_grid, sp_flux, sp_errors)

    def clear_data(self):
        self.data.clear()
        self.view_model.clear_views()

    def dump_data(self):
        data = []
        for detector in self.data:
            data.append(detector.dump_data())
        return data

    def load_data(self, detectors_data: list):
        for detector in detectors_data:
            detector_index = detectors_data.index(detector)
            detector_type = detector['Type']
            self.add_item(detector_index, detector_type)
            self.select_item(detector_index)
            self.data[self.selected_item_index].energi_grid = self.calculation_parameters_model.data[2]
            detector_tuple = tuple(detector.items())
            for detector_property in detector_tuple[1:]:
                self.change_data(detector_property)
