import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QStyleFactory
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import random

class PasswordManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setFixedSize(800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Website", "Username", "Password"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.form_layout = QHBoxLayout()
        self.layout.addLayout(self.form_layout)

        self.labels = ["Website", "Username", "Password"]
        self.entries = []

        for label in self.labels:
            self.form_layout.addWidget(QLabel(label + ":"))
            entry = QLineEdit()
            self.entries.append(entry)
            self.form_layout.addWidget(entry)

        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.buttons = {
            "Add": self.add_entry,
            "Remove": self.remove_entry,
            "Update": self.update_entry,
            "Generate Password": self.generate_password,
            "Dark/Light": self.toggle_dark_mode
        }

        for button_text, button_action in self.buttons.items():
            button = QPushButton(button_text)
            button.clicked.connect(button_action)
            self.button_layout.addWidget(button)

        self.dark_mode = False

    def add_entry(self):
        values = [entry.text() for entry in self.entries]
        if all(values):
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            for column, value in enumerate(values):
                self.table.setItem(row_count, column, QTableWidgetItem(value))
                self.entries[column].clear()

    def remove_entry(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.table.removeRow(selected_row)

    def update_entry(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            values = [entry.text() for entry in self.entries]
            if all(values):
                for column, value in enumerate(values):
                    self.table.setItem(selected_row, column, QTableWidgetItem(value))
                    self.entries[column].clear()

    def generate_password(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
        password = "".join(random.sample(characters, 20))
        self.entries[-1].setText(password)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.setStyleSheet("QMainWindow { background-color: #1E1E1E; color: #FFFFFF; }"
                           "QLabel { color: #FFFFFF; }"
                           "QLineEdit { background-color: #333333; color: #FFFFFF; }"
                           "QTableWidget { background-color: #333333; color: #FFFFFF; }"
                           "QPushButton { background-color: #333333; color: #FFFFFF; }"
                           "QHeaderView::section { background-color: #333333; color: #FFFFFF; }"
                           "QToolBar { background-color: #333333; color: #FFFFFF; }"
                           "QMenuBar { background-color: #333333; color: #FFFFFF; }"
                           "QStatusBar { background-color: #333333; color: #FFFFFF; }")
        else:
            self.setStyleSheet("QMainWindow { background-color: #F0F0F0; color: #000000; }"
                           "QLabel { color: #000000; }"
                           "QLineEdit { background-color: #FFFFFF; color: #000000; }"
                           "QTableWidget { background-color: #FFFFFF; color: #000000; }"
                           "QPushButton { background-color: #FFFFFF; color: #000000; }"
                           "QHeaderView::section { background-color: #F0F0F0; color: #000000; }"
                           "QToolBar { background-color: #F0F0F0; color: #000000; }"
                           "QMenuBar { background-color: #F0F0F0; color: #000000; }"
                           "QStatusBar { background-color: #F0F0F0; color: #000000; }")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PasswordManager()
    window.show()
    sys.exit(app.exec_())
