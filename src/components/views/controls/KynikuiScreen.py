from kivymd.uix.screen import MDScreen

class KynikuiScreen(MDScreen):
    """Parent for screen in KyNikui.

    ---
    ### Public Attributes
    - None

    ### Private Attributes
    - None
    
    ---
    ### Public Methods
    - None
    
    ### Private Methods
    - _finish_init() -> None:
        Post-construction field instantiation.
    - _onScreenEntered() -> None:
        Called when this screen is entered.
    - _onScreenExited() -> None:
        Called when this screen is exited
    """

    def _finish_init(self, _) -> None:
        """Post-construction field instantiation.
        
        This is necessary to get a reference to the fields created in the .kv
        file.
        """
        pass

    def _onScreenEntered(self) -> None:
        """'Start up' actions when this screen is entered."""
        pass

    def _onScreenExited(self) -> None:
        """'Clean up' actions when this screen is left."""
        pass
