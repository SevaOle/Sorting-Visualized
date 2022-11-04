from PyQt5.QtWidgets import QDialog, QLabel, QDialogButtonBox, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.setWindowTitle("Sorting Visualized")
        self.setWindowIcon(QIcon("icon.png"))

        font = QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.button(QDialogButtonBox.Cancel).setStyleSheet("color: rgb(222, 0, 0);")
        self.buttonBox.button(QDialogButtonBox.Cancel).setFont(font)
        self.buttonBox.button(QDialogButtonBox.Ok).setFont(font)


        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.messageLabel = QLabel()
        font.setBold(False)
        self.messageLabel.setFont(font)
        self.layout.addWidget(self.messageLabel)
        self.layout.addWidget(self.buttonBox)
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)
