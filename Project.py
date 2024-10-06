from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
window.resize(400, 300)
window.setWindowTitle("Calculator")
Name = QLabel("Simple Calculator")
Number = QLabel("Number №1:")
Numberr = QLabel("Number №2:")
Respond = QPushButton("Respod")
Write = QLineEdit()
Writee = QLineEdit()

Line = QVBoxLayout()
Line.addWidget(Name)
Line.addWidget(Number)
Line.addWidget(Write)
Line.addWidget(Numberr)
Line.addWidget(Writee)
Line.addWidget(Respond)
window.setLayout(Line)

def multiplication():
    one = int(Number.text())
    two = int(Numberr.text())
    riv = one * two
    
window.show()
app.exec_()