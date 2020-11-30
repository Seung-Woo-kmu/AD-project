from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QToolButton, QGridLayout
from GameRanking import GameRanking

class WriteScore(QDialog):
    def __init__(self, num, score):
        super().__init__()
        self.score = score
        self.num = num
        self.initUI()

    def initUI(self):
        self.nameLabel = QLabel("이름: ")
        self.textFont(self.nameLabel, 5)
        self.nameInput = QLineEdit()
        self.nameInput.returnPressed.connect(self.buttonClicked)
        self.textFont(self.nameInput, 5)
        self.inputButton = QToolButton()
        self.inputButton.setText("입력")
        self.textFont(self.inputButton, 5)
        self.goalResult= QLabel("결과: ")
        self.textFont(self.goalResult, 5)
        self.scoreLabel = QLabel("점수: ")
        self.textFont(self.scoreLabel, 5)
        self.getScore = QLineEdit()
        self.getScore.setReadOnly(True)
        self.textFont(self.getScore, 5)
        self.getScore.setText(str(self.score))
        self.resultShow = QLineEdit()
        self.resultShow.setReadOnly(True)
        self.textFont(self.resultShow, 5)
        self.goalPrint()
        self.inputButton.clicked.connect(self.buttonClicked)
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.nameLabel, 0, 0)
        self.mainLayout.addWidget(self.nameInput, 0, 1)
        self.mainLayout.addWidget(self.inputButton, 0, 2)
        self.mainLayout.addWidget(self.scoreLabel, 1, 0)
        self.mainLayout.addWidget(self.getScore, 1, 1)
        self.mainLayout.addWidget(self.goalResult, 2, 0)
        self.mainLayout.addWidget(self.resultShow, 2, 1)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("점수 기록")
        self.setGeometry(700, 300, 700, 100)
        self.show()

    def buttonClicked(self):
        self.RankTextList = ["3 * 3", "4 * 4", "5 * 5", "6 * 6", "7 * 7", "8 * 8", "9 * 9"]
        self.name = self.nameInput.text()
        f = open("gameResult.txt", "r")
        a = eval(f.read())
        a += [{"모드": self.RankTextList[self.num - 3], "이름": self.name, "점수": self.score}]
        f.close()
        f = open("gameResult.txt", "w")
        f.write(str(a))
        f.close()
        win = GameRanking()
        win.showWindow()
        self.close()


    def goalPrint(self):
        self.numList = [3, 4, 5, 6, 7, 8, 9]
        self.scoreGoal = [100, 165, 235, 302, 380, 430, 510]
        for i in range(3, 10):
            if self.num == i:
                if self.score < self.scoreGoal[i - 3]:
                    self.resultShow.setText("목표치인 {}에 약 {}만큼 부족합니다. 조금만 더 노력하세요!". format(self.scoreGoal[i - 3], round(self.scoreGoal[i - 3] - self.score), 2))
                else:
                    self.resultShow.setText("목표치인 {}과 약 {}의 차이로 성공하셨습니다. 축하합니다!". format(self.scoreGoal[i - 3], round(self.score - self.scoreGoal[i - 3]), 2))

    def textFont(self, text, size):
        font = text.font()
        font.setPointSize(font.pointSize() + size)
        text.setFont(font)

    def showWindow(self):
        return super().exec_()