from PySide import QtCore, QtGui
import sys
from calc import Ui_Form

#Create application
app = QtGui.QApplication(sys.argv)

#Create form and init UI
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#Hook logic
def bp():
    ui.lineEdit.setText("Hello_world!")

ui.pushButton_10.clicked.connect(bp)


   
# Run main loop    
sys.exit(app.exec_())
