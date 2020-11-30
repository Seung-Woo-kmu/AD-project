from PyQt5.QtWidgets import QGridLayout, QLabel, QSizePolicy, QHBoxLayout, QLineEdit, QToolButton, QDialog
from WriteScore import WriteScore
import random
import math
import time

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)


    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class GamePlay(QDialog):
    def __init__(self, num):
        super().__init__()
        self.gridNum = num
        self.timeList = []
        self.scoreList = []
        self.initUI(self.gridNum)

    def initUI(self, num):
        self.num = num
        self.gridlist = [(i, j) for i in range(self.num) for j in range(self.num)]
        self.button = [x for x in range(1, self.num * self.num + 1)]
        random.shuffle(self.gridlist)
        self.buttonText = 0
        self.buttonLayout = QGridLayout()
        for i in range(0, self.num * self.num):
            self.button[i] = Button(str(i + 1), self.buttonClicked)
            self.textFont(self.button[i], 20)
            self.button[i].setEnabled(False)
            self.button[i].setStyleSheet('color:yellow; background:black')
            self.buttonLayout.addWidget(self.button[i], *self.gridlist[i])
        self.button[0].setEnabled(True)
        self.mainLayout = QGridLayout()
        self.scoreLayout = QHBoxLayout()
        self.scoreLabel = QLabel("점수: ")
        self.textFont(self.scoreLabel, 10)
        self.score = QLineEdit()
        self.score.setReadOnly(True)
        self.textFont(self.score, 10)
        self.score.setText("0")
        self.scoreLayout.addWidget(self.scoreLabel)
        self.scoreLayout.addWidget(self.score)
        self.mainLayout.addLayout(self.scoreLayout, 0, 0)
        self.mainLayout.addLayout(self.buttonLayout, 1, 0)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("숫자 순서 맞추기 게임")
        self.setGeometry(700, 300, 500, 500)
        self.show()
        self.firstTime = time.time()

    def buttonClicked(self):
        self.time = time.time()
        self.timeList.append(self.time)
        if self.buttonText == 0:
            self.firstTimeDiffer = time.time() - self.firstTime
            self.scoreList.append(round(15 / math.exp(1) ** self.firstTimeDiffer, 2))
            self.score.setText(str(self.scoreList[0]))
        else:
            self.timeDiffer = time.time() - self.timeList[self.buttonText - 1]
            self.scoreList.append(round(15 / math.exp(1) ** self.timeDiffer, 2))
            self.scoreSum = round(sum(self.scoreList), 2)
            self.score.setText(str(round(sum(self.scoreList), 2)))
        self.buttonText += 1
        button = self.sender()
        if self.buttonText > self.num * self.num - 1:
            self.button[self.buttonText-1].setEnabled(False)
            button.setStyleSheet('color:red; background:red')
        else:
            self.button[self.buttonText].setEnabled(True)
            self.button[self.buttonText-1].setEnabled(False)
            button.setStyleSheet('color:red; background:red')
        if self.buttonText == self.num * self.num:
            win = WriteScore(self.num, self.scoreSum)
            win.showWindow()
            self.close()

    def textFont(self, text, size):
        font = text.font()
        font.setPointSize(font.pointSize() + size)
        text.setFont(font)

    def showWindow(self):
        return super().exec_()