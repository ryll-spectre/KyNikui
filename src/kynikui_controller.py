
from .theme.theme import Theme

class KynikuiController:
    """Main controller of the KyNikui application.
    """

    theme: Theme

    def __init__(self) -> None:
        self.theme = Theme()

kynikuiController: KynikuiController = KynikuiController()