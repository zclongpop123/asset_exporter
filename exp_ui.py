#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Jan 20 17:38:45 2022
#========================================
import sys
import glob
from PySide2 import QtWidgets, QtCore, QtGui
import exp_widgets, exp_app
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class ExportUI(QtWidgets.QMainWindow, exp_widgets.Ui_MainWindow):
    '''
    '''
    def __init__(self, parent=None):
        '''
        '''
        super(ExportUI, self).__init__(parent)
        self.setupUi(self)

        self.listWidget.customContextMenuRequested.connect(self.create_context_menu)
        self.setAcceptDrops(True)



    def dragEnterEvent(self, event):
        '''
        '''
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()



    def dropEvent(self, event):
        '''
        '''
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self.listWidget.addItem(url.toLocalFile())
        else:
            event.ignore()



    @QtCore.Slot()
    def on_let_pattrn_editingFinished(self):
        '''
        '''
        if self.focusWidget() != self.let_pattrn:
            return

        pattrn = self.let_pattrn.text()
        if not pattrn:
            return
        self.listWidget.addItems(glob.glob(pattrn))



    @QtCore.Slot(QtCore.QPoint)
    def create_context_menu(self, point):
        '''
        '''
        menu = QtWidgets.QMenu(self.listWidget)
        menu.addAction('Remove', self.remove_select_items)
        menu.addAction('Remove Duplicates', self.remove_duplicates_items)
        menu.addSeparator()
        menu.addAction('Clear', self.listWidget.clear)
        menu.exec_(QtGui.QCursor.pos())



    def remove_select_items(self):
        '''
        '''
        for item in self.listWidget.selectedItems():
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)



    def remove_duplicates_items(self):
        '''
        '''
        paths = list()
        index = list()
        for i in range(self.listWidget.count()):
            text = self.listWidget.item(i).text()
            if text in paths:
                index.append(i)
            else:
                paths.append(text)
        
        for row in reversed(index):
            self.listWidget.takeItem(row)



    @QtCore.Slot(bool)
    def on_btn_export_clicked(self, args):
        '''
        '''
        result = QtWidgets.QMessageBox.question(self, 'confilm', 'Start to export ? ? ?')
        if result == QtWidgets.QMessageBox.StandardButton.No:
            return

        file_list = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        file_list = [x for i,x in enumerate(file_list) if x not in file_list[:i]]

        exp_app.main(file_list)
        QtWidgets.QMessageBox.about(None, 'Result', 'Export Finished ! !')



def main():
    '''
    '''
    app = QtWidgets.QApplication(sys.argv)
    wnd = ExportUI()
    wnd.show()
    app.exec_()



if __name__ == '__main__':
    main()
