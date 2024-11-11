# Import dependencies
import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QPainter
from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,  
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout,  
                               QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0
        # Dummy data
        self._data = {"Water": 24, "Rent": 1000, "Coffee": 30, "Grocery": 300, "Phone": 45, "Internet": 70}

        # Table widget
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Chart view
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Input fields and buttons
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.plot = QPushButton("Plot")

        # Initially disable 'Add' button
        self.add.setEnabled(False)

        # Right layout
        self.right = QVBoxLayout()
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # Main layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        # Set main layout
        self.setLayout(self.layout)

        # Signals and slots
        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)

        # Fill table with initial data
        self.fill_table()

    @Slot()
    def add_element(self):
        des = self.description.text()
        price = self.price.text()

        try:
            price_item = QTableWidgetItem(f"{float(price):.2f}")
            price_item.setTextAlignment(Qt.AlignRight)

            self.table.insertRow(self.items)
            description_item = QTableWidgetItem(des)

            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)

            self.description.setText("")
            self.price.setText("")

            self.items += 1
        except ValueError:
            print("Invalid input for price:", price)

    @Slot()
    def check_disable(self):
        self.add.setEnabled(bool(self.description.text() and self.price.text()))

    @Slot()
    def plot_data(self):
        series = QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            series.append(text, number)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):
        QApplication.quit()

    def fill_table(self):
        for desc, price in self._data.items():
            description_item = QTableWidgetItem(desc)
            price_item = QTableWidgetItem(f"{price:.2f}")
            price_item.setTextAlignment(Qt.AlignRight)
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)
            self.items += 1

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("Expense Tracker")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit action
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    # Initialize Qt application
    app = QApplication(sys.argv)
    # Create main widget and window
    widget = Widget()
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Run application
    sys.exit(app.exec())
