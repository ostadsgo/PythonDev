import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Calculator:
    """ methods required in claculator app."""

    def __init__(self, equation_box):
        self.equation_box = equation_box

    def calculate(self):
        """ calcualte the result of the equation """

        # check if there is equation in the equation_box
        if len(self.equation_box.text()) > 0:
            eq_result = eval(self.equation_box.text())
            self.equation_box.setText(str(eq_result))

    def clear_one(self):
        """ Remove one charcter of equation_box from the right """
        if len(self.equation_box.text()) > 0:
            self.equation_box.setText(self.equation_box.text()[:-1])

    def clear_all(self):
        """ Clear all text inside equation_box """
        self.equation_box.clear()


class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("calculator.ui", self)
        self.show()
        # set focus to equation_box
        self.equation_box.setFocus()
        self.calculator = Calculator(self.equation_box)

        # call buttonClicked event insert each button text to equation button
        for child in self.findChildren(QtWidgets.QPushButton):
            child.clicked.connect(self.buttonClicked)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.calculator.calculate()

    def buttonClicked(self):
        sender = self.sender()

        # make the = symbol not inserted to the equation_box after calualte the equation.
        if sender.text() != "=":
            self.equation_box.setText(self.equation_box.text() + sender.text())


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = Ui()
    calculater = Calculator(window.equation_box)

    window.equal_button.clicked.connect(calculater.calculate)
    window.clear_one.clicked.connect(calculater.clear_one)
    window.clear_all.clicked.connect(calculater.clear_all)

    app.exec_()


if __name__ == "__main__":
    main()