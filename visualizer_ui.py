# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(self.__class__, self).__init__()
        starting_values = {
            'amount_of_numbers' : 100,
            'max_value' : 200,
            'min_value' : 0
        }

        self.arrayAccesses = 0
        self.comparisons = 0
        self.setObjectName("MainWindow")
        self.resize(800,500)
        self.setStyleSheet('background-color: 240,240,240')
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 10)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_ViewAndName = QtWidgets.QVBoxLayout()
        self.verticalLayout_ViewAndName.setObjectName("verticalLayout_ViewAndName")
        self.label_algName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.label_algName.setFont(font)
        self.label_algName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_algName.setObjectName("label_algName")
        self.verticalLayout_ViewAndName.addWidget(self.label_algName)
        self.graphicsScene = QtWidgets.QGraphicsScene()
        self.graphicsScene.setBackgroundBrush(QtGui.QColor(240,240,240))
        self.graphicsView = QtWidgets.QGraphicsView(self.graphicsScene, parent = self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("border-width: 0px; border-style: solid; background-color: 240,240,240;")
        transform = QtGui.QTransform()
        transform.scale(1, -1)
        self.graphicsView.setTransform(transform)
        self.verticalLayout_ViewAndName.addWidget(self.graphicsView)
        self.gridLayout_3.addLayout(self.verticalLayout_ViewAndName, 0, 0, 1, 1)
        self.gridLayout_bottomMenu = QtWidgets.QGridLayout()
        self.gridLayout_bottomMenu.setObjectName("gridLayout_bottomMenu")
        self.pushButton_randomize = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_randomize.sizePolicy().hasHeightForWidth())
        self.pushButton_randomize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        self.pushButton_randomize.setFont(font)
        self.pushButton_randomize.setObjectName("pushButton_randomize")
        self.gridLayout_bottomMenu.addWidget(self.pushButton_randomize, 2, 2, 1, 1)
        self.horizontalLayout_ValueLimits = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ValueLimits.setObjectName("horizontalLayout_ValueLimits")
        self.verticalLayout_MinValue = QtWidgets.QVBoxLayout()
        self.verticalLayout_MinValue.setObjectName("verticalLayout_MinValue")
        self.labelMinValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.labelMinValue.setFont(font)
        self.labelMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMinValue.setObjectName("labelMinValue")
        self.verticalLayout_MinValue.addWidget(self.labelMinValue)
        self.spinBoxMinValue = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxMinValue.setObjectName("spinBoxMinValue")
        self.spinBoxMinValue.setValue(starting_values['min_value'])
        self.spinBoxMinValue.setMaximum(starting_values['max_value']-1)
        self.verticalLayout_MinValue.addWidget(self.spinBoxMinValue)
        self.horizontalLayout_ValueLimits.addLayout(self.verticalLayout_MinValue)
        self.verticalLayout_MaxValue = QtWidgets.QVBoxLayout()
        self.verticalLayout_MaxValue.setObjectName("verticalLayout_MaxValue")
        self.labelMaxValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.labelMaxValue.setFont(font)
        self.labelMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMaxValue.setObjectName("labelMaxValue")
        self.verticalLayout_MaxValue.addWidget(self.labelMaxValue)
        self.spinBoxMaxValue = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxMaxValue.setObjectName("spinBoxMaxValue")
        self.spinBoxMaxValue.setValue(starting_values['max_value'])
        self.spinBoxMaxValue.setMaximum(100000)
        self.spinBoxMaxValue.setMinimum(1)
        self.spinBoxMaxValue.setValue(starting_values['max_value'])
        self.spinBoxMaxValue.setSingleStep(10)
        self.spinBoxMinValue.setSingleStep(10)
        self.spinBoxMaxValue.setFont(font)
        self.spinBoxMinValue.setFont(font)
        self.verticalLayout_MaxValue.addWidget(self.spinBoxMaxValue)
        self.horizontalLayout_ValueLimits.addLayout(self.verticalLayout_MaxValue)
        self.gridLayout_bottomMenu.addLayout(self.horizontalLayout_ValueLimits, 0, 1, 2, 1)
        self.label_comparisons = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.label_comparisons.setFont(font)
        self.label_comparisons.setAlignment(QtCore.Qt.AlignCenter)
        self.label_comparisons.setObjectName("label_comparisons")
        self.gridLayout_bottomMenu.addWidget(self.label_comparisons, 1, 0, 1, 1)
        self.pushButton_changeAlg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_changeAlg.sizePolicy().hasHeightForWidth())
        self.pushButton_changeAlg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        self.pushButton_changeAlg.setFont(font)
        self.pushButton_changeAlg.setObjectName("pushButton_changeAlg")
        self.gridLayout_bottomMenu.addWidget(self.pushButton_changeAlg, 2, 0, 1, 1)
        self.horizontalSlider_amountOfNumbs = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_amountOfNumbs.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_amountOfNumbs.setSizePolicy(sizePolicy)
        self.horizontalSlider_amountOfNumbs.setMinimum(5)
        self.horizontalSlider_amountOfNumbs.setMaximum(1000)
        self.horizontalSlider_amountOfNumbs.setSingleStep(10)
        self.horizontalSlider_amountOfNumbs.setPageStep(0)
        self.horizontalSlider_amountOfNumbs.setProperty("value", starting_values['amount_of_numbers'])
        self.horizontalSlider_amountOfNumbs.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_amountOfNumbs.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_amountOfNumbs.setTickInterval(50)
        self.horizontalSlider_amountOfNumbs.setObjectName("horizontalSlider_amountOfNumbs")
        self.gridLayout_bottomMenu.addWidget(self.horizontalSlider_amountOfNumbs, 1, 2, 1, 1)
        self.label_arrayAccesses = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.label_arrayAccesses.setFont(font)
        self.label_arrayAccesses.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arrayAccesses.setObjectName("label_arrayAccesses")
        self.gridLayout_bottomMenu.addWidget(self.label_arrayAccesses, 0, 0, 1, 1)
        self.label_amountOfNumbs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        self.label_amountOfNumbs.setFont(font)
        self.label_amountOfNumbs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_amountOfNumbs.setObjectName("label_amountOfNumbs")
        self.gridLayout_bottomMenu.addWidget(self.label_amountOfNumbs, 0, 2, 1, 1)
        self.pushButton_startStop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_startStop.sizePolicy().hasHeightForWidth())
        self.pushButton_startStop.setSizePolicy(sizePolicy)
        self.pushButton_startStop.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_startStop.setStyleSheet('color: rgb(0, 90, 180);')
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_startStop.setFont(font)
        self.pushButton_startStop.setObjectName("pushButton_startStop")
        self.gridLayout_bottomMenu.addWidget(self.pushButton_startStop, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_bottomMenu, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 5)
        self.setCentralWidget(self.centralwidget)

        self.horizontalSlider_amountOfNumbs.valueChanged.connect(lambda new_amount: self.label_amountOfNumbs.setText(f"Amount of numbers: {new_amount}"))
        self.spinBoxMaxValue.valueChanged.connect(lambda new_value: self.spinBoxMinValue.setMaximum(new_value-1))
        self.retranslateUi(starting_values)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, starting_values: dict):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_algName.setText(_translate("MainWindow", ""))
        self.pushButton_randomize.setText(_translate("MainWindow", "Randomize"))
        self.labelMinValue.setText(_translate("MainWindow", "Min.value"))
        self.labelMaxValue.setText(_translate("MainWindow", "Max.value"))
        self.pushButton_changeAlg.setText(_translate("MainWindow", "Change algorithm"))
        self.label_arrayAccesses.setText(_translate("MainWindow", f"Array accesses: {self.arrayAccesses}"))
        self.label_comparisons.setText(_translate("MainWindow", f"Comparisons: {self.comparisons}"))
        self.label_amountOfNumbs.setText(_translate("MainWindow", "Amount of numbers: " + str(starting_values['amount_of_numbers'])))
        self.pushButton_startStop.setText(_translate("MainWindow", "START"))

    def resizeEvent(self, event):
        self.resized.emit()

        return super(self.__class__, self).resizeEvent(event)