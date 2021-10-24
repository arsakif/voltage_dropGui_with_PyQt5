from PyQt5.QtWidgets import *
import sys

from widgets_1 import widgets_1
from calculate_vd import calculate_vd


class ToolBar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.toolbar = QToolBar('VD Toolbar')


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.setMinimumSize(500, 400)
        self.toolbar = ToolBar().toolbar
        self.addToolBar(self.toolbar)

        # --------First Grid--------------------------------------
        self.grid_layout1 = QGridLayout()
        self.grid_layout1.addWidget(widgets_1().voltage_level_groupbox, 0, 0)
        self.grid_layout1.addWidget(widgets_1().phase_groupbox, 0, 1)
        self.grid_layout1.addWidget(widgets_1().conductor_type_groupbox, 0, 2)
        self.grid_layout1.addWidget(widgets_1().vd_allowance_groupbox, 0, 3)
        self.grid_layout1.addWidget(widgets_1().sets_groupbox, 1, 0)
        self.grid_layout1.addWidget(widgets_1().cable_size_groupbox, 1, 1)
        self.grid_layout1.addWidget(widgets_1().current_groupbox, 1, 2)
        self.grid_layout1.addWidget(widgets_1().length_groupbox, 1, 3)
        self.grid_layout1.addWidget(widgets_1().vd_result_groupbox, 2, 0)
        self.grid_layout1.addWidget(widgets_1().max_length_groupbox, 2, 1)
        self.grid_layout1.addWidget(widgets_1().fail_ok_groupbox, 2, 2)
        self.grid_layout1.addWidget(widgets_1().suggest_size_groupbox, 2, 3)

        # -------------------------------------------
        self.vboxlayout_1 = QVBoxLayout()
        # self.vboxlayout_1.addStretch()
        self.vboxlayout_1.addLayout(self.grid_layout1)
        # --------------------------------------------

        self.widget = QWidget()
        self.widget.setLayout(self.vboxlayout_1)
        self.setCentralWidget(self.widget)

        self.widget_dic_1 = self.process_widgets()
        self.set_connections()

        self.vd_resluts = self.run_button_click()

    def process_widgets(self):
        widget_dic_1 = {
            'voltage_level': self.findChild(QComboBox, name='voltage_level_value'),
            'phase_3': self.findChild(QRadioButton, name='phase_3'),
            'phase_1': self.findChild(QRadioButton, name='phase_1'),
            'copper': self.findChild(QRadioButton, name='copper'),
            'aluminum': self.findChild(QRadioButton, name='aluminum'),
            'vd_allowance': self.findChild(QComboBox, name='allowance'),
            'sets': self.findChild(QSpinBox, name='sets'),
            'conductor_size': self.findChild(QComboBox, name='conductor_size'),
            'current': self.findChild(QLineEdit, name='current'),
            'length': self.findChild(QLineEdit, name='length'),
            'vd_percent_result': self.findChild(QLabel, name='vd_percent_result'),
            'vd_absolute_result': self.findChild(QLabel, name='vd_absolute_result'),
            'max_length': self.findChild(QLabel, name='max_length'),
            'fail_okay': self.findChild(QLabel, name='fail_okay'),
            'suggest': self.findChild(QLabel, name='suggest')
        }
        return widget_dic_1

    def set_connections(self):
        self.widget_dic_1['voltage_level'].currentTextChanged.connect(self.run_button_click)
        self.widget_dic_1['phase_3'].clicked.connect(self.run_button_click)
        self.widget_dic_1['phase_1'].clicked.connect(self.run_button_click)
        self.widget_dic_1['copper'].clicked.connect(self.run_button_click)
        self.widget_dic_1['aluminum'].clicked.connect(self.run_button_click)
        self.widget_dic_1['vd_allowance'].currentTextChanged.connect(self.run_button_click)
        self.widget_dic_1['sets'].valueChanged.connect(self.run_button_click)
        self.widget_dic_1['conductor_size'].currentTextChanged.connect(self.run_button_click)
        self.widget_dic_1['current'].textEdited.connect(self.run_button_click)
        self.widget_dic_1['length'].textEdited.connect(self.run_button_click)

    def run_button_click(self):
        vd_resluts = calculate_vd(
            self.widget_dic_1['voltage_level'].currentText(),
            self.widget_dic_1['phase_3'].isChecked(),
            self.widget_dic_1['copper'].isChecked(),
            self.widget_dic_1['vd_allowance'].currentText(),
            self.widget_dic_1['sets'].text(),
            self.widget_dic_1['conductor_size'].currentText(),
            self.widget_dic_1['current'].text(),
            self.widget_dic_1['length'].text())

        self.widget_dic_1['vd_absolute_result'].setText(vd_resluts.vd_absolute)
        self.widget_dic_1['vd_percent_result'].setText(vd_resluts.vd_percent)
        self.widget_dic_1['max_length'].setText(vd_resluts.max_length)

        self.configure_fail_ok_label(vd_resluts.fail_okay)

        return vd_resluts

    def configure_fail_ok_label(self, fail_okey):
        if fail_okey:
            self.widget_dic_1['fail_okay'].setText('OKAY')
            self.widget_dic_1['fail_okay'].setStyleSheet(
                                'background-color: #20b050;'
                                'color: white;'
                                'font-size: 35pt;'
                                'text-align: center;'
                                'font: bold')
        else:
            self.widget_dic_1['fail_okay'].setText('FAIL ')
            self.widget_dic_1['fail_okay'].setStyleSheet(
                'background-color: #85241e;'
                'color: #e0ecff;'
                'font-size: 35pt;'
                'text-align: center;'
                'font: bold')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
