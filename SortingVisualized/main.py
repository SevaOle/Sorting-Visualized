import sys
from PyQt5 import QtWidgets
from editor_back import Editor
from editor_ui import Ui_AlgorithmEditor
from visualizer_back import Visualizer
from visualizer_ui import Ui_MainWindow
from PyQt5.QtGui import QIcon


# Setup
def main():
    """
    Launches the visualizer_ui, editor_ui and ties everything together
    """

    ### Initialization
    app = QtWidgets.QApplication(sys.argv)
    visualizer = Visualizer(Ui_MainWindow())
    editor = Editor(Ui_AlgorithmEditor())

    # Stacked widget allows to swap windows seemlesly
    stacked_widget = QtWidgets.QStackedWidget()
    stacked_widget.addWidget(visualizer.ui)
    stacked_widget.addWidget(editor.ui)
    stacked_widget.setCurrentWidget(visualizer.ui)
    stacked_widget.resize(800,500)
    stacked_widget.setWindowTitle("Sorting Visualized")
    stacked_widget.setWindowIcon(QIcon("icon.png"))

    sorts = editor.getSorts()
    if sorts:
        visualizer.selectAlg(sorts[0])
        editor.selectAlg(sorts[0])

    visualizer.ui.pushButton_changeAlg.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))
    editor.ui.pushButton_useAlg.clicked.connect(lambda: (visualizer.selectAlg(editor.selectedAlg),
                                                         visualizer.fitRectsInView(),
                                                         stacked_widget.setCurrentIndex(0)))

    stacked_widget.show()
    visualizer.initializeRects()
    visualizer.fitRectsInView()


    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
