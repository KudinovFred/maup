from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QHBoxLayout, QVBoxLayout,
                             QGridLayout)

def my_f():
    print("smth")

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("my title")

        btn = QPushButton("Qjlkjkljklit", self)
        btn.clicked.connect(my_f)
        btn.resize(btn.sizeHint())

        #absolute position
        btn.move(300,0)

        btn2 = QPushButton("Close", self)
        btn2.clicked.connect(self.close)
        btn2.resize(btn.sizeHint())

        self.show()


class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        lbl1 = QLabel("Examples", self)
        lbl2 = QLabel("For Us", self)
        lbl3 = QLabel("From Book", self)

        lbl1.move(0, 0)
        lbl2.move(100,0)
        lbl3.move(200, 0)


        btn_ok = QPushButton("OK", self)
        btn_cancel = QPushButton("Cancel", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 500, 300)

        self.show()
        btn_cancel.hide()


class Window_Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ["cls", "bck", "", "close",
                 "7", "8","9", "/"
                 "4", "5", "6", "*"]
        position = [(i,j) for i in range(0,5), for j in range(0,4)]

        for (position, name) in zip(position, names):
            if name =="":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300,150)

        self.show()





if __name__ == "__main__":
    app = QApplication([])
    ex = Window_Calc()
    app.exec_()