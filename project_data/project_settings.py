from dataclasses import dataclass


@dataclass
class ProjectSettings:
    project_name: str = ''
    project_directory: str = ''
    solver: str = ''
    solver_directory: str = ''
    calculation_data_directory: str = ''
    nuclear_data_library: str = ''
    nuclear_data_library_directory: str = ''
