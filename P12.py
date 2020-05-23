from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit

class ButtonsPanel(QWidget):

    def __init__(self):

        QWidget.__init__(self)
        mainWidget = QWidget()

        self.layout1 = QHBoxLayout()
        self.button1 = QPushButton("Configure")
        self.button2 = QPushButton("Connect")
        self.button3 = QPushButton("Disconnect")

        self.layout1.addWidget(self.button1)
        self.layout1.addWidget(self.button2)
        self.layout1.addWidget(self.button3)

        self.setLayout(self.layout1)



if __name__ == "__main__":
    app = QApplication([])
    win = ButtonsPanel()
    win.show()
    app.exec_()


