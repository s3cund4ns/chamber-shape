from dataclasses import dataclass


@dataclass
class Localization:
    file_menu: str | None = None
    new_project_action: str | None = None
    open_action: str | None = None
    save_action: str | None = None
    save_as_action: str | None = None
    settings_action: str | None = None
    edit_menu: str | None = None
    cut_action: str | None = None
    copy_action: str | None = None
    paste_action: str | None = None
    project_menu: str | None = None
    run_simulation_action: str | None = None
    open_input_data_action: str | None = None
    calculation_menu: str | None = None
    neutron_population_action: str | None = None
    boundary_conditions_action: str | None = None
    energy_grid_action: str | None = None
    output_action: str | None = None
    help_menu: str | None = None
    manual_action: str | None = None
    about_action: str | None = None
    input_data_editor_tab_name: str | None = None
    save_project_directory_caption: str | None = None
    open_project_directory_caption: str | None = None
    viewport_tab_name: str | None = None
    universes_dock_title: str | None = None
    surfaces_dock_title: str | None = None
    materials_dock_title: str | None = None
    cells_dock_title: str | None = None
    properties_dock_title: str | None = None
    detectors_dock_title: str | None = None
    pins_dock_title: str | None = None
    lattices_dock_title: str | None = None
    start_widget_title: str | None = None
    start_widget_header: str | None = None
    start_widget_create_project: str | None = None
    start_widget_open_project: str | None = None
    new_project_widget_title: str | None = None
    new_project_widget_header: str | None = None
    new_project_widget_label_name: str | None = None
    new_project_widget_label_project_directory: str | None = None
    new_project_widget_label_precision_code: str | None = None
    new_project_widget_label_precision_code_directory: str | None = None
    new_project_widget_label_nuclear_data_library: str | None = None
    new_project_widget_label_nuclear_data_library_directory: str | None = None
    new_project_widget_create: str | None = None
    new_project_widget_cancel: str | None = None
    new_project_widget_choose_project_directory_caption: str | None = None
    new_project_widget_choose_precision_code_caption: str | None = None
    new_project_widget_choose_nuclear_data_library_caption: str | None = None
    settings_widget_title: str | None = None
