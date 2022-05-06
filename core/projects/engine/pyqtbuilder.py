#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
import logging
import os, sys, platform
import json

# Third-party Library Imports
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QWidget, QTextEdit, QPushButton, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QFrame, QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path

# Local Library Imports


class QtBuilder(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = self.settings_init()

    def btn_stage(self, btnself, text: str, style: str, connect=None) -> QPushButton:
        btn_stage = QPushButton(btnself)
        btn_stage.setText(text)
        btn_stage.setStyleSheet(style)
        if connect:
            btn_stage.clicked.connect(connect)
        return btn_stage

    def quit_app(self):
        mbox = QMessageBox()
        mbox.setText(f"Are you sure you want to exit?")
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = mbox.exec()
        if returnValue == QMessageBox.Ok:
            sys.exit()

    def lin_seperator(self) -> QFrame:
        seperator = QFrame()
        seperator.setFrameShape(QFrame.HLine)
        seperator.setFrameShadow(QFrame.Sunken)
        return seperator

    def get_file_path(self, btn: QWidget, filetype: str):
        filename, _ = QFileDialog.getOpenFileName(
            btn,
            "Open File",
            'C:\\Users\\',
            filetype
        )
        self.settings['loc']['jsonfile'] = filename
        if self.settings['loc']["jsonfile"]:
            self.settings['loc']['fileloc'] = os.path.dirname(os.path.abspath(filename))
            self.settings['loc']["logfile"] = f"{filename}.log"

    def text_box(self, boxself: QWidget, text: str, height: int) -> QTextEdit:
        box_window = QTextEdit(boxself)
        box_window.setText(text)
        box_window.setFixedHeight(height)
        return box_window

    def cbx_stage(self, cbxself, text: str, connect=None) -> QCheckBox:
        cbx_stage = QCheckBox(cbxself)
        cbx_stage.setText(text)
        cbx_stage.stateChanged.connect(connect)
        return cbx_stage

    def settings_init(self):
        settings = Path(os.getcwd(), "./etc/settings.json")
        logging.info(f"Loading settings from {settings.absolute()}")
        if Path.exists(settings):
            with open(settings, "r") as f:
                return json.load(f)
        else:
            raise FileNotFoundError