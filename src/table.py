from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem


class MainTable(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.current_cell)

    def current_cell(self):
        row = self.currentRow()
        col = self.currentColumn()

        col_header = self.horizontalHeaderItem(col).text()
        row_header = self.verticalHeaderItem(row).text()
        value = self.item(row, col).text()
        print(f"""\
        The current cell is at: ({row_header}, {col_header})
        In this cell we have: {value}
        """)


class Sheet(QMainWindow):
    def __init__(self, rows, cols):
        super().__init__()

        self.form_widget = MainTable(rows, cols)
        self.setCentralWidget(self.form_widget)
        col_headers = ['Year', 'Author', 'Novel', 'Publisher or Publication']
        row_headers = ['1953', '1955', '1956', '1958']
        self.form_widget.setHorizontalHeaderLabels(col_headers)
        self.form_widget.setVerticalHeaderLabels(row_headers)

        number = QTableWidgetItem('10')
        self.form_widget.setCurrentCell(1, 1)
        self.form_widget.setItem(1, 1, number)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    sheet = Sheet(10, 4)
    sys.exit(app.exec_())
