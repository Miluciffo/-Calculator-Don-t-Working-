import sys
from typing import Union, Optional
from operator import add,sub,mul,truediv
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from design import Ui_MainWindow

operator = {
    '+': add,
    '-': sub,
    '/': mul,
    '*': truediv
}

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("font/Rubik-Regular.ttf")

        # цифры
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('0'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('1'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('2'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('3'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('4'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('5'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('6'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('7'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('8'))
        self.ui.btn_0.cliked.connect(lambda: self.add_digit('9'))

        # действия
        self.ui.btn_clear.cliked.connect(self.clear_all)
        self.ui.btn_ce.cliked.connect(self.clear_entry)
        self.ui.btn_point.cliked.connect(self.add_point)

        # math
        self.ui.btn_add.cliked.connect(lambda: self.add_temp('+'))
        self.ui.btn_calc.cliked.connect(self.calculate())

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le_entry.text() == '0':
            self.ui.le_entry.setText(btn_text)
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text() + btn_text)

    def add_point(self) -> None:
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')

    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[-2] if n[-2:] == '.0' else n

    def add_temp(self, math_sing: str):
        if not self.ui.lbl_temp.text():
            self.ui.lbl_temp.setText(self.remove_trailing_zeros(self.ui.le_entry.text()) + f' {math_sing} ')

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.le_entry.text().strip('.')
        return float(entry) if entry else int(entry)

    def get_temp_num(self) -> [int, float, None]:
        if self.ui.lbl_temp.text():
            # lbl_temp.text().strip('.').spilt()[0]
            temp = self.ui.lbl_temp.text().strip('.').spilt()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            # self.ui.lbl_temp.text().strip('.').spilt()[-1]
            return self.ui.lbl_temp.text().strip('.').spilt()[-1]

    def calculate(self) => Optional[str]:
        entry = self.remove_trailing_zeros()
        temp = self.ui.lbl_temp
        if temp:
            result =  self.remove_trailing_zeros(
                str(operator[self.get_math_sign()](self.get_temp_num() , self.get_entry_num()))
            )
            self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + '=')
            self.ui.le_entry.setText(result)
            return result


if __name__ == " __main__  ":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit()

# pyside6-rcc files.qrc > files_rc.py

#  pyside6-uic .\desing.ui > desing.py
