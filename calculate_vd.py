import numpy as np
from widgets_1 import widgets_1
import cable_resistances


class calculate_vd:
    def __init__(self,
                 voltage_level,
                 phase,
                 conductor_type,
                 vd_allowance,
                 sets,
                 conductor_size,
                 current,
                 length):
        self.voltage_level = float(voltage_level)
        self.phase = phase
        self.conductor_type = conductor_type
        self.vd_allowance = float(vd_allowance.strip('%'))
        self.sets = int(sets)
        self.conductor_size = conductor_size
        try:
            self.current = float(current)
        except ValueError:
            self.current = 0
        try:
            self.length = float(length)
        except ValueError:
            self.length = 0
        self.vd_temp = 0
        if self.phase:
            self.multi_factor = np.sqrt(2)
        else:
            self.multi_factor = 2
        self.resistance = self.find_cable_resistance()
        self.vd_absolute = self.calculate_vd()[0]
        self.vd_percent = self.calculate_vd()[1]

    def find_cable_resistance(self):
        if self.conductor_type:
            for key, value in cable_resistances.copper.items():
                if key == self.conductor_size:
                    return value / 1000

        else:
            for key, value in cable_resistances.aluminum.items():
                if key == self.conductor_size:
                    return value / 1000

    def calculate_vd(self):
        vd_absolute = (self.current * self.length * self.resistance * self.multi_factor) / self.sets
        vd_pecent = (vd_absolute/self.voltage_level)*100
        return f'VD(V): {round(vd_absolute,2):.2f}', f'VD(%): {round(vd_pecent,2):.2f}%'


