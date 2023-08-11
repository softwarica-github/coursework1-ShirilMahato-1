from imports import *

class Page_info_Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the Page Title box
        title_label = QLabel("Page Title")
        title_label.setFont(QFont("Arial", 10))
        title_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(title_label)

        self.title_box = QTextEdit()
        self.title_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.title_box.setReadOnly(True)
        layout.addWidget(self.title_box)

        # Create the Meta box
        meta_label = QLabel("Meta")
        meta_label.setFont(QFont("Arial", 10))
        meta_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(meta_label)

        self.meta_box = QTextEdit()
        self.meta_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; border-radius: 7px;")
        self.meta_box.setReadOnly(True)
        layout.addWidget(self.meta_box)

        # Create the Body box
        body_label = QLabel("Body")
        body_label.setFont(QFont("Arial", 10))
        body_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(body_label)

        self.body_box = QTextEdit()
        self.body_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.body_box.setReadOnly(True)
        layout.addWidget(self.body_box)

        self.setLayout(layout)
