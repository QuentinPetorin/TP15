from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit



class LabeledTextField(QWidget):

    def __init__(self,text):

        QWidget.__init__(self,text)
        self.text = text
        self.layout = QHBoxLayout()
        self.label = QLabel(self.text)
        self.textedit = QTextEdit()
        self.textedit.setMaximumHeight(400)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textedit)
        self.setLayout(self.layout)



if __name__ == "__main__":
   app = QApplication([])
   text = 'a'
   win = LabeledTextField(text)
   win.show()
   app.exec_()

