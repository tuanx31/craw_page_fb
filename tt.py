import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFileDialog
from PyQt6.QtCore import QFile

class ConfigurationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuration App")
        self.setGeometry(100, 100, 500, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 10, 480, 280)

        self.save_button = QPushButton("Save Configuration", self)
        self.save_button.setGeometry(10, 300, 150, 30)
        self.save_button.clicked.connect(self.save_configuration)

        self.load_button = QPushButton("Load Configuration", self)
        self.load_button.setGeometry(170, 300, 150, 30)
        self.load_button.clicked.connect(self.load_configuration)

    def save_configuration(self):
        config_text = self.text_edit.toPlainText()
        filename = f"cauhinh{self.get_configuration_count()}.txt"
        with open(filename, "w") as file:
            file.write(config_text)

    

    def get_configuration_count(self):
        count = 0
        while True:
            filename = f"cauhinh{count}.txt"
            if not QFile.exists(filename):
                break
            count += 1
        return count

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigurationApp()
    window.show()
    sys.exit(app.exec())
