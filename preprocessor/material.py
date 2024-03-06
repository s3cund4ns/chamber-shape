from dataclasses import dataclass


@dataclass
class Properties:
    Name = 'Name'
    Density = 'Density'
    Mode = 'Mode'
    Nuclides = 'Nuclides'
    Add = 'Add'
    Delete = 'Delete'


@dataclass
class Mode:
    Atomic = 'Atomic'
    Massive = 'Massive'
    Summary = 'Summary'


class Material:
    def __init__(self):
        self.name: str = 'NewMaterial'
        self.density: float = 0.0
        self.modes: dict = {'Atomic': 'Atomic', 'Massive': 'Massive', 'Summary': 'Summary'}
        self.mode = self.modes['Atomic']
        self.nuclides: list[list[str | float]] = []
        self.add_nuclide()

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_density(self, density: float):
        self.density = density

    def get_density(self):
        return self.density

    def add_nuclide(self):
        self.nuclides.append(['NewNuclide', 0.0])

    def delete_nuclide(self, nuclide_id: int):
        self.nuclides.pop(nuclide_id)

    def get_nuclide(self, index):
        return self.nuclides[index]

    def set_nuclide(self, index, name: str, density: float):
        self.nuclides[index] = [name, density]

    def get_nuclides(self):
        return self.nuclides

    def get_nuclides_count(self):
        return len(self.nuclides)

    def get_data(self):
        return {'Name': self.name, 'Density': self.density, 'Mode': [self.modes, self.mode], 'Nuclides': self.nuclides}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Name:
                name = value
                self.name = name
            case Properties.Density:
                density = value
                self.set_density(density)
            case Properties.Mode:
                mode = value
                self.mode = self.modes[mode]
            case Properties.Nuclides:
                index, name, density = value
                self.set_nuclide(index, name, density)
            case Properties.Add:
                index, name, density = value
                self.add_nuclide()
                self.set_nuclide(index, name, density)
            case Properties.Delete:
                index = value
                self.delete_nuclide(index)
