from dataclasses import dataclass


@dataclass
class ThemeSettings:
    qss_file: str | None = None
    viewport_color: tuple[int, int, int, int] | None = None
    dark_plot_style: bool | None = None
