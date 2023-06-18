from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget

app = QApplication([])
window = QMainWindow()

table_widget = QTableWidget(4, 3)  # Tạo QTableWidget có 4 hàng và 3 cột

# Truy cập vào header của cột dọc
vertical_header = table_widget.verticalHeader()

# Tùy chỉnh giao diện của header của cột dọc
vertical_header.setStyleSheet("""
    QHeaderView::section {
        background-color: rgb(43, 43, 43);
        color: white;
    }
""")

window.setCentralWidget(table_widget)
window.show()

app.exec()
