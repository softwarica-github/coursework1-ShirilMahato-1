from imports import *

class Server_Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the Server Type box
        server_type_label = QLabel("Server Type")
        server_type_label.setFont(QFont("Arial", 10))
        server_type_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(server_type_label)

        self.server_type_box = QTextEdit()
        self.server_type_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.server_type_box.setReadOnly(True)
        layout.addWidget(self.server_type_box)

        # Create the Platform box
        platform_label = QLabel("Platform")
        platform_label.setFont(QFont("Arial", 10))
        platform_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(platform_label)

        self.platform_box = QTextEdit()
        self.platform_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.platform_box.setReadOnly(True)
        layout.addWidget(self.platform_box)

        # Create the Services box
        services_label = QLabel("Services")
        services_label.setFont(QFont("Arial", 10))
        services_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(services_label)

        self.services_box = QTextEdit()
        self.services_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.services_box.setReadOnly(True)
        layout.addWidget(self.services_box)

        # Create the Version box
        version_label = QLabel("Version")
        version_label.setFont(QFont("Arial", 10))
        version_label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(version_label)

        self.version_box = QTextEdit()
        self.version_box.setStyleSheet("background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")
        self.version_box.setReadOnly(True)
        layout.addWidget(self.version_box)

        self.setLayout(layout)