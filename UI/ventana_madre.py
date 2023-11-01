# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_madre.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_iniciar = QtWidgets.QPushButton(self.widget)
        self.pushButton_iniciar.setObjectName("pushButton_iniciar")
        self.horizontalLayout.addWidget(self.pushButton_iniciar)
        self.pushButton_detener = QtWidgets.QPushButton(self.widget)
        self.pushButton_detener.setEnabled(False)
        self.pushButton_detener.setObjectName("pushButton_detener")
        self.horizontalLayout.addWidget(self.pushButton_detener)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_7d = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7d.setChecked(True)
        self.radioButton_7d.setObjectName("radioButton_7d")
        self.GrupoBoton_mostrar = QtWidgets.QButtonGroup(MainWindow)
        self.GrupoBoton_mostrar.setObjectName("GrupoBoton_mostrar")
        self.GrupoBoton_mostrar.addButton(self.radioButton_7d)
        self.horizontalLayout_2.addWidget(self.radioButton_7d)
        self.radioButton_24h = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_24h.setObjectName("radioButton_24h")
        self.GrupoBoton_mostrar.addButton(self.radioButton_24h)
        self.horizontalLayout_2.addWidget(self.radioButton_24h)
        self.radioButton_1h = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_1h.setObjectName("radioButton_1h")
        self.GrupoBoton_mostrar.addButton(self.radioButton_1h)
        self.horizontalLayout_2.addWidget(self.radioButton_1h)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.widget)
        self.plt_container = QtWidgets.QFrame(self.frame)
        self.plt_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plt_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plt_container.setObjectName("plt_container")
        self.verticalLayout_2.addWidget(self.plt_container)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_info = QtWidgets.QLabel(self.widget_2)
        self.label_info.setObjectName("label_info")
        self.horizontalLayout_3.addWidget(self.label_info)
        self.label_recomendacion = QtWidgets.QLabel(self.widget_2)
        self.label_recomendacion.setObjectName("label_recomendacion")
        self.horizontalLayout_3.addWidget(self.label_recomendacion)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 11)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Trainding - BootCamp Challenge"))
        self.pushButton_iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.pushButton_detener.setText(_translate("MainWindow", "Detener"))
        self.groupBox.setTitle(_translate("MainWindow", "Mostrar:"))
        self.radioButton_7d.setText(_translate("MainWindow", "7 días"))
        self.radioButton_24h.setText(_translate("MainWindow", "24 hrs"))
        self.radioButton_1h.setText(_translate("MainWindow", "1 hr"))
        self.label_info.setText(_translate("MainWindow", "Info"))
        self.label_recomendacion.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
