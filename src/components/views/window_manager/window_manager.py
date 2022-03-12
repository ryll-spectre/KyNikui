from collections import deque
from typing import Deque

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ..controls.KynikuiScreen import KynikuiScreen


class WindowManager(ScreenManager):
    """Controller that manages transitions between screens.
    """

    _animationDuration: float

    _currentScreen: KynikuiScreen

    _windowStack: Deque[KynikuiScreen]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._animationDuration = .3
        self._currentScreen = None
        self._windowStack = deque()

    def proceedToScreen(self,
                        nextScreen: KynikuiScreen) -> None:
        """Proceeds to the given screen.

        ### Args:
        - nextScreen (KynikuiScreen): The next screen to proceed to.
        """

        if not self._currentScreen:
            self._currentScreen = App.get_running_app().root.ids[self.current]

        self._windowStack.append(self._currentScreen)

        self._changeScreen(nextScreen)

    def _changeScreen(self,
                      nextScreen: KynikuiScreen,
                      transitionDirection: str = "left") -> None:
        """Changes screen based on the given transitionDirection.

        ### Args:
        - nextScreen (KynikuiScreen): The next screen to proceed to.
        - transitionDirection (str, optional): Determines which direction the transition animates in. Default value is "left".
        """
        app = App.get_running_app()

        self._animateNavbar()

        self.transition.duration = self._animationDuration
        self.transition.direction = transitionDirection

        if self._currentScreen:
            self._currentScreen._onScreenExited()
        nextScreen._onScreenEntered()

        self.current = nextScreen.name
        self._currentScreen = nextScreen
        app._current = self._currentScreen