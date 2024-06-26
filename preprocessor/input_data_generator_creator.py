from preprocessor.input_data_generator_for_openmc import InputDataGeneratorForOpenMC
from preprocessor.input_data_generator_for_serpent import InputDataGeneratorForSerpent
from solvers.solver import Solvers

solvers: dict = {
    Solvers.Serpent: InputDataGeneratorForSerpent,
    Solvers.OpenMC: InputDataGeneratorForOpenMC
}


def create_input_data_generator(input_data_generator):
    return solvers[input_data_generator]()
