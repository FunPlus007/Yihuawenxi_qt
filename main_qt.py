#coding:UTF-8
#coding:utf-8
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Yihuawenxinui import Ui_MainWindow
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFileDialog,QPushButton,QProgressDialog,QLabel



    
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
       #super(MyWindow, self).__init__()
        super().__init__()
        self.setupUi(self)

        #������ק�¼�
        self.setAcceptDrops(True)
        
        #�����źźͲۺ�������///////////////

        # �� QListWidget �� itemClicked �źŵ��ۺ���
        self.listWidget_1.itemClicked.connect(self.changePage)
        # model 1
        self.button_1.clicked.connect(self.button_1_clicked_ProessImg) # ����һ�����£�����
        self.button_2.clicked.connect(self.button_2_clicked_SaveImg)#������������

    #listWidget_1.itemClicked ��stackwigdet�л�����  
    def changePage(self, item: QListWidgetItem):
        # ��ȡ QListWidgetItem �� QListWidget �е�����
        index = self.listWidget_1.row(item)
        # �л�����Ӧ�� QStackedWidget ҳ��
        self.stackedWidget.setCurrentIndex(index)

    #ͼƬ����ק
    def dragEnterEvent(self, event):
        # ֻ�����ļ����͵��Ϸ�
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        # ��ȡ�Ϸŵ��ļ�·��
        file_path_1 = event.mimeData().urls()[0].toLocalFile()

        #�ж�������ڵ�wigdet�Ӷ��ж���ʾ���ĸ�imglabel��
        widget_imglabel = self.childAt(event.pos())
        #�ж�widget�Ƿ���qlabel����
        if isinstance(widget_imglabel,QLabel):
            if widget_imglabel.objectName() == "imglabel_1_1":
                 # ����ͼƬ
                pixmap = QPixmap(file_path_1)
                # ����ͼƬ
                label_size = self.imglabel_1_1.size()
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # ��ʾͼƬ
                self.imglabel_1_1.setPixmap(scaled_pixmap)
            elif widget_imglabel.objectName() == "imglabel_3_1":
                 # ����ͼƬ
                pixmap = QPixmap(file_path_1)
                # ����ͼƬ
                label_size = self.imglabel_3_1.size()
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # ��ʾͼƬ
                self.imglabel_3_1.setPixmap(scaled_pixmap)               

       
    #������  ���ض���
    def progress_dialog(self):
        # ����һ���������Ի���
        progress_dialog = QProgressDialog('Processing...', 'Cancel', 0, 100, self.page_1)

        # ��ʾ�Ի�������ģ̬
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.show()

        # ִ��һЩ���������½�����
        for i in range(100):
            if progress_dialog.wasCanceled():
                break
            progress_dialog.setValue(i)
        # ִ��ĳЩ����

        # ���ضԻ���
        progress_dialog.hide()


    def button_1_clicked_ProessImg(self):#@save 
        #proessing iamge (send image to wed and create a new proessing dialog)
        # ����ͼƬ
        pixmap = self.imglabel_1_1.pixmap()
        
        #����������
        #self.progress_dialog()
        # ��תͼƬ ����ͼƬ����
        transformed_pixmap = pixmap.transformed(QTransform().scale(-1, 1))

        # ��ʾͼƬ
        self.imglabel_1_2.setPixmap(transformed_pixmap)

    def button_2_clicked_SaveImg(self):
    # �����ļ�ѡ��Ի������û�ѡ�񱣴�·�����ļ���
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG  (*.png)")

        if file_path:
            # ��ȡͼƬ����
            image = self.imglabel_1_2.pixmap().toImage()

            # ����ͼƬ
            if image.save(file_path, "PNG"):
                print("Image saved successfully")
            else:
                print("Image not saved successfully")    

    

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()