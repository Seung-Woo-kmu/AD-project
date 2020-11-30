from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLabel, QComboBox, QTextEdit, QToolButton
from GamePlay import GamePlay
from GameRanking import GameRanking
import sys


class MainGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initNum()

    def initNum(self):
        self.startLabel = QLabel("게임 시작: ")
        self.textFont(self.startLabel, 10)
        self.numberBox = QComboBox()
        self.textFont(self.numberBox, 5)
        self.mainLayout = QGridLayout()
        self.info = QLabel()
        self.infoprint = QTextEdit()
        self.infoprint.setReadOnly(True)
        self.info.setText("게임 설명서: ")
        self.textFont(self.info, 10)
        self.infoprint.setText("n * n 으로 구성된 숫자가 화면에 무작위로 배열됩니다."
                               "\n게임은 주어진 숫자들을 순서대로 클릭하여 모두 눌러주면 끝나는 방식으로 진행됩니다."
                               "\n숫자들을 누르기 전에는 버튼이 검정색이며 누르면 빨간색으로 변합니다."
                               "\n숫자들을 빨리 누를수록 점수를 더 많이 얻습니다"
                               "\n게임을 시작해서 목표 점수를 넘어 보세요!"
                               "\n게임이 끝난 후 본인이 몇 등인지도 확인해보세요!")
        self.textFont(self.infoprint, 5)
        for i in range(3, 10):
            self.numberBox.addItem(("{} * {} 으로 구성됨 (1 ~ {})". format(i, i, i ** 2)))
        self.numberBox.activated.connect(self.Activated)
        self.goalLabel = QLabel("게임 목표: ")
        self.goalPrint = QTextEdit()
        self.goalPrint.setReadOnly(True)
        self.goalPrint.setText("3 * 3 일 때의 목표 점수: 100"
                                 "\n4 * 4 일 때의 목표 점수: 165"
                                 "\n5 * 5 일 때의 목표 점수: 235"
                                 "\n6 * 6 일 때의 목표 점수: 302"
                                 "\n7 * 7 일 때의 목표 점수: 380"
                                 "\n8 * 8 일 때의 목표 점수: 430"
                                 "\n9 * 9 일 때의 목표 점수: 510")
        self.textFont(self.goalLabel, 10)
        self.textFont(self.goalPrint, 6)
        self.result = QToolButton()
        self.result.clicked.connect(self.buttonClicked)
        self.result.setText("게임 등수")
        self.textFont(self.result, 10)
        self.mainLayout.addWidget(self.startLabel, 0, 0)
        self.mainLayout.addWidget(self.numberBox, 0, 1)
        self.mainLayout.addWidget(self.info, 1, 0)
        self.mainLayout.addWidget(self.infoprint, 1, 1)
        self.mainLayout.addWidget(self.goalLabel, 2, 0)
        self.mainLayout.addWidget(self.goalPrint, 2, 1)
        self.mainLayout.addWidget(self.result, 3, 0)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("숫자 순서 맞추기 게임")
        self.setGeometry(550, 280, 860, 570)
        self.show()


    def Activated(self):
        self.getGridNum = self.numberBox.currentText()
        self.gridNum = int(self.getGridNum[0])
        SubWin = GamePlay(self.gridNum)
        SubWin.showWindow()

    def buttonClicked(self):
        rankWin = GameRanking()
        rankWin.showWindow()

    def textFont(self, text, size):
        font = text.font()
        font.setPointSize(font.pointSize() + size)
        text.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MainGame()
    sys.exit(app.exec_())