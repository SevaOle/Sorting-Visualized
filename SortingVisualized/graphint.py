from random import choice, randint
from string import printable

from PyQt5 import QtCore, QtWidgets, QtGui


class GraphInt:
    """
    Used insted of regular integers to track changes in values during sorting.
    """
    _rectWidth = 5
    __accessvalue_link = lambda *params: None # Gets called everytime the value of the object is accessed
    __valuechange_link = lambda *params: None # Gets called everytime the value of the object is changed
    __compare_link = lambda *params: None # Gets called everytime the value of the object is compared

    def __init__(self, enumerator: int):
        if enumerator < 0:
            raise ValueError(self.__class__.__name__, "cannot be smaller than 0.")
        self._id = ''.join([choice(printable) for _ in range(20)])
        self._enumerator = int(enumerator)

    def getValue(self):
        self.__class__.__accessvalue_link(self)
        return self._enumerator

    def setValue(self, number):
        """
        :param number: int

        Changes enumerator of the object, calls linked function
        """

        if isinstance(number, GraphInt):
            number = number.getValue()
        if number < 0:
            raise ValueError(f"{self.__class__.__name__} cannot be lower than zero.")
        else:
            self.__class__.__valuechange_link(self, number)  # Calls the linked function with the OLD GRAPHING and the NEW INT numbers
            self._enumerator = number
            return self

    @classmethod
    def connect_setValue(cls, function):
        """
        :param function: a function that will be called everytime the value is changed
        """
        cls.__valuechange_link = function


    @classmethod
    def connect_getValue(cls, function):
        """
        :param function: a function that will be called everytime the value is accessed
        """
        cls.__accessvalue_link = function


    @classmethod
    def connect_compare(cls, function):
        """
        :param function: a function that will be called everytime the value is changed
        """
        cls.__compare_link = function

    def __repr__(self):
        return str(self._enumerator)

    def __hash__(self):
        return self._id.__hash__()

    def __lt__(self, other): # <
        self.__compare_link(self, other, '<')

        if isinstance(other, GraphInt):
            return self.getValue() < other.getValue()
        else:
            return self.getValue() < other

    def __le__(self, other): # <=
        self.__compare_link(self, other, '<=')
        if isinstance(other, GraphInt):
            return self.getValue() <= other.getValue()
        else:
            return self.getValue() <= other

    def __eq__(self, other): # ==
        self.__compare_link(self, other, '<=')
        if isinstance(other, GraphInt):
            return self.getValue() == other.getValue()
        else:
            return self.getValue() == other

    def __ne__(self, other): # !=
        self.__compare_link(self, other, "!=")
        if isinstance(other, GraphInt):
            return self.getValue() != other.getValue()
        else:
            return self.getValue() != other

    def __gt__(self, other): # >
        self.__compare_link(self, other, ">")
        if isinstance(other, GraphInt):
            return self.getValue() > other.getValue()
        else:
            return self.getValue() > other

    def __ge__(self, other): # >=
        self.__compare_link(self, other, ">=")
        if isinstance(other, GraphInt):
            return self.getValue() >= other.getValue()
        else:
            return self.getValue() >= other

    def __add__(self, other): # +
        self._enumerator += other
        self.__valuechange_link(self)

    def __sub__(self, other): # -
        self._enumerator -= other
        self.__valuechange_link(self)

    def __mul__(self, other): # *
        self._enumerator *= other
        self.__valuechange_link(self)

    def __truediv__(self, other): # /
        self._enumerator /= other
        self.__valuechange_link(self)

    def __floordiv__(self, other): # //
        self._enumerator //= other
        self.__valuechange_link(self)





class GraphRects:
    """
    Used to represent a list of GraphInt as rectangles.
    """
    def __init__(self, graphicsScene: QtWidgets.QGraphicsScene, graphicsView: QtWidgets.QGraphicsView, amount, min = None, max = None, color = None):

        color = (0, 90, 180) if color is None else color
        self.__min =  0 if min is None else min
        self.__max = 900 if max is None else max
        self._graphicsScene = graphicsScene
        self._graphicsView = graphicsView
        self._brush = QtGui.QBrush(QtGui.QColor(color[0], color[1], color[2]), QtCore.Qt.SolidPattern)
        self.__width = int(self._graphicsView.width() / amount)
        self.numbers = [GraphInt(randint(min, max)) for _ in range(amount)]
        self.rects = {number: QtCore.QRectF() for index, number in enumerate(self.numbers)}
        for index, (numb, rect) in enumerate(self.rects.items()):
            rect.setCoords(self.__width * index, 0, self.__width * index + self.__width, numb._enumerator)
            self.rects[numb] = self._graphicsScene.addRect(rect, brush=self._brush)

    def get_fullWidth(self):
        return self.__width * len(self.numbers)

    @property
    def min(self):
        return self.__min
    @property
    def max(self):
        return self.__max
    @property
    def width(self):
        return self.__width

    def set_min(self, new_minimum_value: int):
        if new_minimum_value < self.__max:
            self.__min = new_minimum_value
        else:
            raise ValueError("Minimum value cannot be set higher than or equal to the maximum.")

    def set_max(self, new_maximum_value: int):
        if new_maximum_value > self.__min:
            self.__max = new_maximum_value
        else:
            raise ValueError("Maximum value cannot be set lower than or equal to the minimum.")

    def set_width(self, new_rect_width: int):
        if new_rect_width > 0:
            self.__width = new_rect_width
        else:
            raise ValueError("Rect width cannot be less than 1.")




    def change_amount(self, new_amount):
        if new_amount > len(self.numbers):
            for number in self.numbers:  # Change heights of existing rects
                new_height = randint(self.min, self.max)
                number._enumerator = new_height
                new_rect = self.rects[number].rect()
                new_rect.setHeight(new_height)
                self.rects[number].setRect(new_rect)

            for i in range(new_amount - len(self.numbers)):  # Add new rects
                new_int = GraphInt(randint(self.min, self.max))
                new_rect = QtCore.QRectF(self.width * len(self.numbers), 0, self.width, int(str(new_int)))
                self.numbers.append(new_int)
                self.rects[new_int] = new_rect

        elif new_amount < len(self.numbers):
            self.numbers = self.numbers[0:new_amount]
            self.rects = {numb : self.rects[numb] for numb in self.numbers}
            for number in self.numbers:  # Change heights of existing rects
                new_height = randint(self.min, self.max)
                number._enumerator = new_height
                new_rect = self.rects[number].rect()
                new_rect.setHeight(new_height)
                self.rects[number].setRect(new_rect)

        self.draw()

    def randomize(self):
        for number in self.numbers:
            new_height = randint(self.min, self.max)
            number._enumerator = new_height
            new_rect = self.rects[number].rect()
            new_rect.setHeight(new_height)
            self.rects[number].setRect(new_rect)
        self.draw()



    def draw(self, *args):
        self._graphicsScene.clear()
        for i, number in enumerate(self.numbers):
            new_rect = QtCore.QRectF()
            new_rect.setCoords(self.__width * i, 0, self.__width * i + self.__width, number._enumerator)
            self.rects[number] = self._graphicsScene.addRect(new_rect, brush = self._brush)

        QtWidgets.QApplication.processEvents()
