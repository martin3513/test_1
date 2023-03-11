import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon



class Application(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AUTO 배부~")
        self.setGeometry(1200, 510, 400, 350)
        self.setWindowIcon(QIcon('./image/icon.png'))
        
        self.create_widgets()
        self.doc_name = ""
        self.doc_name_count = 0

    def create_widgets(self):
        self.log_text = QTextEdit(self)
        self.log_text.setGeometry(10, 0, 380, 300)

        self.ok = QPushButton(self)
        self.ok.setText("시 작")
        self.ok.setGeometry(10, 310, 150, 30)
  #    self.ok.setFont(self.ok.font().pointSize() + 5)
        self.ok.setStyleSheet("background-color: blue; color: white;")
        self.ok.clicked.connect(self.show_message)

        self.quit = QPushButton(self)
        self.quit.setText("종 료")
        self.quit.setGeometry(170, 310, 150, 30)
    #    self.quit.setFont(self.quit.font().pointSize() + 2)
    #    self.quit.setStyleSheet("background-color: red; color: white;")
        self.quit.clicked.connect(self.close)

        self.chkLoop = QCheckBox(self)
        self.chkLoop.setText("반복실행")
        self.chkLoop.setGeometry(330, 315, 100, 20)
        self.chkLoop.setChecked(True)
        self.chkLoop.stateChanged.connect(self.print_value)

        message = "문서 배부를 위해 만들어진 자동 배부 프로그램입니다.\n"
        self.log_text.append(message)

    def print_value(self, state):
        print(state)
        self.looping_main = (state == 2)

    def show_message(self):
        self.looping_main = True
        while self.looping_main:
            message = "진행중...\n"
            self.log_text.append(message)
            self.log_text.verticalScrollBar().setValue(self.log_text.verticalScrollBar().maximum())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.setWindowIcon(QIcon('./image/icon.png'))
    
    window.show()
    sys.exit(app.exec_())
