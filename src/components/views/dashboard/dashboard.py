from kivy.clock import Clock

from ..controls.KynikuiScreen import KynikuiScreen

class Dashboard(KynikuiScreen):
    """Dashboard home page when starting KyNikui
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._title = ""

        Clock.schedule_once(self._finish_init)

    def _finish_init(self, _) -> None:

        print(f'Finished initializing Dashboard page')