from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
def button_click():
    print("button")
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("My GUI")
button = QPushButton("Click me",window)

window.setGeometry(500,500,500,500)

#button.setGeometry(14,15,16,16)

#button.clicked.connect(button_click)

#window.setCentralWidget(button)
window.showFullScreen()
sys.exit(app.exec_())