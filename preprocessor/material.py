
class Material:
    def __init__(self, name: str, density: float):
        self.name: str = name
        self.density: float = density
        self.nuclides: list[float] = []

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_density(self, density: float):
        self.density = density

    def get_density(self):
        return self.density

    def add_nuclide(self, fraction: float):
        self.nuclides.append(fraction)

    def delete_nuclide(self, nuclide_id: int):
        self.nuclides.pop(nuclide_id)

    def get_nuclide(self, index):
        return self.nuclides[index]

    def set_nuclide(self, index, value):
        self.nuclides[index] = value

    def get_nuclides(self):
        return self.nuclides

    def get_nuclides_count(self):
        return len(self.nuclides)





