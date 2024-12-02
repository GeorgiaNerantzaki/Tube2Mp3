import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from mainwindow import Ui_MainWindow

if __name__ == "__main__":
    loader = QUiLoader()

    def mainwindow_setup(w):
      w.setWindowTitle("MainWindow Title")

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Ui_MainWindow()
    MainWindow.show()
    app.exec()