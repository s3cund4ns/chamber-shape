import os

import serpentTools

from postprocessor.output_data_writer import OutputDataWriter


class SerpentOutputDataWriter(OutputDataWriter):
    def __init__(self, calculation_data_path: str):
        super().__init__(calculation_data_path)

    def __find_output_file(self, suffix: str):
        for file in os.listdir(self.calculation_data_path):
            if file.endswith(suffix):
                return os.path.join(self.calculation_data_path, file)

    def get_calculation_output(self):
        calculation_output_file_path = self.__find_output_file('_res.m')
        calculation_output_data = serpentTools.read(calculation_output_file_path, reader='results')
        imp_keff, abs_kinf = calculation_output_data['impKeff'], calculation_output_data['absKinf']
        return imp_keff, abs_kinf

    def get_plot_output(self, detector_name: str):
        plot_output_file_path = self.__find_output_file('det0.m')
        detector_file = None
        if os.path.isfile(plot_output_file_path):
            detector_file = serpentTools.read(plot_output_file_path, reader='det')
        spectrum = detector_file.detectors[detector_name]
        energy_mid_grid = spectrum.grids['E'][:,2]
        sp_flux = spectrum.tallies
        sp_errors = spectrum.errors
        num = len(energy_mid_grid)
        f = sum(sp_flux)
        sp_flux = sp_flux / f * num

        return energy_mid_grid, sp_flux, sp_errors
