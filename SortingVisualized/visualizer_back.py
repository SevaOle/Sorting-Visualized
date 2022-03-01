import importlib.util

from PyQt5 import QtCore, QtWidgets

from graphint import GraphInt, GraphRects


class Visualizer:
    """
    Class responsible for functioning of the visualizer.
    """
    def __init__(self, ui_visuzliser: QtWidgets.QMainWindow):
        self.ui = ui_visuzliser
        self.rects = None
        self.selectedAlg = None
        self.sorting = False


    def initializeRects(self):
        """
        Needs to be called after window.show()
        Made to properly display rectangles on program start.
        """
        self.rects = GraphRects(graphicsScene=self.ui.graphicsScene, graphicsView=self.ui.graphicsView,
                                amount=self.ui.horizontalSlider_amountOfNumbs.value(),
                                min=self.ui.spinBoxMinValue.value(), max=self.ui.spinBoxMaxValue.value())
        self.ui.horizontalSlider_amountOfNumbs.valueChanged.connect(self.rects.change_amount)
        self.ui.pushButton_randomize.clicked.connect(self.rects.randomize)
        self.ui.resized.connect(self.fitRectsInView)
        self.ui.horizontalSlider_amountOfNumbs.valueChanged.connect(self.fitRectsInView)
        self.ui.spinBoxMinValue.valueChanged.connect(self.change_min)
        self.ui.spinBoxMaxValue.valueChanged.connect(self.change_max)
        self.ui.pushButton_startStop.clicked.connect(self.start)
        self.rects.numbers[0].connect_compare(self.increase_comparisons)
        self.rects.numbers[0].connect_getValue(self.increase_accesses)


    def fitRectsInView(self):
        """
        Scales the graphicsView appropriately when window is resized or amount is changed
        """
        width = self.rects.get_fullWidth()
        self.ui.graphicsView.fitInView(QtCore.QRectF(0, self.rects.max, width, self.rects.max))
        self.ui.graphicsView.setSceneRect(0, 0, width, self.rects.max)

    def change_min(self, new_min: int):
        if new_min >= self.rects.max:
            self.ui.spinBoxMinValue.setValue(self.rects.min)
        else:
            self.rects.set_min(new_min)
            self.rects.randomize()
            self.fitRectsInView()

    def change_max(self, new_max: int):
        if new_max <= self.rects.min:
            self.ui.spinBoxMaxValue.setValue(self.rects.max)
        else:
            self.rects.set_max(new_max)
            self.rects.randomize()
            self.fitRectsInView()


    def start(self):
        """
        Executes selected sorting algorithm self.selectedAlg
        """
        if self.selectedAlg is None:
            return None
        ##### Display message?
        try:
            self.ui.arrayAccesses = 0
            self.ui.label_arrayAccesses.setText(f"Array accesses: {self.ui.arrayAccesses}")
            self.ui.comparisons = 0
            self.ui.label_comparisons.setText(f"Comparisons: {self.ui.comparisons}")
            self.rects.numbers[0].connect_setValue(self.change_value)
            self.ui.pushButton_startStop.setText('STOP')
            self.ui.pushButton_startStop.setStyleSheet('color: rgb(222, 0, 0);')
            self.sorting = True
            spec = importlib.util.spec_from_file_location(self.selectedAlg, f"./algorithms/{self.selectedAlg}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            self.ui.pushButton_startStop.clicked.disconnect()
            self.ui.pushButton_startStop.clicked.connect(self.stop)

            module.main(self.rects.numbers)
            self.stop()
        except Exception as exc:
            print("Exception occurred during sorting:\n", exc)
            self.sorting = False

    def stop(self):
        """
        Stops sorting by throwing zero division exception.
        """
        self.ui.pushButton_startStop.setText('START')
        self.ui.pushButton_startStop.setStyleSheet('color: rgb(0, 70, 160);')
        self.ui.pushButton_startStop.clicked.disconnect()
        self.ui.pushButton_startStop.clicked.connect(self.start)
        self.rects.numbers[0].connect_setValue(lambda *args: 1/0) # Raising an exception to stop sorting


    def selectAlg(self, algName):
        """
        Changes current algorithm.
        """
        self.selectedAlg = algName
        self.ui.label_algName.setText(algName)

    def increase_accesses(self, *args):
        self.ui.arrayAccesses += 1
        self.ui.label_arrayAccesses.setText(f"Array accesses: {self.ui.arrayAccesses}")
    def increase_comparisons(self, *args):
        self.ui.comparisons += 1
        self.ui.label_comparisons.setText(f"Comparisons: {self.ui.comparisons}")


    def change_value(self, target: GraphInt, value: int):
        """
        Changes value of a number (height of rectangle), displays the change
        """
        target_rect = self.rects.rects[target]
        new_rect = target_rect.rect()
        new_rect.setHeight(value)
        target_rect.setRect(new_rect)

        if target._enumerator <= value:
            self.ui.graphicsScene.update(target_rect.rect())
        else:
            rect = target_rect.rect()
            rect.setHeight(target._enumerator)
            self.ui.graphicsScene.update(rect)
        target._enumerator = value

        QtWidgets.QApplication.processEvents()
        self.ui.graphicsScene.update()
