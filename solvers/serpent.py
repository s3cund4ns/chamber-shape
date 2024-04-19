import json
import os
import subprocess

from pydos2unix import dos2unix

from solvers.solver import Solver


class Serpent(Solver):
    def __init__(self, path: str, calculation_data_path: str):
        super().__init__()
        self.path = path
        self.calculation_data_path = calculation_data_path

    def load_tokens(self):
        with open('D:/Projects/chamber-shape/solvers/tokens/Serpent.json', 'r') as file:
            self.tokens = json.load(file)

    def create_input_data_file(self, file_name: str):
        with open(f'{self.calculation_data_path}/{file_name}', 'w') as file:
            file.write('')

    def save_input_data_file(self, file_name: str, input_data: list):
        with open(f'{self.calculation_data_path}/{file_name}', 'w') as file:
            for cshape_object_data in input_data:
                file.writelines(cshape_object_data)

    def start_calculation(self, file_name: str):
        path_to_input_data_file = f'{self.calculation_data_path}/{file_name}'
        with open(path_to_input_data_file, 'rb') as file:
            buffer = dos2unix(file)
        with open(path_to_input_data_file, 'wb') as file:
            file.write(buffer)
        path_to_input_data_file = self.replace_disk_letter_with_mnt(path_to_input_data_file)
        path_to_execute_file = f'{self.path}/sss2'
        path_to_execute_file = self.replace_disk_letter_with_mnt(path_to_execute_file)
        subprocess.run(["bash", "-c", f"{path_to_execute_file} {path_to_input_data_file}"])

    @staticmethod
    def replace_disk_letter_with_mnt(file_path):
        drive_letter, rest_of_path = os.path.splitdrive(file_path)
        mnt_path = "/mnt/" + drive_letter[0].lower() + rest_of_path
        return mnt_path

