class Color:
    def __init__(self, color):
        self._color = color# para encapsular se agrega el _ al atributo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color[color:{self._color}]'