import sys
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _directions (Dict): A dictionary containing Points for U, D, L, and
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        self._words = {}
        self._letter['abcdefghijklmnopqrstuvwxyz']
        self._current = self._letter[30]
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if event == 27:
                sys.exit()
            elif event == 10: 
                result = "*"
            elif event >= 97 and event <= 122: 
                result = chr(event)
            self._current = self._letters.get(event, self._current)
        return result

        return self._current