from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication([])

# Tạo một instance của QMessageBox
message_box = QMessageBox()
message_box.setText("Hello World!")

# Áp dụng CSS để thay đổi màu văn bản
message_box.setStyleSheet("QMessageBox :: {background-color: white }")

# Hiển thị QMessageBox
message_box.exec()
