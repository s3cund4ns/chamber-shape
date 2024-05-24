from cshape_objects.calculation_output import CalculationOutput
from cshape_objects.plot_info import PlotInfo
from postprocessor.output_data_writer import OutputDataWriter
from postprocessor.output_data_writer_creator import create_output_data_writer
from project_data.model import Model


class ModelOutputData(Model):
    def __init__(self):
        super().__init__()
        self.output_data_writer: OutputDataWriter | None = None
        self.data: dict = {
            'CalculationOutput': CalculationOutput()
        }

    def create_output_data_writer(self, output_data_writer: str, calculation_data_path: str):
        self.output_data_writer: OutputDataWriter = create_output_data_writer(output_data_writer,
                                                                              calculation_data_path)

    def add_item(self, *args):
        cshape_object_data, index = args
        self.data[index].clear()
        self.data[index] = cshape_object_data
        self.view_model.add_item_to_views(self.data)

    def get_calculation_output(self):
        calculation_output: CalculationOutput = self.data['CalculationOutput']
        if calculation_output.is_clean():
            imp_keff, abs_kinf = self.output_data_writer.get_calculation_output()
            calculation_output.set_data(('ImpKeff', imp_keff))
            calculation_output.set_data(('AbsKinf', abs_kinf))
        self.view_model.select_item_in_views(calculation_output.get_data())

    def translate_plot_info(self, *plot_info):
        detector_name, energy_mid_grid, sp_flux, sp_errors = plot_info
        self.view_model.change_item_in_views(detector_name, energy_mid_grid, sp_flux, sp_errors)

    def change_data(self, value):
        plot_info: PlotInfo = self.data['PlotInfo']
        plot_info.set_data(value)
        self.view_model.change_item_in_views(value)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
