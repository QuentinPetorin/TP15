from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit, QTableWidget, QHeaderView

from P12 import ButtonsPanel

class SQLClientWindow(QWidget):

    def __init__(self):

        QWidget.__init__(self)
        mainWidget = QWidget()
        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.Panel = ButtonsPanel()
        self.layout.addWidget(self.Panel)
        self.notificationPanel = QTextEdit("text")
        self.layout.addWidget(self.notificationPanel)
        self.resultable = QTableWidget()
        self.layout.addWidget(self.resultable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch))
        self.setLayout(self.layout)






if __name__ == "__main__":
    app = QApplication([])
    win = SQLClientWindow()
    win.show()
    app.exec_()







