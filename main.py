import json
import os
import sys
import time
from threading import Thread
import apprcc_rc
import cv2
import numpy as np
import torch
import torch.backends.cudnn as cudnn
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from threading import Thread
from dialog.rtsp_win import Window
from main_win.win import Ui_mainWindow
from models.experimental import attempt_load
from utils.CustomMessageBox import MessageBox
from utils.capnums import Camera
from utils.datasets import LoadImages, LoadWebcam
from utils.general import check_img_size, non_max_suppression, scale_coords
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device

torch.cuda.empty_cache()


def showimage(img1, img2):
    cv2.destroyAllWindows()
    both = np.hstack((img1, img2))
    cv2.imshow('img', both)
    cv2.waitKey(0)


class DetThread(QThread):
    send_img = Signal(np.ndarray)
    send_raw = Signal(np.ndarray)
    send_statistic = Signal(dict)

    send_msg = Signal(str)
    send_percent = Signal(int)
    send_fps = Signal(str)

    def __init__(self):
        super(DetThread, self).__init__()
        self.zed = None
        self.depth = None
        self.weights = './pt/best.pt'
        self.current_weight = './pt/best.pt'
        self.source = 'F:/abc.mp4'
        self.conf_thres = 0.9
        self.iou_thres = 0.5
        self.jump_out = False
        self.is_continue = True
        self.percent_length = 1000
        self.rate_check = False
        self.rate = 100

    @torch.no_grad()
    def run(self, imgsz=640, max_det=1000, device='cpu', view_img=True, save_txt=False, save_conf=False,
            save_crop=False, nosave=False, classes=None, agnostic_nms=True, augment=False, visualize=False, update=True,
            project='runs/detect', name='exp', exist_ok=False, line_thickness=1, hide_labels=True, hide_conf=True,
            half=False, ):
        """
        """

        global im0
        try:

            device = select_device(device)

            model = attempt_load(self.weights, map_location=device)
            num_params = 0
            for param in model.parameters():
                num_params += param.numel()
            stride = int(model.stride.max())
            imgsz = check_img_size(imgsz, s=stride)
            names = model.module.names if hasattr(model, 'module') else model.names
            if half:
                model.half()

            if self.source.isnumeric() or self.source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://')):

                cudnn.benchmark = True
                dataset = LoadWebcam(self.source, img_size=imgsz, stride=stride)
            else:
                dataset = LoadImages(self.source, img_size=imgsz, stride=stride)

            count = 0
            countu = 1

            jump_count = 0
            start_time = time.time()
            dataset = iter(dataset)
            while True:

                if self.jump_out:
                    self.send_percent.emit(0)
                    self.send_msg.emit('停止')

                    break

                if self.current_weight != self.weights:

                    model = attempt_load(self.weights, map_location=device)
                    num_params = 0
                    for param in model.parameters():
                        num_params += param.numel()
                    stride = int(model.stride.max())
                    imgsz = check_img_size(imgsz, s=stride)
                    names = model.module.names if hasattr(model, 'module') else model.names
                    if half:
                        model.half()

                    self.current_weight = self.weights

                if self.is_continue:
                    self.zed, self.depth, path, img, im0s = next(dataset)
                    count += 1
                    if count % 30 == 0 and count >= 30:
                        fps = int(30 / (time.time() - start_time))
                        self.send_fps.emit('fps：' + str(fps))
                        start_time = time.time()

                    statistic_dic = {name: 0 for name in names}
                    img = torch.from_numpy(img).to(device)
                    img = img.half() if half else img.float()
                    img /= 255.0
                    if img.ndimension() == 3:
                        img = img.unsqueeze(0)

                    pred = model(img, augment=False)[0]

                    pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, classes, agnostic_nms,
                                               max_det=max_det)

                    for i, det in enumerate(pred):
                        im0 = im0s.copy()
                        if len(det):
                            countu += 1

                            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                            x = 0
                            y = 0
                            for *xyxy, conf, cls in reversed(det):
                                c = int(cls)
                                label = None if hide_labels else (names[c] if hide_conf else '{names[c]} {conf:.2f}')
                                plot_one_box(xyxy, im0, label=label, color=colors(c, True),
                                             line_thickness=line_thickness)
                                q = 0
                                if y != 0 and y - (xyxy[1] + xyxy[3]) / 2 <= 30 and y - (xyxy[1] + xyxy[3]) / 2 >= -30:
                                    if (xyxy[0] + xyxy[2]) / 2 > 1280 and x < 1280:
                                        z = int((x + (xyxy[0] + xyxy[2]) / 2 - 1280) / 2)
                                        z2 = int((y + (xyxy[1] + xyxy[3]) / 2) / 2)
                                        q = 1
                                        x_l = int(xyxy[2] - xyxy[0])
                                        y_l = int(xyxy[3] - xyxy[1])
                                    elif x > 1280 and (xyxy[0] + xyxy[2]) / 2 < 1280:
                                        z = int((x - 1280 + (xyxy[0] + xyxy[2]) / 2) / 2)
                                        z2 = int((y + (xyxy[1] + xyxy[3]) / 2) / 2)
                                        q = 1
                                        x_l = int(xyxy[2] - xyxy[0])
                                        y_l = int(xyxy[3] - xyxy[1])
                                x = int((xyxy[0] + xyxy[2]) / 2)
                                y = int((xyxy[1] + xyxy[3]) / 2)
                                pp = 0
                                ll = 0
                                if q == 1 and 400 <= z <= 880 and 200 <= z2 <= 720:
                                    for k in range(z - 1, z + 2):
                                        for j in range(z2 - 1, z2 + 2):
                                            if self.depth.get_value(k, j)[1] is not None and self.depth.get_value(k, j)[
                                                1] >= 300 and 1500 >= self.depth.get_value(k, j)[1] == \
                                                    self.depth.get_value(k, j)[1]:
                                                pp += self.depth.get_value(k, j)[1]
                                                ll += 1
                                    if ll >= 5:
                                        pp /= ll
                                        k = pp * 6 / (2.12 * 1468.6)
                                        x_ll = x_l
                                        y_ll = y_l
                                        x_l *= k
                                        y_l *= k
                                        z_l = x_l / y_l
                                        w = 2.10 * x_l + 4.86 * y_l - 668.11+16.61
                                        if 100 <= w <= 1000 and 50 <= y_l <= 150 and 100 <= x_l <= 300 and 1.5 <= z_l <= 2.5:
                                            print('长度', x_l, '宽度', y_l, '重量', w, '深度', pp * 1.3, 'x坐标', z,
                                                  'y坐标', z2, '原长度', x_ll, '原宽度', y_ll)
                                            myWin.show_statistic(['长度', str(x_l), '宽度', str(y_l), '重量', str(w)])
                                            line = (x_l, y_l, w)
                                            save_path = str(countu) + ".jpg"
                                            cv2.imwrite(save_path, im0)
                                            thread = Thread(target=showimage, args=(im0s, im0s))
                                            thread.start()
                                            with open(save_path + '.txt', 'a') as f:
                                                f.write(('%g ' * len(line)).rstrip() % line + '\n')
                                countu += 1
                    if self.rate_check:
                        time.sleep(1 / self.rate)
                    self.send_img.emit(im0)
                    self.send_raw.emit(im0s if isinstance(im0s, np.ndarray) else im0s[0])
                    self.send_statistic.emit(statistic_dic)
        except Exception as e:
            self.send_msg.emit('%s' % e)


class MainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.rtsp_window = None
        self.m_Position = None
        self.setupUi(self)
        self.m_flag = False

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

        self.minButton.clicked.connect(self.showMinimized)
        self.maxButton.clicked.connect(self.max_or_restore)
        self.closeButton.clicked.connect(self.close)

        self.qtimer = QTimer(self)
        self.qtimer.setSingleShot(True)
        self.qtimer.timeout.connect(lambda: self.statistic_label.clear())

        self.comboBox.clear()
        self.pt_list = os.listdir('./pt')
        self.pt_list = [file for file in self.pt_list if file.endswith('.pt')]
        self.pt_list.sort(key=lambda x: os.path.getsize('./pt/' + x))
        self.comboBox.clear()
        self.comboBox.addItems(self.pt_list)
        self.qtimer_search = QTimer(self)
        self.qtimer_search.timeout.connect(lambda: self.search_pt())
        self.qtimer_search.start(2000)

        self.det_thread = DetThread()
        self.model_type = self.comboBox.currentText()
        self.det_thread.weights = "./pt/%s" % self.model_type
        self.det_thread.source = '0'
        self.det_thread.percent_length = self.progressBar.maximum()
        self.det_thread.send_img.connect(lambda x: self.show_image(x, self.out_video))
        self.det_thread.send_msg.connect(lambda x: self.show_msg(x))
        self.det_thread.send_percent.connect(lambda x: self.progressBar.setValue(x))
        self.det_thread.send_fps.connect(lambda x: self.fps_label.setText(x))
        self.fileButton.clicked.connect(self.open_file)
        self.cameraButton.clicked.connect(self.chose_cam)
        self.rtspButton.clicked.connect(self.chose_rtsp)

        self.runButton.clicked.connect(self.run_or_continue)
        self.stopButton.clicked.connect(self.stop)
        self.comboBox.currentTextChanged.connect(self.change_model)
        self.comboBox.currentTextChanged.connect(lambda x: self.statistic_msg('模型切换为%s' % x))
        self.confSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'confSpinBox'))
        self.confSlider.valueChanged.connect(lambda x: self.change_val(x, 'confSlider'))
        self.iouSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'iouSpinBox'))
        self.iouSlider.valueChanged.connect(lambda x: self.change_val(x, 'iouSlider'))
        self.rateSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'rateSpinBox'))
        self.rateSlider.valueChanged.connect(lambda x: self.change_val(x, 'rateSlider'))

        self.checkBox.clicked.connect(self.checkrate)
        self.load_setting()

    def search_pt(self):
        """
        """
        pt_list = os.listdir('./pt')
        pt_list = [file for file in pt_list if file.endswith('.pt')]
        pt_list.sort(key=lambda x: os.path.getsize('./pt/' + x))

        if pt_list != self.pt_list:
            self.pt_list = pt_list
            self.comboBox.clear()
            self.comboBox.addItems(self.pt_list)

    def checkrate(self):
        """
        """
        if self.checkBox.isChecked():

            self.det_thread.rate_check = True
        else:
            self.det_thread.rate_check = False

    def chose_rtsp(self):
        """
        """
        self.rtsp_window = Window()
        config_file = 'config/ip.json'
        if not os.path.exists(config_file):
            ip = "rtsp://admin:admin888@192.168.1.67:555"
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            ip = config['ip']
        self.rtsp_window.rtspEdit.setText(ip)
        self.rtsp_window.show()
        self.rtsp_window.rtspButton.clicked.connect(lambda: self.load_rtsp(self.rtsp_window.rtspEdit.text()))

    def load_rtsp(self, ip):
        """
        """
        try:
            self.stop()
            MessageBox(self.closeButton, text='请稍等，正在加载rtsp视频流', auto=True).exec()
            self.det_thread.source = ip
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open('config/ip.json', 'w', encoding='utf-8') as f:
                f.write(new_json)
            self.statistic_msg('加载rtsp：{}'.format(ip))
            self.rtsp_window.close()
        except Exception as e:
            self.statistic_msg('%s' % e)

    def chose_cam(self):
        """
        """
        try:
            self.stop()

            _, cams = Camera().get_cam_num()

            popMenu = QMenu()
            popMenu.setFixedWidth(self.cameraButton.width())
            popMenu.setStyleSheet('''
                                            QMenu {
                                            font-size: 16px;
                                            font-family: "Microsoft YaHei UI";
                                            font-weight: light;
                                            color:white;
                                            padding-left: 5px;
                                            padding-right: 5px;
                                            padding-top: 4px;
                                            padding-bottom: 4px;
                                            border-style: solid;
                                            border-width: 0px;
                                            border-color: rgba(255, 255, 255, 255);
                                            border-radius: 3px;
                                            background-color: rgba(200, 200, 200,50);}
                                            ''')

            for cam in cams:
                exec("action_%s = QAction('%s')" % (cam, cam))
                exec("popMenu.addAction(action_%s)" % cam)

            x = self.groupBox_5.mapToGlobal(self.cameraButton.pos()).x()
            y = self.groupBox_5.mapToGlobal(self.cameraButton.pos()).y()
            y = y + self.cameraButton.frameGeometry().height()
            pos = QPoint(x, y)
            action = popMenu.exec(pos)
            if action:
                self.det_thread.source = action.text()
                self.statistic_msg('加载摄像头：{}'.format(action.text()))

        except Exception as e:
            self.statistic_msg('%s' % e)

    def load_setting(self):
        config_file = 'config/setting.json'
        if not os.path.exists(config_file):
            iou = 0.9
            conf = 0.5
            rate = 0
            check = 0
            new_config = {"iou": iou, "conf": conf, "rate": rate, "check": check, }
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            if len(config) != 5:
                iou = 0.9
                conf = 0.5
                rate = 0
                check = Qt.Unchecked
            else:
                iou = config['iou']
                conf = config['conf']
                rate = config['rate']
                check = Qt.Unchecked
        self.confSpinBox.setValue(iou)
        self.iouSpinBox.setValue(conf)
        self.rateSpinBox.setValue(rate)
        self.checkBox.setCheckState(Qt.Unchecked)
        self.det_thread.rate_check = check

    def change_val(self, x, flag):
        """
        """
        if flag == 'confSpinBox':
            self.confSlider.setValue(int(x * 100))
        elif flag == 'confSlider':
            self.confSpinBox.setValue(x / 100)
            self.det_thread.conf_thres = x / 100
        elif flag == 'iouSpinBox':
            self.iouSlider.setValue(int(x * 100))
        elif flag == 'iouSlider':
            self.iouSpinBox.setValue(x / 100)
            self.det_thread.iou_thres = x / 100
        elif flag == 'rateSpinBox':
            self.rateSlider.setValue(x)
        elif flag == 'rateSlider':
            self.rateSpinBox.setValue(x)
            self.det_thread.rate = x * 10
        else:
            pass

    def statistic_msg(self, msg):
        """
        """
        self.statistic_label.setText(msg)

    def show_msg(self, msg):
        """
        """
        self.runButton.setChecked(Qt.Unchecked)
        self.statistic_msg(msg)

    def change_model(self, x):
        """
        """
        self.model_type = self.comboBox.currentText()
        self.det_thread.weights = "./pt/%s" % self.model_type
        self.statistic_msg('模型切换为%s' % x)

    def open_file(self):

        config_file = 'config/fold.json'

        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, '选取视频或图片', open_fold, "Pic File(*.mp4 *.mkv *.avi *.flv "
                                                                                 "*.jpg *.png)")
        if name:
            self.det_thread.source = name
            self.statistic_msg('加载文件：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)

            self.stop()

    def max_or_restore(self):
        """
        """
        if self.maxButton.isChecked():
            self.showMaximized()
        else:
            self.showNormal()

    def run_or_continue(self):
        """
        """
        self.det_thread.jump_out = False
        if self.runButton.isChecked():
            self.det_thread.is_continue = True
            if not self.det_thread.isRunning():
                self.det_thread.start()
            source = os.path.basename(self.det_thread.source)
            source = '摄像头设备' if source.isnumeric() else source
            self.statistic_msg('正在检测 >> 模型：{}，文件：{}'.format(os.path.basename(self.det_thread.weights), source))
        else:
            self.det_thread.is_continue = False
            self.statistic_msg('暂停')

    def stop(self):
        """
        """
        self.det_thread.jump_out = True

    def mousePressEvent(self, event):
        """
        """
        self.m_Position = event.pos()
        if event.button() == Qt.LeftButton:
            if 0 < self.m_Position.x() < self.groupBox.pos().x() + self.groupBox.width() and 0 < self.m_Position.y() < self.groupBox.pos().y() + self.groupBox.height():
                self.m_flag = True

    def mouseMoveEvent(self, QMouseEvent):
        """
        """
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        """
        """
        self.m_flag = False
        self.setCursor(QCursor())

    @staticmethod
    def show_image(img_src, label):
        """
        """
        try:
            ih, iw, _ = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()

            if iw > ih:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (nw, nh))

            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(img_src, (nw, nh))

            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(img))

        except Exception as e:
            print(repr(e))

    def show_statistic(self, results):
        self.resultWidget.clear()
        self.resultWidget.addItems(results)

    def closeEvent(self, event):

        self.det_thread.jump_out = True

        config = dict()
        config['iou'] = self.confSpinBox.value()
        config['conf'] = self.iouSpinBox.value()
        config['rate'] = self.rateSpinBox.value()
        config['check'] = self.checkBox.checkState()
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication()
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec())
