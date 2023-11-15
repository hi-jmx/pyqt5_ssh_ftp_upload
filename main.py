

### 打包命令：pyinstaller -F -w main.py

from upload_ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QPushButton
import PyQt5.QtGui
import tkinter.messagebox as tmb
import tkinter.filedialog as tkfd
import re as myre
import shutil
from PyQt5.QtCore import  Qt
from upload_file import FTPUpload
from upload_file import SSHUpload
import socket
import time
from loguru import logger


class QMainWin(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(QMainWin, self).__init__()

        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.device_list = []
        self.checkBox_list = []
        self.device_0.setVisible(False)
        self.checkBox_list.append(self.checkBox_0)
        self.device_list.append(self.device_0)
        self.device_1.setVisible(False)
        self.checkBox_list.append(self.checkBox_1)
        self.device_list.append(self.device_1)
        self.device_2.setVisible(False)
        self.checkBox_list.append(self.checkBox_2)
        self.device_list.append(self.device_2)
        self.device_3.setVisible(False)
        self.checkBox_list.append(self.checkBox_3)
        self.device_list.append(self.device_3)
        self.device_4.setVisible(False)
        self.checkBox_list.append(self.checkBox_4)
        self.device_list.append(self.device_4)
        self.device_5.setVisible(False)
        self.checkBox_list.append(self.checkBox_5)
        self.device_list.append(self.device_5)
        self.device_6.setVisible(False)
        self.checkBox_list.append(self.checkBox_6)
        self.device_list.append(self.device_6)
        self.device_7.setVisible(False)
        self.checkBox_list.append(self.checkBox_7)
        self.device_list.append(self.device_7)
        self.device_8.setVisible(False)
        self.checkBox_list.append(self.checkBox_8)
        self.device_list.append(self.device_8)
        self.device_9.setVisible(False)
        self.checkBox_list.append(self.checkBox_9)
        self.device_list.append(self.device_9)

        self.font = PyQt5.QtGui.QFont()
        self.font.setPointSize(10)



        self.pushButton_select.clicked.connect(self.selectFile)
        self.pushButton_upload.clicked.connect(self.uploadAction)
        # 设备类型，E板或Z板或H板,对应”设备“comboBox
        self.device_type_list = []

        self.device_ip_list = []
        self.option_dic_list = []

        self.readConfig()

    def selectFile(self):
        file_name = tkfd.askopenfilename()
        # logger.debug(file_name)
        self.lineEdit.clear()
        file_name_list = file_name.split("/")
        last_split = file_name_list[-1]
        # logger.debug(append)
        if len(last_split) > 0:
            if '.' in last_split:
                tmb.showerror("错误", "错选文件错误")
                return
            self.lineEdit.setText(file_name)
            shutil.copy(file_name, './file/dwcertificate')
    def readConfig(self):
        filename = './config.txt'
        with open(filename) as file_object:
            self.device_index = 0
            self.device_info = []
            for line in file_object:
                if len(line) > 5:
                    line_spit_list = myre.split(r':|;|_', line.strip())
                    logger.debug(line_spit_list) #['BP-905', '192.168.100.200', 'JT']
                    self.device_info.append(line_spit_list)
                    self.device_type_list.append(line_spit_list[0])
                    self.comboBox.addItem(line_spit_list[0], self.device_index)
                    self.device_index = self.device_index + 1
            self.cur_device_list = self.device_info[0]
            self.comboBox.setCurrentIndex(0)
            self.change_index = 0
            self.device_counter = 0
            self.comboBox.currentIndexChanged.connect(self.selectionchange)
            for i in range(1, len(self.cur_device_list), 2):
                self.checkBox_list[self.device_counter].setFont(self.font)
                self.checkBox_list[self.device_counter].setText(self.cur_device_list[i])
                self.checkBox_list[self.device_counter].setChecked(True)
                self.device_list[self.device_counter].setVisible(True)
                self.device_counter = self.device_counter + 1
                self.devic_type_list = self.cur_device_list[2]
                logger.debug(self.devic_type_list)

    def selectionchange(self):
        for i in range (10):
            self.device_list[i].setVisible(False)
        self.change_index = self.comboBox.currentIndex()
        self.device_counter = 0
        self.cur_device_list = self.device_info[self.change_index]
        for i in range(1, len(self.cur_device_list), 2):
            self.checkBox_list[self.device_counter].setFont(self.font)
            self.checkBox_list[self.device_counter].setText(self.cur_device_list[i])
            self.checkBox_list[self.device_counter].setChecked(True)
            self.device_list[self.device_counter].setVisible(True)
            self.device_counter = self.device_counter + 1
            self.devic_type_list = self.cur_device_list[2]
            logger.debug(self.devic_type_list)
    def check_ip_format(self, ip):
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
        if myre.match(pattern, ip):
            return True
        else:
            return False

    def check_ip_range(selt, ip):
        ip_list = ip.split('.')
        for num in ip_list:
            if int(num) < 0 or int(num) > 255:
                return False
        return True

    def is_valid_ip(self, ip):
        if not self.check_ip_format(ip):
            return False
        if not self.check_ip_range(ip):
            return False
        return True
    def uploadAction(self):

        if(len(self.lineEdit.text()) == 0):
            tmb.showerror("错误", "请先选择文件")
            return
        self.option_dic_list=[]
        logger.debug(self.device_counter)
        for i in range(self.device_counter):
            # logger.debug("i:" + str(i))
            if self.checkBox_list[i].isChecked():
                tmp_device={}
                # logger.debug("i:" + str(i)+" " + self.cur_device_list[2*i +1])
                tmp_device['IP']=self.cur_device_list[2*i +1]
                tmp_device['Type'] = self.cur_device_list[2 * i + 2]
                self.option_dic_list.append(tmp_device)
                self.devic_type_list = tmp_device['Type']
        add_device_list = self.textEdit.toPlainText().strip().split(";")
        if(len(self.textEdit.toPlainText().strip()) > 0):
            self.textEdit.toPlainText().strip()
            for i in range(len(add_device_list)):
                tmp_device = {}
                if True == self.is_valid_ip(add_device_list[i]):
                    tmp_device['IP'] = add_device_list[i]
                    tmp_device['Type'] = self.devic_type_list
                    self.option_dic_list.append(tmp_device)
        #     ssh = SShUpload()
        #     ssh.__int__(host='192.168.1.179', port=22,username='root', pwd='root')
        #     res = ssh.connect()
        #     logger.debug(res)
        #     if (1 == res):
        #         ssh.cmd("ls")
        #         ssh.upload('config.txt','/dev/shm/ks77.py')
        #         ssh.download('/dev/shm/ks77.py','kkkk',)
        #         ssh.close()
        #     else:
        #         logger.debug("do nothing")

        # ftp = FTPUpload()
        # ftp.__int__(host='192.168.100.26', port=21, username='test', pwd='test')
        # res = ftp.connect()
        # logger.debug(res)
        # if (1 == res):
        #     ftp.upload('config.txt','./config.txt')
        #     ftp.download('Clash.for.Windows-0.20.31-win.7z','./123',)
        #     ftp.close()
        # else:
        #     logger.debug("do nothing")
        ssh = SSHUpload()
        ftp = FTPUpload()
        errorFormat = '<font color="red" size=4>{}</font>'
        normalFormat = '<font size=4>{}</font>'

        for i in range(len(self.option_dic_list)):
            tmp = self.option_dic_list[i]
            time.sleep(0.2)
            logger.debug(tmp)
            if('Z' == tmp['Type']):
                ssh.__int__(tmp['IP'], port=22,username='root', pwd='root')
                res = ssh.connect()
                if (1 == res):
                    ssh.upload('./file/dwcertificate','/mnt/config/dwcertificate')
                    ssh.close()
                    self.textEdit_log.append(normalFormat.format(tmp['IP'] + "上传成功"))
                    self.textEdit_log.show()
                else:
                    logger.debug("error:do nothing")
                    self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
                    self.textEdit_log.show()
            if ('JT-2K' == tmp['Type']):
                ssh.__int__(tmp['IP'], port=22, username='user', pwd='123456')
                res = ssh.connect()
                if (1 == res):
                    ssh.upload('./file/dwcertificate', '/tmp/dwcertificate')
                    ssh.close()
                    if (1 == self.upd_save(tmp['IP'], 5300)):
                        self.textEdit_log.append(normalFormat.format(tmp['IP'] + "上传成功"))
                    else:
                        self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
                        logger.debug("JT:udp save fail")
                else:
                    logger.debug("error:do nothing")
                    self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
            if ('JT-1K' == tmp['Type']):
                ssh.__int__(tmp['IP'], port=22, username='root', pwd='jrootd')
                res = ssh.connect()
                if (1 == res):
                    ssh.upload('./file/dwcertificate', '/dev/shm/dwcertificate')
                    ssh.close()
                    if (1 == self.upd_save(tmp['IP'], 5300)):
                        self.textEdit_log.append(normalFormat.format(tmp['IP'] + "上传成功"))
                    else:
                        self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
                        logger.debug("JT:udp save fail")
                else:
                    logger.debug("error:do nothing")
                    self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
            if ('E' == tmp['Type']):
                ftp.__int__(tmp['IP'], port=21, username='root', pwd='farwave1.')
                res = ftp.connect()
                if (1 == res):
                    ftp.upload('./file/dwcertificate', '/mnt/disk1/dwcertificate')
                    ftp.close()
                    self.textEdit_log.append(normalFormat.format(tmp['IP'] + "上传成功"))
                else:
                    logger.debug("error:do nothing")
                    self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
            if ('H' == tmp['Type']):
                ssh.__int__(tmp['IP'], port=22, username='root', pwd='root')
                res = ssh.connect()
                if (1 == res):
                    ssh.upload('./file/dwcertificate', '/app/config/dwcertificate')
                    ssh.close()
                    self.textEdit_log.append(normalFormat.format(tmp['IP'] + "上传成功"))
                else:
                    logger.debug("error:do nothing")
                    self.textEdit_log.append(errorFormat.format(tmp['IP'] + "上传失败"))
        self.textEdit_log.append("\n")

    def upd_save(self, ip='192.168.100.200', port=5300):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.bind(('0.0.0.0', 5301))
            server_address = (ip, port)
            data = b'\xBC\x00\x06\x7B\x22\x6D\x6F\x64\x65\x22\x3A\x22\x77\x69\x6E\x22\x2C\x22\x6D\x73\x67\x22\x3A\x7B\x22\x65\x72\x72\x6F\x72\x4D\x73\x67\x22\x3A\x22\x22\x2C\x22\x66\x69\x6C\x65\x53\x74\x61\x74\x65\x22\x3A\x30\x7D\x2C\x22\x6F\x70\x22\x3A\x22\x63\x6F\x6D\x2D\x62\x62\x6F\x78\x2D\x6C\x69\x63\x65\x6E\x73\x65\x2D\x63\x6F\x6D\x70\x2D\x63\x6D\x64\x22\x7D'
            client_socket.sendto(data, server_address)
            client_socket.settimeout(2)
            try:
                # 接收数据
                data, client_addr = client_socket.recvfrom(1024)
                logger.debug('Received data from client:', data[2:].decode())
                return 1
            except socket.timeout:
                logger.debug('Timeout: No data received within 2 seconds')
                return 0
        except Exception as e:
            logger.debug(e)
            return 0


if __name__ == '__main__':
    # logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", level="DEBUG")
    logger.add("./log/WA_{time}.log", enqueue=True, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} : {module}:{line:4} | {message}", level="DEBUG")
    app = QApplication(sys.argv)

    main = QMainWin()

    main.show()
    sys.exit(app.exec_())

