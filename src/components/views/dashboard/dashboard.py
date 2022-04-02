from kivy.clock import Clock

from ..controls.KynikuiScreen import KynikuiScreen
from ....kynikui_controller import kynikuiController

class Dashboard(KynikuiScreen):
    """Dashboard home page when starting KyNikui
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._controller = None

        Clock.schedule_once(self._finish_init, 1)

    def _finish_init(self, _) -> None:

        self._controller = kynikuiController

        print(f'Finished initializing Dashboard page') 