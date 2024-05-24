from viewmodels.view_model_calculation_parameters import ViewModelCalculationParameters
from viewmodels.view_model_cells_list import ViewModelCellsList
from viewmodels.view_model_detectors_list import ViewModelDetectorsList
from viewmodels.view_model_input_data import ViewModelInputData
from viewmodels.view_model_lattices_list import ViewModelLatticesList
from viewmodels.view_model_materials_list import ViewModelMaterialsList
from viewmodels.view_model_output_data import ViewModelOutputData
from viewmodels.view_model_pins_list import ViewModelPinsList
from viewmodels.view_model_surfaces_list import ViewModelSurfacesList
from viewmodels.view_model_universes_list import ViewModelUniversesList


class ViewModelsData:
    def __init__(self):
        self.universes_view_model = ViewModelUniversesList()
        self.materials_view_model = ViewModelMaterialsList()
        self.surfaces_view_model = ViewModelSurfacesList()
        self.cells_view_model = ViewModelCellsList()
        self.pins_view_model = ViewModelPinsList()
        self.lattices_view_model = ViewModelLatticesList()
        self.detectors_view_model = ViewModelDetectorsList()
        self.calculation_parameters_view_model = ViewModelCalculationParameters()
        self.input_data_view_model = ViewModelInputData()
        self.output_data_view_model = ViewModelOutputData()
