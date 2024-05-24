from models.model_calculation_parameters import ModelCalculationParameters
from models.model_cells_list import ModelCellsList
from models.model_detectors_list import ModelDetectorsList
from models.model_input_data import ModelInputData
from models.model_lattices_list import ModelLatticesList
from models.model_materials_list import ModelMaterialsList
from models.model_output_data import ModelOutputData
from models.model_pins_list import ModelPinsList
from models.model_surfaces_list import ModelSurfacesList
from models.model_universes_list import ModelUniversesList


class ModelsData:
    def __init__(self):
        self.universes_model = ModelUniversesList()
        self.materials_model = ModelMaterialsList()
        self.surfaces_model = ModelSurfacesList()
        self.cells_model = ModelCellsList()
        self.pins_model = ModelPinsList()
        self.lattices_model = ModelLatticesList()
        self.detectors_model = ModelDetectorsList()
        self.calculation_parameters_model = ModelCalculationParameters()
        self.input_data_model = ModelInputData()
        self.output_data_model = ModelOutputData()

        self.cells_model.materials_model = self.materials_model
        self.cells_model.surfaces_model = self.surfaces_model
        self.cells_model.universes_model = self.universes_model
        self.cells_model.input_data_model = self.input_data_model

        self.pins_model.materials_model = self.materials_model
        self.pins_model.universes_model = self.universes_model
        self.pins_model.input_data_model = self.input_data_model

        self.lattices_model.pins_model = self.pins_model
        self.lattices_model.universes_model = self.universes_model
        self.lattices_model.input_data_model = self.input_data_model

        self.detectors_model.materials_model = self.materials_model
        self.detectors_model.lattices_model = self.lattices_model
        self.detectors_model.input_data_model = self.input_data_model
        self.detectors_model.output_data_model = self.output_data_model

        self.calculation_parameters_model.input_data_model = self.input_data_model

        self.materials_model.input_data_model = self.input_data_model
        self.surfaces_model.input_data_model = self.input_data_model
        self.universes_model.input_data_model = self.input_data_model
