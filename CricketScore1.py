# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CricketScore.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    import sqlite3
    Mycrkt=sqlite3.connect("CricketGame.db")
    Mycur=Mycrkt.cursor()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(844, 569)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(69, 207, 207);\n"
"background-color: rgb(81, 179, 208);\n"
"background-color: rgb(51, 211, 171);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 160, 466, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lw1_2 = QtWidgets.QListWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw1_2.setFont(font)
        self.lw1_2.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);")
        self.lw1_2.setObjectName("lw1_2")
        self.horizontalLayout_5.addWidget(self.lw1_2)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lw2_2 = QtWidgets.QListWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw2_2.setFont(font)
        self.lw2_2.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.lw2_2.setObjectName("lw2_2")
        self.horizontalLayout_5.addWidget(self.lw2_2)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(220, 120, 461, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(166, 55, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(166, 55, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 70, 511, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"color: rgb(85, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(340, 500, 211, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("font: 63 10pt \"Lucida Fax\";\n"
"background-color: rgb(201, 209, 41);\n"
"color: rgb(4, 32, 134);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.scorelabel_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scorelabel_2.setFont(font)
        self.scorelabel_2.setText("")
        self.scorelabel_2.setObjectName("scorelabel_2")
        self.horizontalLayout_8.addWidget(self.scorelabel_2)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(300, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(85, 85, 0);\n"
"color: rgb(85, 0, 127);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(620, 270, 201, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Players/All Rounder.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 310, 261, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Players/l2.png"))
        self.label.setObjectName("label")
        self.label_2.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.layoutWidget_3.raise_()
        self.label_9.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.teamscombobox()
        self.pushButton_2.clicked.connect(self.cal_Score)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Players"))
        self.label_7.setText(_translate("Dialog", "Points"))
        self.label_8.setText(_translate("Dialog", "Select Team"))
        self.label_3.setText(_translate("Dialog", "Select Match"))
        self.comboBox.setItemText(0, _translate("Dialog", "Match 1"))
        self.comboBox.setItemText(1, _translate("Dialog", "Match2"))
        self.pushButton_2.setText(_translate("Dialog", "Calculate Score"))
        self.label_9.setText(_translate("Dialog", "Final Team Score"))

    def teamscombobox(self):
        sql="SELECT Name FROM teams;"
        try:
            Ui_Dialog.Mycur.execute(sql)
            result=Ui_Dialog.Mycur.fetchall()
            for i in result:
                self.comboBox_2.addItem(i[0])
        except:
            pass
        
    def matchcombobox(self):
        match_nm=self.comboBox.currentText()
        if match_nm=="Match 1":
            match_nm="match"
        return match_nm

    def cal_Score(self):
        team_nm=self.comboBox_2.currentText()
        self.lw1_2.clear()
        self.lw2_2.clear()
        sql="SELECT Players FROM teams WHERE Name='"+team_nm+"';"
        try:
            Ui_Dialog.Mycur.execute(sql)
            result=Ui_Dialog.Mycur.fetchone()
            Players=result[0].split(",")
            teamScore=0
            for player in Players:
                tot_pts=0
                tot_pts=self.batScore(player)+self.bwlScore(player)+self.fieldScore(player)
                teamScore+=tot_pts
                self.lw1_2.addItem(player)
                self.lw2_2.addItem(str(tot_pts))
            self.scorelabel_2.setText(str(teamScore))
        except:
            pass

    def batScore(self,player):
        match=self.matchcombobox()
        bat_score=0
        sql="SELECT Scored,Faced,Fours,Sixes FROM '"+match+"'WHERE Player='"+player+"';"
        try:
            Ui_Dialog.Mycur.execute(sql)
            batting_stats=Ui_Dialog.Mycur.fetchone()
            scored=int(batting_stats[0])
            faced=int(batting_stats[1])
            fours=int(batting_stats[2])
            sixes=int(batting_stats[3])
            if faced:
                strike_rate=(scored/faced)*100
            else:
                strike_rate=0
            if scored>=100: 
                bat_score+=10            
            if scored>=50:
                bat_score+=5
            if strike_rate>=80 and strike_rate<=100:
                bat_score+=2
            if strike_rate>100:
                bat_score+=4
            bat_score+=fours
            bat_score+=(sixes*2)
            return bat_score
        except:
            pass

    def bwlScore(self,player):
        match=self.matchcombobox()
        bwl_score=0
        sql="SELECT Bowled,Maiden,Given,Wkts FROM '"+match+"'WHERE Player='"+player+"';"
        try:
            Ui_Dialog.Mycur.execute(sql)
            bowling_stats=Ui_Dialog.Mycur.fetchone()
            bowled=int(bowling_stats[0])
            maiden=int(bowling_stats[1])
            given=int(bowling_stats[2])
            wkts=int(bowling_stats[3])
            if bowled:
                eco_rate=given/(bowled//6)
            else:
                eco_rate=0
            if eco_rate>=3.5 and eco_rate<=4.5:            
                bwl_score+=4
            if eco_rate>=2 and eco_rate<3.5:
                bwl_score+=7
            if eco_rate>0 and eco_rate<2:
                bwl_score+=10
            if wkts>=5:
                bwl_score+=10
            if wkts>=3 and wkts<=4:
                bwl_score+=5
            bwl_score+=(wkts*10)
            return bwl_score
        except:
            pass

    def fieldScore(self,player):
        match=self.matchcombobox()
        field_score=0
        sql="SELECT Catches,Stumping,RO FROM '"+match+"'WHERE Player='"+player+"';"
        try:
            Ui_Dialog.Mycur.execute(sql)
            fielding_stats=Ui_Dialog.Mycur.fetchone()
            catches=int(fielding_stats[0])
            stumping=int(fielding_stats[1])
            ro=int(fielding_stats[2])
            field_score=field_score+(catches*10)
            field_score=field_score+(stumping*10)
            field_score=field_score+(ro*10)
            return field_score
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())