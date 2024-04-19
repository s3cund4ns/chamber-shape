import subprocess


def load_serpent(file_path: str):
    path = 'Projects/project.inp'
    program_path = "/mnt/d/serpent/Serpent2130/sss2"
    subprocess.run(["dos2unix", path])
    subprocess.run(["bash", "-c", f"{program_path} {file_path}"])
