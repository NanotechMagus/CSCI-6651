#!/etc/python-3.9

# This code was authored by Brandon Frostbourne
# Written for the CSCI-6651-01 - Scripting / Python class at University of New Haven taught by George Pillar III
# Assignment: [insert assignment name or number]

# Standard Library Imports
import logging
import os, sys, platform, json

# Third-party Library Imports
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QWidget, QTextEdit, QPushButton, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QFrame, QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path

# Local Library Imports
from engine.pyqtbuilder import QtBuilder
__version__ = "1.0.0"

# In-window logging display mechanism
class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

# This snippet loads the version and app identifier for Windows systems for process identification
try:
    from PyQt5.QtWinExtras import QtWin
    myappid = f'CSCI6651.PythonProject.BMF-GUI.{__version__}'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class Project(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.builder = QtBuilder()
            self.builder.settings = self.builder.settings
        except FileNotFoundError as err:
            logging.warning(f"System exiting: {err}")
            sys.exit(1)
        self.crypt = None
        self.layouts = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: []
        }

        # Set the size and title of the window
        self.resize(800, 600)
        self.setWindowTitle(self.builder.settings["txt"]["WindowTitle"])

        # Image Banner
        self._img_banner = QLabel(self)
        self._img_banner.setPixmap(QPixmap(self.builder.settings['loc']["banner"]))
        self._img_banner.setScaledContents(False)
        self.layouts[0].append(self._img_banner)
        self.layouts[0].append(self.builder.lin_seperator())

        # Text Box // window for file path
        self._box_fp_window = self.builder.text_box(
            self,
            self.builder.settings["txt"]["pathtext"],
            28
        )
        self.builder.settings["txt"]["outfile"] = self._box_fp_window.toPlainText()
        self.layouts[0].append(self._box_fp_window)

        # # Text Box // window for encryption token path
        self._box_tkn_window = self.builder.text_box(
            self,
            self.builder.settings["txt"]["tknpath"],
            28
        )
        self.builder.settings["txt"]["tokenfile"] = self._box_tkn_window.toPlainText()
        self.layouts[0].append(self._box_tkn_window)

        # Find File Button
        self._btn_fp_findfile = self.builder.btn_stage(
            self,
            self.builder.settings["txt"]["boxfpv"],
            self.builder.settings['css']['nbutton'],
            (lambda: self.builder.get_file_path("Text files (*.txt)"))
        )
        # self.layouts[2].append(self._btn_fp_findfile)

        # Create File Button
        self._btn_fp_createfile = self.builder.btn_stage(
            self,
            self.builder.settings["txt"]["create"],
            self.builder.settings['css']['nbutton'],
            (lambda: self.builder.get_file_path("Text files (*.txt)"))
        )
        # self.layouts[2].append(self._btn_fp_createfile)

        # Find Token button
        self._btn_tkn_findfile = self.builder.btn_stage(
            self,
            self.builder.settings["txt"]["tknfpv"],
            self.builder.settings['css']['nbutton'],
            (lambda: self.builder.get_file_path(self, "Text files (*.token)"))
        )
        # self.layouts[2].append(self._btn_tkn_findfile)

        # Create Token button
        self._btn_tkn_createfile = self.builder.btn_stage(
            self,
            self.builder.settings["txt"]["createtkn"],
            self.builder.settings['css']['nbutton'],
            (lambda: self.builder.get_file_path("Token files (*.token)"))
        )
        # self.layouts[2].append(self._btn_tkn_createfile)

        # Align buttons
        filebtnV = QVBoxLayout()
        filebtnV.addWidget(self._btn_fp_findfile)
        filebtnV.addWidget(self._btn_fp_createfile)
        tknbtnV = QVBoxLayout()
        tknbtnV.addWidget(self._btn_tkn_findfile)
        tknbtnV.addWidget(self._btn_tkn_createfile)
        filetknH = QHBoxLayout()
        filetknH.addLayout(filebtnV)
        filetknH.addLayout(tknbtnV)
        self.layouts[2].append(filetknH)

        # Logging box
        self._box_log = QTextEditLogger(self)
        self._box_log.setFormatter(
            logging.Formatter("[{asctime}] [{levelname}] {name}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
        )
        logging.getLogger().addHandler(self._box_log)
        logging.getLogger().setLevel(logging.INFO)
        self.debug_info()
        self.layouts[3].append(self._box_log.widget)

        # Debug mode checkbox
        self._cbx_debug = self.builder.cbx_stage(
            self,
            self.builder.settings["txt"]["dbgchk"],
            (lambda: self._combobox_changed(self._cbx_debug))
        )

        # Log file checkbox
        self._cbx_log = self.builder.cbx_stage(
            self,
            self.builder.settings["txt"]["logchk"],
            (lambda: self._combobox_changed(self._cbx_log))
        )

        # Add checkboxes to a grid and add to layout
        btnlayout = QHBoxLayout()
        btnlayout.addWidget(self._cbx_debug)
        btnlayout.addWidget(self._cbx_log)
        self.layouts[1].append(btnlayout)

        # About Me text blurb at bottom
        self._txt_about = QLabel(self)
        self._txt_about.setText(
            f"{self.builder.settings['txt']['copyright']} | Developed by {self.builder.settings['txt']['author']} "
            f"for the University of New Haven class CSCI-6651 | All rights reserved | version {__version__}"
        )
        self._txt_about.setAlignment(Qt.AlignCenter)
        self.layouts[4].append(self._txt_about)

        btngrid_disp = QVBoxLayout()
        # Button for displaying all numbers with sum and average
        self._btn_disp_all = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['disp_all'],
            self.builder.settings['css']['nbutton'],
            None
        )
        self.layouts[3].append(self._btn_disp_all)
        # self._btn_disp_all.setText(self.staticText["disp_all"])
        # self._btn_disp_all.setStyleSheet("background-color : #000000")
        # self._btn_disp_all.clicked.connect()

        # Button for displaying all numbers sorted ascending
        self._btn_disp_asc = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['disp_asc'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_disp.addWidget(self._btn_disp_asc)
        # self._btn_disp_asc.setText(self.staticText["disp_asc"])
        # self._btn_disp_asc.setStyleSheet("background-color : #000000")
        # self._btn_disp_asc.clicked.connect()

        # Button for displaying all numbers sorted descending
        self._btn_disp_dec = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['disp_dec'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_disp.addWidget(self._btn_disp_dec)
        # self._btn_disp_dec.setText(self.staticText["disp_dec"])
        # self._btn_disp_dec.setStyleSheet("background-color : #000000")
        # self._btn_disp_dec.clicked.connect()

        btngrid_sort = QVBoxLayout()
        # Button for searching numbers and number of occurrences
        self._btn_search = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['search'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_sort.addWidget(self._btn_search)
        # self._btn_search.setText(self.staticText["search"])
        # self._btn_search.setStyleSheet("background-color : #000000")
        # self._btn_search.clicked.connect()

        # Button for displaying largest number
        self._btn_largest = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['largest'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_sort.addWidget(self._btn_largest)
        # self._btn_largest.setText(self.staticText["largest"])
        # self._btn_largest.setStyleSheet("background-color : #000000")
        # self._btn_largest.clicked.connect()

        btngrid_apnd = QVBoxLayout()
        # Button for appending number
        self._btn_append = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['append'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_apnd.addWidget(self._btn_append)
        # self._btn_append.setText(self.staticText["append"])
        # self._btn_append.setStyleSheet("background-color : #000000")
        # self._btn_append.clicked.connect()

        btngrid_encrypt = QVBoxLayout()
        # Button for encrypting file
        self._btn_encrypt = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['encrypt'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_encrypt.addWidget(self._btn_encrypt)
        # self._btn_encrypt.setText(self.staticText["encrypt"])
        # self._btn_encrypt.setStyleSheet("background-color : #000000")
        # self._btn_encrypt.clicked.connect()

        # Button for decrypting file
        self._btn_decrypt = self.builder.btn_stage(
            self,
            self.builder.settings['txt']['decrypt'],
            self.builder.settings['css']['nbutton'],
            None
        )
        btngrid_encrypt.addWidget(self._btn_decrypt)
        # self._btn_decrypt.setText(self.staticText["decrypt"])
        # self._btn_decrypt.setStyleSheet("background-color : #000000")
        # self._btn_decrypt.clicked.connect()
        btngrid = QHBoxLayout()
        btngrid.addLayout(btngrid_disp)
        btngrid.addLayout(btngrid_sort)
        btngrid.addLayout(btngrid_apnd)
        btngrid.addLayout(btngrid_encrypt)
        self.layouts[3].append(btngrid)

        # Button for exit program
        self._btn_exit = self.builder.btn_stage(
            self,
            self.builder.settings['txt']["exit"],
            "background-color : #FFFFFF",
            self.builder.quit_app
        )
        self.layouts[3].append(self._btn_exit)


        toplayout = QVBoxLayout()
        for items in self.layouts.keys():
            for things in self.layouts[items]:
                if isinstance(things, QHBoxLayout or QVBoxLayout):
                    toplayout.addLayout(things)
                elif isinstance(things, QWidget):
                    toplayout.addWidget(things)
            toplayout.addWidget(self.builder.lin_seperator())

        self.setLayout(toplayout)

    def debug_info(self):
        os_info = platform.uname()
        osver = "{} {} (version {})".format(os_info.system, os_info.release, os_info.version)
        logging.info(
            "\nInitial System Information\n\n"
            + f"OS version: {osver}\n"
            + f"System arch: {platform.machine()}\n"
            + f"Python version: {sys.version}\n\n"
        )

    def _combobox_changed(self, button):
        if button.text() == self.builder.settings['txt']['logchk']:
            if button.isChecked():
                self.builder.settings['loc']['filelog'] = True
            else:
                self.builder.settings['loc']['filelog'] = False
        elif button.text() == self.builder.settings['txt']['dbgchk']:
            if button.isChecked():
                self.builder.settings['loc']["logstate"] = logging.DEBUG
                logging.getLogger().setLevel(logging.DEBUG)
            else:
                self.builder.settings['loc']['logstate'] = logging.INFO


if __name__ == "__main__":
    app = QApplication(sys.argv)

    FinalProject = Project()
    FinalProject.show()

    sys.exit(app.exec_())

