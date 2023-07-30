from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, \
    QPushButton
import sys
from backend import ChatBot
import threading

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #instantiate chatbot for the whole conversation
        self.chatbot = ChatBot()

        self.setMinimumSize(700,400)
        self.setWindowTitle("AI Chatbot")
        #instead of a setcentralwidget method (table in prev exercise) we use different multiple widgets
        #in the window now. using the 'self' variable ties widget to mainwindow object
        self.chatspace = QTextEdit(self)
        self.chatspace.setGeometry(10,10, 500,300)
        self.chatspace.setReadOnly(True)

        self.chatbar = QLineEdit(self)
        self.chatbar.setPlaceholderText("enter query")
        self.chatbar.setGeometry(10, 320, 500, 30)
        self.chatbar.returnPressed.connect(self.send_message)

        self.button = QPushButton("send", self)
        self.button.setGeometry(520, 320, 80, 30)
        self.button.clicked.connect(self.send_message)

        #required if there is no central widget
        self.show()

    def send_message(self):
        user_input = self.chatbar.text().strip()
        self.chatspace.append(f"<p style='color:#4169E1'><b>You: {user_input}</p></b>")
        self.chatbar.clear()

        #thread is created so that user question is printed in chatbot first, while
        #waiting for openai response, which may take time
        thread = threading.Thread(target=self.bot_response, args=(user_input,))
        thread.start()

    def bot_response(self, user_input): #user input as arg
        answer = self.chatbot.getresponse(user_input)
        #answer = 'dummy answer'
        self.chatspace.append(f"""<p style='color:#4169E1;
        background-color:#E0FFFF'>AI Bot: {answer}</p>""")


app = QApplication(sys.argv)
mainwindow = ChatWindow()
sys.exit(app.exec())




