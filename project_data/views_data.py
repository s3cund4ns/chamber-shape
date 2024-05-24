from renderer.views.view_lattice_renderer import ViewLatticeRenderer
from renderer.views.view_pin_renderer import ViewPinRenderer
from renderer.views.view_surface_renderer import ViewSurfaceRenderer
from widgets.views.view_cells_list import ViewCellsList
from widgets.views.view_detectors_list import ViewDetectorsList
from widgets.views.view_input_data import ViewInputData
from widgets.views.view_lattices_list import ViewLatticesList
from widgets.views.view_materials_list import ViewMaterialsList
from widgets.views.view_pins_list import ViewPinsList
from widgets.views.view_plot import ViewPlot
from widgets.views.view_properties import ViewMaterialProperties, ViewSurfaceProperties, ViewDetectorProperties, \
    ViewUniverseProperties, ViewCalculationParametersProperties, ViewCellProperties, ViewPinProperties, \
    ViewLatticeProperties, ViewOutputDataProperties
from widgets.views.view_surfaces_list import ViewSurfacesList
from widgets.views.view_universes_list import ViewUniversesList
from widgets.views.view_universes_tree import ViewUniversesTree


class ViewsData:
    def __init__(self):
        self.universes_list_view = ViewUniversesList()
        self.materials_list_view = ViewMaterialsList()
        self.surfaces_list_view = ViewSurfacesList()
        self.cells_list_view = ViewCellsList()
        self.pins_list_view = ViewPinsList()
        self.lattices_list_view = ViewLatticesList()
        self.detectors_list_view = ViewDetectorsList()
        self.material_properties_view = ViewMaterialProperties()
        self.surface_properties_view = ViewSurfaceProperties()
        self.cell_properties_view = ViewCellProperties()
        self.pin_properties_view = ViewPinProperties()
        self.lattice_properties_view = ViewLatticeProperties()
        self.detector_properties_view = ViewDetectorProperties()
        self.universe_properties_view = ViewUniverseProperties()
        self.calculation_parameters_properties_view = ViewCalculationParametersProperties()
        self.output_data_properties_view = ViewOutputDataProperties()
        self.surfaces_renderer_view = ViewSurfaceRenderer()
        self.pin_renderer_view = ViewPinRenderer()
        self.lattice_renderer_view = ViewLatticeRenderer()
        self.input_data_view = ViewInputData()
        self.plot_view = ViewPlot()

        self.lattice_renderer_view.pin_renderer_view = self.pin_renderer_view
