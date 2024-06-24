from postprocessor.output_data_writer import OutputDataWriter


class OpenMCOutputDataWriter(OutputDataWriter):
    def __init__(self, calculation_data_path: str):
        super().__init__(calculation_data_path)

    def get_calculation_output(self):
        pass

    def get_plot_output(self, detector_name: str):
        pass
