#!/usr/bin/env python
from PySide import QtCore, QtGui
import resources_rc

ICONS = dict(    
    downarrow = QtGui.QIcon(":/icons/QComboBox_down_arrow.png"),
    checkbox_checked = QtGui.QIcon(":/icons/QCheckBox_checked.png"),
    checkbox_checkedhover = QtGui.QIcon(":/icons/QCheckbox_checked_hover.png"),
    checkbox_unchecked = QtGui.QIcon(":/icons/QCheckBox_unchecked.png"),
    checkbox_uncheckedhover = QtGui.QIcon(":/icons/QCheckbox_unchecked_hover.png"),
    radio_checked = QtGui.QIcon(":/icons/QRadioButton_checked.png"),
    radio_checkedhover = QtGui.QIcon(":/icons/QRadioButton_checked_hover.png"),
    radio_unchecked = QtGui.QIcon(":/icons/QRadioButton_unchecked.png"),
    radio_uncheckedhover = QtGui.QIcon(":/icons/QRadioButton_unchecked_hover.png"),
    spinbox_leftarrow = QtGui.QIcon(":/icons/QSpinBox_left_arrow.png"),
    spinbox_rightarrow = QtGui.QIcon(":/icons/QSpinBox_right_arrow.png"),
)


class IconMapper(object):
    def __init__(self, node=None):
        self.node = node
