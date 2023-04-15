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

        #链接拖拽事件
        self.setAcceptDrops(True)
        
        #各种信号和槽函数链接///////////////

        # 绑定 QListWidget 的 itemClicked 信号到槽函数
        self.listWidget_1.itemClicked.connect(self.changePage)
        # model 1
        self.button_1.clicked.connect(self.button_1_clicked_ProessImg) # 按键一被按下，处理
        self.button_2.clicked.connect(self.button_2_clicked_SaveImg)#按键二，保存

    #listWidget_1.itemClicked 和stackwigdet切换界面  
    def changePage(self, item: QListWidgetItem):
        # 获取 QListWidgetItem 在 QListWidget 中的索引
        index = self.listWidget_1.row(item)
        # 切换到对应的 QStackedWidget 页面
        self.stackedWidget.setCurrentIndex(index)

    #图片的拖拽
    def dragEnterEvent(self, event):
        # 只接受文件类型的拖放
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        # 获取拖放的文件路径
        file_path_1 = event.mimeData().urls()[0].toLocalFile()

        #判读鼠标所在的wigdet从而判断显示在哪个imglabel上
        widget_imglabel = self.childAt(event.pos())
        #判断widget是否是qlabel类型
        if isinstance(widget_imglabel,QLabel):
            if widget_imglabel.objectName() == "imglabel_1_1":
                 # 加载图片
                pixmap = QPixmap(file_path_1)
                # 缩放图片
                label_size = self.imglabel_1_1.size()
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # 显示图片
                self.imglabel_1_1.setPixmap(scaled_pixmap)
            elif widget_imglabel.objectName() == "imglabel_3_1":
                 # 加载图片
                pixmap = QPixmap(file_path_1)
                # 缩放图片
                label_size = self.imglabel_3_1.size()
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # 显示图片
                self.imglabel_3_1.setPixmap(scaled_pixmap)               

       
    #进度条  加载动画
    def progress_dialog(self):
        # 创建一个进度条对话框
        progress_dialog = QProgressDialog('Processing...', 'Cancel', 0, 100, self.page_1)

        # 显示对话框并设置模态
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.show()

        # 执行一些操作并更新进度条
        for i in range(100):
            if progress_dialog.wasCanceled():
                break
            progress_dialog.setValue(i)
        # 执行某些操作

        # 隐藏对话框
        progress_dialog.hide()


    def button_1_clicked_ProessImg(self):#@save 
        #proessing iamge (send image to wed and create a new proessing dialog)
        # 加载图片
        pixmap = self.imglabel_1_1.pixmap()
        
        #弹出进度条
        #self.progress_dialog()
        # 反转图片 处理图片测试
        transformed_pixmap = pixmap.transformed(QTransform().scale(-1, 1))

        # 显示图片
        self.imglabel_1_2.setPixmap(transformed_pixmap)

    def button_2_clicked_SaveImg(self):
    # 弹出文件选择对话框，让用户选择保存路径和文件名
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG  (*.png)")

        if file_path:
            # 获取图片数据
            image = self.imglabel_1_2.pixmap().toImage()

            # 保存图片
            if image.save(file_path, "PNG"):
                print("Image saved successfully")
            else:
                print("Image not saved successfully")    

    

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()