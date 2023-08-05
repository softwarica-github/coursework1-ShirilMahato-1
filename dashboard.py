from imports import *
class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to Web Enumerator")
        welcome_label.setFont(QFont("Arial", 20, QFont.Bold))
        welcome_label.setStyleSheet("color: white")
        layout.addWidget(welcome_label)

        image_label = QLabel()
        pixmap = QPixmap("D:\\Shiril\\programming\\python\\web.jpg")
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)  # Adjust the size of the image automatically
        layout.addWidget(image_label)

        self.setLayout(layout)