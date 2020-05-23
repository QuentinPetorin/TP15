from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit, QDialog

from P21 import LabeledTextField

class ConfigurationDialog(QDialog):

    def __init__(self):
        self.A = LabeledTextField('IP')
        self.B = LabeledTextField('User')
        self.C = LabeledTextField('Password')







if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   win.show()
   app.exec_()




















