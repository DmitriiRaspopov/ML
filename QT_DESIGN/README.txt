1) Нужно зайти в папку с файлом графического интерфейса.
2) Затем в терминале ввести следующую команду, для перевода нашего файла интерфейса Qt в .py
pyside-uic calculator_test.ui  -x -o calc.py

3) Затем заходим в созданный файл и копируем те строчки, которые расположены в его вконце. И вырезаем их и сохраням файл.

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
    4)Создаем новый файл с названием main.py куда помещаем наши строки и немножко редактируем их!

from PySide import QtCore, QtGui
import sys
from calc import Ui_Form


