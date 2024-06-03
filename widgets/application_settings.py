from dataclasses import dataclass


@dataclass
class ApplicationSettings:
    localization_config: str | None = None
    theme_config: str | None = None
