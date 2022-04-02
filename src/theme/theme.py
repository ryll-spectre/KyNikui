import enum

from ..constants import Constants


class ThemeMode(enum.Enum):
        LIGHT = 1
        DARK  = 2

class Theme():
    """Contains values for the currently used color scheme in KyNikui."""

    _themeMode: ThemeMode

    background: str

    def __init__(self) -> None:
        # TODO: Theme will be saved from previous session
        # Default to LIGHT for now
        self._themeMode = ThemeMode.LIGHT
        
        self.background = None

        self._switchThemeValues()

    def switchTheme(self) -> None:
        """TODO: This is going to swap the theme values out in this class."""
        if self._themeMode == ThemeMode.LIGHT:
            self._themeMode = ThemeMode.DARK
            self._switchThemeValues()
        else:
            self._themeMode = ThemeMode.LIGHT
            self._switchThemeValues()

    def _switchThemeValues(self) -> None:
        """Change all member values to new theme."""
        if self._themeMode == ThemeMode.LIGHT:
            self.background = Constants.themeBackground_Light
        else:
            pass