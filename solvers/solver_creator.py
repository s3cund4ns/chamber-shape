from solvers.openmc import OpenMC
from solvers.serpent import Serpent
from solvers.solver import Solvers

solvers: dict = {
    Solvers.Serpent: Serpent,
    Solvers.OpenMC: OpenMC
}


def create_solver(solver: str, solver_path: str, calculation_data_path: str):
    return solvers[solver](solver_path, calculation_data_path)
