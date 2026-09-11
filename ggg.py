import sys
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout  
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("wassup")

        self.label = QLabel("blueberries")
        self.button = QPushButton("pls don't")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.clicked)

    def clicked(self):
            self.label.setText("I said pls don't")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()