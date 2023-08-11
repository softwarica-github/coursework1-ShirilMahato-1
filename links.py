from imports import *

class Links_Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the Links box
        links_label = QLabel("Links")
        links_label.setFont(QFont("Arial", 10))
        links_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(links_label)

        self.links_box = QTextEdit()
        self.links_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.links_box.setReadOnly(True)
        layout.addWidget(self.links_box)

        self.setLayout(layout)
        
