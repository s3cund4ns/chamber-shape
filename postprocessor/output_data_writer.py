from abc import ABC, abstractmethod


class OutputDataWriter(ABC):
    def __init__(self, calculation_data_path: str):
        super().__init__()
        self.calculation_data_path: str = calculation_data_path

    @abstractmethod
    def get_calculation_output(self):
        pass

    @abstractmethod
    def get_plot_output(self, detector_name: str):
        pass
