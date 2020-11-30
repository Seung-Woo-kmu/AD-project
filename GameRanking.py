from PyQt5.QtWidgets import QHBoxLayout, QDialog, QTextEdit


class GameRanking(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        f = open("gameResult.txt", "r")
        grade = eval(f.read())
        rank = QTextEdit()
        rank.setReadOnly(True)
        f.close()
        grade = sorted(grade, key=lambda x: x["모드"])
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        listNum = [list3, list4, list5, list6, list7, list8, list9]
        for i in range(3, 10):
            for j in grade:
                if j["모드"] == '{} * {}'.format(i, i):
                    listNum[i - 3].append(j)
        for i in range(1, 8):
            grade = sorted(listNum[i - 1], key=lambda x: x["점수"])
            grade.reverse()
            ranking = 0
            for i in grade:
                ranking += 1
                mode = "모드" + " = " + str(i["모드"]) + "\t"
                name = "이름" + " = " + str(i["이름"])
                score = str(ranking) + "등. " + "점수" + " = " + str(i["점수"]) + "\t"
                rankingPrint = mode + score + name
                rank.insertPlainText(rankingPrint)
                rank.append("")
            rank.append("")
        font = rank.font()
        font.setPointSize(font.pointSize() + 10)
        rank.setFont(font)
        rankLayout = QHBoxLayout()
        rankLayout.addWidget(rank)
        self.setLayout(rankLayout)
        self.setWindowTitle("게임 결과")
        self.setGeometry(590, 310, 800, 500)
        self.show()

    def showWindow(self):
        return super().exec_()