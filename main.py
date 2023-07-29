from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, \
    QPushButton
import sys


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,400)
        self.setWindowTitle("AI Chatbot")
        #instead of a setcentralwidget method (table in prev exercise) we use different multiple widgets
        #in the window now. using the 'self' variable ties widget to mainwindow object
        self.chatspace = QTextEdit(self)
        self.chatspace.setGeometry(10,10, 500,300)
        self.chatspace.setReadOnly(True)

        self.chatbar = QLineEdit(self)
        self.chatbar.setGeometry(10, 320, 500, 30)

        self.button = QPushButton("send", self)
        self.button.setGeometry(520, 320, 80, 30)
        #required if there is no central widget
        self.show()


app = QApplication(sys.argv)
mainwindow = ChatWindow()
sys.exit(app.exec())




