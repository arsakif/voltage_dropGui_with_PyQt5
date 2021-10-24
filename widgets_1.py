from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cable_resistances


class widgets_1(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # VOLTAGE LEVEL
        voltage_level_lable = QLabel('Voltage (V)')
        voltage_level_value = QComboBox()
        voltage_level_value.setObjectName('voltage_level_value')
        voltage_level_value.addItems(['120', '208', '277', '480', 'Custom'])
        voltage_level_vbox = QVBoxLayout()
        voltage_level_vbox.addWidget(voltage_level_lable)
        voltage_level_vbox.addWidget(voltage_level_value)
        self.voltage_level_groupbox = QGroupBox()
        self.voltage_level_groupbox.setLayout(voltage_level_vbox)

        # PHASE CHOISE
        phase_3_radio_btn = QRadioButton('3-Phase')
        phase_3_radio_btn.setObjectName('phase_3')
        phase_3_radio_btn.setChecked(True)
        phase_1_radio_btn = QRadioButton('1-Phase')
        phase_1_radio_btn.setObjectName('phase_1')
        phase_vbox = QVBoxLayout()
        phase_vbox.addWidget(phase_3_radio_btn)
        phase_vbox.addWidget(phase_1_radio_btn)
        self.phase_groupbox = QGroupBox()
        self.phase_groupbox.setLayout(phase_vbox)

        # Conductor Type CHOISE
        cu_btn = QRadioButton('Copper')
        cu_btn.setObjectName('copper')
        cu_btn.setChecked(True)
        al_btn = QRadioButton('Aluminum')
        al_btn.setObjectName('aluminum')
        conductor_type_vbox = QVBoxLayout()
        conductor_type_vbox.addWidget(cu_btn)
        conductor_type_vbox.addWidget(al_btn)
        self.conductor_type_groupbox = QGroupBox()
        self.conductor_type_groupbox.setLayout(conductor_type_vbox)

        # VOLTAGE DROP ALLOVANCE
        vd_allowance_lable = QLabel('VD Allowance (%)')
        vd_allowance_value = QComboBox()
        vd_allowance_value.setObjectName('allowance')
        vd_allowance_value.addItems(['3%', '5%', 'Custom'])
        vd_allowance_vbox = QVBoxLayout()
        vd_allowance_vbox.addWidget(vd_allowance_lable)
        vd_allowance_vbox.addWidget(vd_allowance_value)
        self.vd_allowance_groupbox = QGroupBox()
        self.vd_allowance_groupbox.setLayout(vd_allowance_vbox)

        # PARALLEL SETS
        sets_lable = QLabel('Sets')
        sets_value = QSpinBox()
        sets_value.setObjectName('sets')
        sets_value.setMinimum(1)
        sets_vbox = QVBoxLayout()
        sets_vbox.addWidget(sets_lable)
        sets_vbox.addWidget(sets_value)
        self.sets_groupbox = QGroupBox()
        self.sets_groupbox.setLayout(sets_vbox)

        # CABLE SIZE
        cable_size_lable = QLabel('Cunductor Size')
        cable_size_value = QComboBox()
        cable_size_value.setObjectName('conductor_size')
        cable_size_value.addItems(cable_resistances.cable_sizes)
        cable_size_vbox = QVBoxLayout()
        cable_size_vbox.addWidget(cable_size_lable)
        cable_size_vbox.addWidget(cable_size_value)
        self.cable_size_groupbox = QGroupBox()
        self.cable_size_groupbox.setLayout(cable_size_vbox)

        # CURRENT VALUE
        current_lable = QLabel('Current(A)')
        current_value = QLineEdit('0')
        current_value.setObjectName('current')
        current_vbox = QVBoxLayout()
        current_vbox.addWidget(current_lable)
        current_vbox.addWidget(current_value)
        self.current_groupbox = QGroupBox()
        self.current_groupbox.setLayout(current_vbox)

        # LENGTH OF THE RUN
        length_lable = QLabel('Length(Ft)')
        length_value = QLineEdit('0')
        length_value.setObjectName('length')
        length_vbox = QVBoxLayout()
        length_vbox.addWidget(length_lable)
        length_vbox.addWidget(length_value)
        self.length_groupbox = QGroupBox()
        self.length_groupbox.setLayout(length_vbox)

        # VOLTAGE DROP RESULT
        vd_percent_value = QLabel('VD(%): 0')
        vd_percent_value.setObjectName('vd_percent_result')
        vd_absolute_value = QLabel('VD(V): 0')
        vd_absolute_value.setObjectName('vd_absolute_result')
        vd_result_vbox = QVBoxLayout()
        vd_result_vbox.addWidget(vd_percent_value)
        vd_result_vbox.addWidget(vd_absolute_value)
        self.vd_result_groupbox = QGroupBox()
        self.vd_result_groupbox.setLayout(vd_result_vbox)

        # Max Allowed Length
        max_length_lable = QLabel('Max Lenght(Ft)')
        max_length_value = QLabel('0')
        max_length_value.setObjectName('max_length')
        max_length_vbox = QVBoxLayout()
        max_length_vbox.addWidget(max_length_lable)
        max_length_vbox.addWidget(max_length_value)
        self.max_length_groupbox = QGroupBox()
        self.max_length_groupbox.setLayout(max_length_vbox)

        # Fail/Okay Label
        fail_ok_lable = QLabel('Fail/Okay')
        fail_ok_lable.setObjectName('fail_okay')
        fail_ok_vbox = QVBoxLayout()
        fail_ok_vbox.addWidget(fail_ok_lable)
        self.fail_ok_groupbox = QGroupBox()
        self.fail_ok_groupbox.setLayout(fail_ok_vbox)

        # Suggested Size
        suggest_size_label = QLabel('Suggested')
        suggest_size_value = QLabel('0')
        suggest_size_value.setObjectName('suggest')
        suggest_size_vbox = QVBoxLayout()
        suggest_size_vbox.addWidget(suggest_size_label)
        suggest_size_vbox.addWidget(suggest_size_value)
        self.suggest_size_groupbox = QGroupBox()
        self.suggest_size_groupbox.setLayout(suggest_size_vbox)







