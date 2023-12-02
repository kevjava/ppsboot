class InputFile:
    def __init__(self, filename: str) -> None:
        self._filename = filename

    def as_single_ints(self) -> list[int]:
        """ Returns the input file as a list of ints. """
        with open(self._filename) as f:
            return [int(line) for line in f.readlines()]

    def as_single_strings(self) -> list[str]:
        """ Returns the input file as a list of strings. """
        with open(self._filename) as f:
            return [line.strip() for line in f.readlines()]

    def as_character_lists(self) -> list[list[str]]:
        """ Returns the input file as a list of lists of characters. """
        with open(self._filename) as f:
            return [list(line.strip()) for line in f.readlines()]

    def as_tuples(self) -> list[tuple]:
        """ Returns the input file as a list of tuples. """
        with open(self._filename) as f:
            return [tuple(line.split()) for line in f.readlines()]

    @property
    def filename(self) -> str:
        """ Returns the filename. """
        return self._filename
