import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from numpy import arange, cos, sin, pi

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMinimumSize(QtCore.QSize(1000, 600))
        Form.setMaximumSize(QtCore.QSize(1000, 600))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(5, 10, 65, 25))
        self.label.setObjectName("label")
        self.range_values = QtWidgets.QTextEdit(Form)
        self.range_values.setGeometry(QtCore.QRect(75, 10, 60, 25))
        self.range_values.setObjectName("range_values")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 130, 25))
        self.label_2.setObjectName("label_2")
        self.k_value = QtWidgets.QTextEdit(Form)
        self.k_value.setGeometry(QtCore.QRect(260, 10, 45, 25))
        self.k_value.setObjectName("k_value")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(155, 40, 105, 25))
        self.label_3.setObjectName("label_3")
        self.m_value = QtWidgets.QTextEdit(Form)
        self.m_value.setGeometry(QtCore.QRect(255, 40, 50, 25))
        self.m_value.setObjectName("m_value")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(5, 40, 85, 25))
        self.label_4.setObjectName("label_4")
        self.dl_value = QtWidgets.QTextEdit(Form)
        self.dl_value.setGeometry(QtCore.QRect(95, 40, 40, 25))
        self.dl_value.setObjectName("dl_value")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(320, 0, 700, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 170, 431, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(5, 70, 141, 25))
        self.label_7.setObjectName("label_7")
        self.v0_value = QtWidgets.QTextEdit(Form)
        self.v0_value.setGeometry(QtCore.QRect(150, 70, 40, 25))
        self.v0_value.setObjectName("v0_value")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(320, 45, 500, 55))
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 90, 1040, 530))
        self.widget.setObjectName("widget")
        self.plot_button = QtWidgets.QPushButton(Form)
        self.plot_button.setGeometry(QtCore.QRect(205, 70, 95, 23))
        self.plot_button.setObjectName("plot_button")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " Диапазон = "))
        self.range_values.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20</p></body></html>"))
        self.label_2.setText(_translate("Form", " Коэф. жесткости k = "))
        self.k_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.981</p></body></html>"))
        self.label_3.setText(_translate("Form", " Масса груза m = "))
        self.m_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_4.setText(_translate("Form", " Смещение dl = "))
        self.dl_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_5.setText(_translate("Form", " Без учета силы тяжести координа Y, центра массы груза, находится на значении 0,\n"
" Сила тяжести воздействует на систему таким образом, что пружина растягивается на величину x0 = mg / k\n"
" В первой части графика (диапазон [-2:0]) тело находится в состоянии покоя"))
        self.label_7.setText(_translate("Form", " Начальная скорость v0 = "))
        self.v0_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_8.setText(_translate("Form", " для вывода системы из положения равновесия неодходимо,\n"
" либо сместить груз из положения равновесия на растояние dl,\n"
" либо, с помощью резкого толчка, придать грузу начальную скорость v0"))
        self.plot_button.setText(_translate("Form", "plot"))


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)


class MainWidget(QWidget, Ui_Form):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.init_widget()
        self.plot_button.clicked.connect(self.event_button)
        self.g = 9.81
        self.start_t ,self.stop_t = 0 , float(self.range_values.toPlainText())
        self.k = float(self.k_value.toPlainText())
        self.m = float(self.m_value.toPlainText())
        self.dl = float(self.dl_value.toPlainText())
        self.v0 = float(self.v0_value.toPlainText())
        self.x0 = self.m * self.g / self.k
        self.xm = self.dl + self.v0 * (self.m * self.k)**0.5
        self.w = (self.k / self.m)**0.5
        self.fi0 = 0
        if self.v0:
            self.fi0 = -pi / 2
        self.plot_widget()
        self.show()
        
    def init_widget(self):
        self.matplotlibwidget = MatplotlibWidget()
        self.layoutvertical = QVBoxLayout(self.widget)
        self.layoutvertical.addWidget(self.matplotlibwidget)
        
    def plot_widget(self):
        self.matplotlibwidget.axis.clear()
        self.t = arange(self.start_t ,self.stop_t, 0.01)
        self.x = self.xm * cos(self.w*self.t + self.fi0) - self.x0
        self.matplotlibwidget.axis.plot([self.start_t - 2, self.start_t], [-self.x0, -self.x0], color='#8b00ff')
        self.matplotlibwidget.axis.plot([self.start_t, self.start_t], [-self.x0, self.x[0]], color='#8b00ff')
        self.matplotlibwidget.axis.plot([self.start_t, self.stop_t], [-self.x0, -self.x0], color='#666666')
        self.matplotlibwidget.axis.plot(self.t, self.x, color='#8b00ff')
        self.matplotlibwidget.axis.grid(True)
        self.matplotlibwidget.canvas.draw()
        
    def event_button(self):
        self.start_t ,self.stop_t = 0 , float(self.range_values.toPlainText())
        self.k = float(self.k_value.toPlainText())
        self.m = float(self.m_value.toPlainText())
        self.dl = float(self.dl_value.toPlainText())
        self.v0 = float(self.v0_value.toPlainText())
        self.x0 = self.m * self.g / self.k
        self.xm = self.dl + self.v0 * (self.m * self.k)**0.5
        self.w = self.k / self.m
        self.fi0 = 0
        if self.v0:
            self.fi0 = -pi/2 
        self.plot_widget()


def main():
    app = QApplication(sys.argv)
    w = MainWidget()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

