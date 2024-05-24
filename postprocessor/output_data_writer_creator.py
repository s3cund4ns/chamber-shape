from postprocessor.serpent_output_data_writer import SerpentOutputDataWriter
from solvers.solver import Solvers

output_data_writers: dict = {
    Solvers.Serpent: SerpentOutputDataWriter
}


def create_output_data_writer(output_data_writer, calculation_data_path):
    return output_data_writers[output_data_writer](calculation_data_path)
