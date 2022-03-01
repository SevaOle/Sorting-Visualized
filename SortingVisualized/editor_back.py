import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox
from sys import path
from dialog_ui import CustomDialog


class Editor:
    """
    Class responsible for functioning of the editor.
    """
    def __init__(self, ui_editor: QtWidgets.QMainWindow):
        self.ui = ui_editor
        self.selectedAlg = None
        self._buttonBackgroundColor_Selected = (220, 220, 220)
        self._buttonBackgroundColor_NotSelected = (230, 230, 230, 0)
        self.algorithms = dict() # {sort_name : QPushButton}
        path.insert(0, "/algorithms") # Temporarly add files from ./algorihms into path to allow import

        for sortname in self.getSorts():
            self.addSort(sortname)

        self.confirmationDialog = None

        self.ui.pushButton_createAlg.clicked.connect(self.createSort)
        self.ui.pushButton_saveAlg.clicked.connect(self.saveChanges)
        self.ui.pushButton_deleteAlg.clicked.connect(self.confirmDelete)

    @staticmethod
    def getSorts(foldername = "algorithms"):
        """
        :return list of algorithms without .py from foldername
        """
        return sorted([filename.replace('.py', '') for filename in filter(lambda filename: filename.endswith('.py'), os.listdir(f'./{foldername}'))])

    def addSort(self, sortname: str):
        """
        Creates a button to the left menu corresponding to the sort name, adds it in self.algorithms
        """
        self.algorithms[sortname] = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_buttonsAlgs)
        self.algorithms[sortname].setFont(self.ui.algfont)
        self.algorithms[sortname].setStyleSheet(f"background-color:rgb({self._buttonBackgroundColor_NotSelected})")
        self.algorithms[sortname].setObjectName(f"pushButton_{sortname}")
        self.ui.verticalLayout_buttonsAlgs.addWidget(self.algorithms[sortname])
        self.algorithms[sortname].setText(sortname)
        self.algorithms[sortname].clicked.connect(lambda: self.selectAlg(sortname))

    def createSort(self):
        if 'New algorithm' not in self.algorithms:
            sortname = 'New algorithm'
        else:
            i = 2
            sortname = f'New algorithm {i}'
            while sortname in self.algorithms:
                i += 1
                sortname = f'New algorithm {i}'
        with open(f'./algorithms/{sortname}.py', 'w') as new_file:
            with open('template_algorithm.py', 'r') as template:
                new_file.write(template.read())
        self.addSort(sortname)

    def selectAlg(self, sortname):
        """
        Called when button corresponding to one of the sorts is clicked.
        """
        if sortname == self.selectedAlg:
            return None

        if self.selectedAlg is not None:
            self.algorithms[self.selectedAlg].setStyleSheet(f"background-color:rgb{self._buttonBackgroundColor_NotSelected}")
            self.ui.algfont.setBold(False)
            self.algorithms[self.selectedAlg].setFont(self.ui.algfont)

        self.selectedAlg = sortname
        self.algorithms[sortname].setStyleSheet(f"background-color:rgb{self._buttonBackgroundColor_Selected}")
        self.ui.algfont.setBold(True)
        self.algorithms[sortname].setFont(self.ui.algfont)
        self.ui.algfont.setBold(False)

        self.ui.lineEdit_algName.setText(sortname)
        with open(f"./algorithms/{sortname}.py", "r") as code:
            self.ui.textEdit_algEditor.setText(code.read())


    def saveChanges(self):
        if self.selectedAlg is None:
            return None
        with open(f"./algorithms/{self.selectedAlg}.py", "w") as file:
            file.write(self.ui.textEdit_algEditor.toPlainText())


    def confirmDelete(self):
        if self.selectedAlg is None:
            return None
        self.confirmationDialog = CustomDialog()
        self.confirmationDialog.messageLabel.setText(f"Are you sure you want to delete {self.selectedAlg}?")

        self.confirmationDialog.buttonBox.button(QDialogButtonBox.Cancel).setText("Delete")
        self.confirmationDialog.buttonBox.button(QDialogButtonBox.Ok).setText("Cancel")
        
        self.confirmationDialog.buttonBox.rejected.connect(lambda: (self.deleteSort(self.selectedAlg), self.__deleteConfirmation()))
        self.confirmationDialog.buttonBox.accepted.connect(self.__deleteConfirmation)
        self.confirmationDialog.show()

    def deleteSort(self, sortname: str):
        try:
            os.remove(f"{os.path.abspath(os.getcwd())}\\algorithms\\{sortname}.py")
        except FileNotFoundError:
            return None
        self.selectedAlg = None
        self.ui.verticalLayout_buttonsAlgs.removeWidget(self.algorithms[sortname])
        del(self.algorithms[sortname])

        self.ui.lineEdit_algName.setText("")
        self.ui.textEdit_algEditor.setText("")

        self.ui.update()

    def __deleteConfirmation(self):
        del self.confirmationDialog
        self.confirmationDialog = None
