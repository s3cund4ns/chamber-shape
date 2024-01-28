
class Material:
    def __init__(self, name: str, density: float):
        self.name: str = name
        self.density: float = density
        self.nuclides: list[float] = []

    def set_name(self, name: str):
        self.name = name

    def set_density(self, density: float):
        self.density = density

    def add_nuclide(self, fraction: float):
        self.nuclides.append(fraction)

    def delete_nuclide(self, nuclide_id: int):
        self.nuclides.pop(nuclide_id)





