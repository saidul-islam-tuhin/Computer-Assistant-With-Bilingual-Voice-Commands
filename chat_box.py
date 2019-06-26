##−∗−coding :  utf−8−∗−

import sys
import time
import json

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow,
                            QGridLayout, QVBoxLayout, QHBoxLayout,QDialog,
                            QLabel, QMessageBox, QComboBox, QFrame, QSizePolicy,
                            QLineEdit, QTextEdit, QAction, QMenuBar, QPlainTextEdit,
                            QTableWidget, QTableWidgetItem)

from speech_to_text import stt
from commands_table import TableWindow
import folder_table
import send_email

import sql
import registration
import command_control
import conf

import logging

LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w",
                    )
logger = logging.getLogger(__name__)



class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Application'
        self.left = 20
        self.top = 20
        self.width = 800
        self.height = 480

        self.frame = None
        self.text = ''

        self.initUI()


    def initUI(self):
        
        try:
            with open('config.local.json') as f:
                conf.JSON_DATA = json.load(f)
        except FileNotFoundError:
            with open('config.json') as f:
                conf.JSON_DATA = json.load(f)

        # {'task': [...], 'english': [....], 'bangla': [....], 'security': [....], 'custom': [....]}
        self.all_commands = sql.run_query(query='SELECT * FROM COMMANDS')
        self.profile_info =  sql.run_query(query="SELECT * from USER")

        # check that any user data stored or not
        if len(self.profile_info) == 0:
            dialog = registration.Dialog()
            dialog.exec_()

        
        conf.USER_NAME = self.profile_info['name'][0]
        
        languages = ["english", "bangla", ]
        query_result = sql.run_query(query="select language from user") # Return type: Dictionary
        selected_lang = query_result['language'][0]
        index_no = languages.index(selected_lang.lower()) # Raise : Valuerror unless item is found


        """ ------------------- Design Main Window -------------------- """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        """ ------------------- Combo Box -------------------- """
        self.combo = QComboBox()
        self.combo.addItems(languages)
        self.combo.setCurrentIndex(index_no)


        """ ------------------- Label -------------------- """
        # Selected language label
        self.language_label = QLabel(selected_lang)
        self.language_label.setFont(QFont("Times", 12, QFont.Bold,))
        self.language_label.setStyleSheet("background-color:#f531ba;text-align:center;")


        """ ------------------- Text -------------------- """
        # Create Chat Box
        self.chat = QPlainTextEdit()
        self.chat.setReadOnly(True)

        # Create input box where user type his command
        self.chatTextField = QLineEdit()
        self.chatTextField.resize(480,100)
        self.chatTextField.move(10,350)


        """ ---------------- Button ---------------------- """
        # voice_btn not triggered when enter key pressed
        self.voice_btn = QPushButton(' Voice', default=False, autoDefault=False)
        self.voice_btn.setIcon(QIcon("icons/voice.png"))
        self.voice_btn.setStyleSheet("background-color:#31f5d7;font: 20px arial, sans-serif;")

        self.folder_btn = QPushButton("Folder", default=False, autoDefault=False)
        self.forget_pass_btn = QPushButton('Forget Password', default=False, autoDefault=False)
        self.commands_btn = QPushButton('Commands', default=False, autoDefault=False)


        """ -------------------- Layout -------------------------- """
        # Add horizontal layout
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        # Add vertical layout
        self.v_layout = QVBoxLayout()

        self.v_layout.addWidget(self.language_label)
        self.v_layout.addWidget(self.chat,)
        self.v_layout.addWidget(self.chatTextField,)
        self.v_layout.addWidget(self.voice_btn,)

        # Tools vertical layout
        self.tools_v_layout = QVBoxLayout()
        self.tools_v_layout.addWidget(self.combo)
        self.tools_v_layout.addWidget(self.forget_pass_btn)
        self.tools_v_layout.addWidget(self.folder_btn)
        self.tools_v_layout.addWidget(self.commands_btn)

        self.h_layout.addLayout(self.v_layout)
        self.h_layout.addLayout(self.tools_v_layout)


        """ ------------------ triggered button ---------------"""
        self.voice_btn.clicked.connect(self.voice_text)
        self.folder_btn.clicked.connect(folder_table.main)
        self.forget_pass_btn.clicked.connect(self.send_password)
        self.commands_btn.clicked.connect(self.show_table)
        self.combo.activated[str].connect(lambda : self.language_label.setText((self.combo.currentText()).capitalize()))

        self.show()


    @pyqtSlot()
    def send_password(self):
        """ Collect password and email_address from database.
            Generate subject and body of email.
            Call send email func.
        """

        password = self.profile_info['password'][0]
        email_address = self.profile_info['email'][0]

        subject = "Password of voice application"
        msg = "Your password is: {}".format(password)

        QMessageBox.about(self,"Forget Password","Please Check your email inbox.")
        send_email.send_email_func(
            to_email_id = email_address,
            subject = subject,
            body = msg
        )


    @pyqtSlot()
    def voice_text(self):
        """ Convert voice to text and appear the text into chatbox """
        
        current_lang = self.combo.currentText() # collect selected language from combo box

        if conf.NEW_COMMAND:
            update_commands = sql.run_query(query='SELECT * FROM COMMANDS')
            self.all_commands = update_commands
            conf.NEW_COMMAND = False

        self.text = stt.stt_func(selected_lang=current_lang) 

        self.text_append(self.text)

        self.send_to_command(current_lang)


    def send_to_command(self, current_lang):

        command_control.input_parser(
            commands_list = self.all_commands,
            selected_lang = current_lang,
            command = self.text,
            profile_info = self.profile_info,
            )

        self.text = ''

    
    def text_append(self, text):
        """ Show USER speech_to_text into window """

        textFormatted='<b>{}: </b><span style=" font-size:12pt; font-weight:600; color:#33c4ff;">{}</span>'.format(conf.USER_NAME.capitalize(),text)
        self.chat.appendHtml(textFormatted)
        conf.CHAT_OBJ = self.chat # Make pulic of chat object so that we can use this object from other file by conf.CHAT_OBJ


    @pyqtSlot()
    def show_table(self):
        """ Show all command list into table """
        
        if conf.NEW_COMMAND:
            update_commands = sql.run_query(query='SELECT * FROM COMMANDS')
            self.all_commands = update_commands
            conf.NEW_COMMAND = False

        column_names = tuple(self.all_commands.keys())
        row_values = tuple(self.all_commands.values())
        col_size = len(column_names)
        row_size = len((row_values)[0])

        ab = TableWindow(row_values, column_names, row_size, col_size)
        if ab.exec_():
            ab.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
