from imports import *

class DNS_SD_Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the Domain box
        domain_label = QLabel("DNS")
        domain_label.setFont(QFont("Arial", 10))
        domain_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(domain_label)

        self.domain_box = QTextEdit()
        self.domain_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.domain_box.setReadOnly(True)
        layout.addWidget(self.domain_box)

        # Create the Subdomain box
        subdomain_label = QLabel("Subdomain")
        subdomain_label.setFont(QFont("Arial", 10))
        subdomain_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(subdomain_label)

        self.subdomain_box = QTextEdit()
        self.subdomain_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.subdomain_box.setReadOnly(True)
        layout.addWidget(self.subdomain_box)

        self.setLayout(layout)