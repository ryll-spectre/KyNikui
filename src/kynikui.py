from kivymd.app import MDApp

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder

from .constants.constants import Constants
from .components.views.window_manager.window_manager import WindowManager
from .components.views.dashboard.dashboard import Dashboard
from .kynikui_controller import kynikuiController

Window.size = (Constants.windowSize_Width, Constants.windowSize_Height)

class KyNikui(MDApp):
    """KyNikui main class."""

    windowManager: WindowManager

    dashboard: Dashboard

    background: str

    kynikuiController

    def build(self):

        kynikuiController._app = self
        self.kynikuiController = kynikuiController

        return Builder.load_file("main.kv")

    def __init__(self, **kwargs):
        super(MDApp, self).__init__(**kwargs)

        self.background    = None

        self.windowManager = None
        self.dashboard     = None

        Clock.schedule_once(self._finish_init, 1)

    def _finish_init(self, _):

        self.background = Constants.themeBackground_Light

        self.windowManager = self.root.ids['windowManager']
        self.dashboard     = self.root.ids['dashboard']