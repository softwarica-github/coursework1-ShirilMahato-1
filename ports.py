from imports import *

class Port_Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the Open Ports box
        open_ports_label = QLabel("Open Ports")
        open_ports_label.setFont(QFont("Arial", 10))
        open_ports_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(open_ports_label)

        self.open_ports_box = QTextEdit()
        self.open_ports_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.open_ports_box.setReadOnly(True)
        layout.addWidget(self.open_ports_box)

        self.setLayout(layout)