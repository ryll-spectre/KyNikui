"""
Holds constant values used throughout the application.
"""

import kivy.utils

class Constants:
    """Application constants.
    """

    windowSize_Width  = 1366
    windowSize_Height = 768

    themeBackground_Light = kivy.utils.get_color_from_hex("E4E4E4")
    themeButtons_Light    = kivy.utils.get_color_from_hex("5DEEFF")

    themeBackground_Dark = kivy.utils.get_color_from_hex("003339")
    themeButtons_Dark    = kivy.utils.get_color_from_hex("6B35FF")