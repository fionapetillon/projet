from PySide2.QtWidgets import *

class Erreur(QWidget) :
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Erreur")
        self.setFixedSize(200, 100)

        self.layout = QVBoxLayout()

        self.label = QLabel("Vérifiez vos informations")

        self.layout.addWidget(self.label)




        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    winE =Erreur()

    app.exec_()

