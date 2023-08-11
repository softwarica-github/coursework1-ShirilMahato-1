import unittest
from unittest.mock import patch
from PyQt5.QtTest import QTest
# from enumeration import EnumerationThread
from imports import*

app = QApplication(sys.argv)

class TestDashboardWidgetIntegration(unittest.TestCase):

    def setUp(self):
        self.widget = DashboardWidget()

    def test_welcome_label(self):
        # Find all QLabels in the widget
        labels = self.widget.findChildren(QLabel)
        # Filter out the labels to find the welcome label
        welcome_labels = [label for label in labels if label.text() == "Welcome to Web Enumerator"]
        self.assertTrue(len(welcome_labels) > 0, "Welcome label not found")
        welcome_label = welcome_labels[0]
        self.assertEqual(welcome_label.text(), "Welcome to Web Enumerator")
        self.assertEqual(welcome_label.font().family(), "Arial")
        self.assertEqual(welcome_label.font().pointSize(), 20)
        self.assertEqual(welcome_label.font().weight(), QFont.Bold)
        self.assertEqual(welcome_label.styleSheet(), "color: white")

    def test_image_label(self):
        # Find all QLabels in the widget
        labels = self.widget.findChildren(QLabel)
        # Filter out the labels to find the image label
        image_labels = [label for label in labels if label.pixmap() is not None]
        self.assertTrue(len(image_labels) > 0, "Image label not found")
        image_label = image_labels[0]
        self.assertTrue(image_label.hasScaledContents())

class TestDNSSDWidgetIntegration(unittest.TestCase):

    def setUp(self):
        self.widget = DNS_SD_Widget()

    def test_domain_label(self):
        # Find all QLabels in the widget
        labels = self.widget.findChildren(QLabel)
        # Filter out the labels to find the domain label
        domain_labels = [label for label in labels if label.text() == "DNS"]
        self.assertTrue(len(domain_labels) > 0, "Domain label not found")
        domain_label = domain_labels[0]
        self.assertEqual(domain_label.text(), "DNS")
        self.assertEqual(domain_label.font().family(), "Arial")
        self.assertEqual(domain_label.font().pointSize(), 10)
        self.assertEqual(domain_label.styleSheet(), "color: white;")

    def test_domain_box(self):
        domain_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(domain_box)
        self.assertTrue(domain_box.isReadOnly())
        self.assertEqual(domain_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

    def test_subdomain_label(self):
        # Find all QLabels in the widget
        labels = self.widget.findChildren(QLabel)
        # Filter out the labels to find the subdomain label
        subdomain_labels = [label for label in labels if label.text() == "Subdomain"]
        self.assertTrue(len(subdomain_labels) > 0, "Subdomain label not found")
        subdomain_label = subdomain_labels[0]
        self.assertEqual(subdomain_label.text(), "Subdomain")
        self.assertEqual(subdomain_label.font().family(), "Arial")
        self.assertEqual(subdomain_label.font().pointSize(), 10)
        self.assertEqual(subdomain_label.styleSheet(), "color: white;")

    def test_subdomain_box(self):
        subdomain_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(subdomain_box)
        self.assertTrue(subdomain_box.isReadOnly())
        self.assertEqual(subdomain_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

class TestEnumerationThreadIntegration(unittest.TestCase):

    def setUp(self):
        self.loop = QEventLoop()
        self.results = None

    def handle_results(self, results):
        self.results = results
        self.loop.quit()

    def test_enumeration(self):
        # Use a known website for testing
        url = "http://example.com"
        thread = EnumerationThread(url)
        thread.signal.connect(self.handle_results)
        thread.start()
        self.loop.exec_()

        # Check if the results are as expected
        self.assertIsNotNone(self.results)
        self.assertIn('page_title', self.results)
        self.assertIn('meta_desc', self.results)
        self.assertIn('links', self.results)
        self.assertIn('subdomains', self.results)
        self.assertIn('ports', self.results)
        self.assertIn('dns_records', self.results)
        self.assertIn('server', self.results)
        self.assertIn('platform', self.results)
        self.assertIn('services', self.results)
        self.assertIn('version', self.results)
        self.assertIn('body', self.results)
        
class TestLinksWidgetIntegration(unittest.TestCase):

    def setUp(self):
        self.widget = Links_Widget()

    def test_links_label(self):
        # Find all QLabels in the widget
        labels = self.widget.findChildren(QLabel)
        # Filter out the labels to find the links label
        links_labels = [label for label in labels if label.text() == "Links"]
        self.assertTrue(len(links_labels) > 0, "Links label not found")
        links_label = links_labels[0]
        self.assertEqual(links_label.text(), "Links")
        self.assertEqual(links_label.font().family(), "Arial")
        self.assertEqual(links_label.font().pointSize(), 10)
        self.assertEqual(links_label.styleSheet(), "color: white;")

    def test_links_box(self):
        links_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(links_box)
        self.assertTrue(links_box.isReadOnly())
        self.assertEqual(links_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

class TestPageInfoWidgetIntegration(unittest.TestCase):

    def setUp(self):
        self.widget = Page_info_Widget()

    def test_title_label_and_box(self):
        labels = self.widget.findChildren(QLabel)
        title_label = next((label for label in labels if label.text() == "Page Title"), None)
        self.assertIsNotNone(title_label)
        self.assertEqual(title_label.text(), "Page Title")
        self.assertEqual(title_label.font().family(), "Arial")
        self.assertEqual(title_label.font().pointSize(), 10)
        self.assertEqual(title_label.styleSheet(), "color: white;")
        
        title_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(title_box)
        self.assertTrue(title_box.isReadOnly())
        self.assertEqual(title_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

    def test_meta_label_and_box(self):
        labels = self.widget.findChildren(QLabel)
        meta_label = next((label for label in labels if label.text() == "Meta"), None)
        self.assertIsNotNone(meta_label)
        self.assertEqual(meta_label.text(), "Meta")
        self.assertEqual(meta_label.font().family(), "Arial")
        self.assertEqual(meta_label.font().pointSize(), 10)
        self.assertEqual(meta_label.styleSheet(), "color: white;")
        


    def test_body_label_and_box(self):
        labels = self.widget.findChildren(QLabel)
        body_label = next((label for label in labels if label.text() == "Body"), None)
        self.assertIsNotNone(body_label)
        self.assertEqual(body_label.text(), "Body")
        self.assertEqual(body_label.font().family(), "Arial")
        self.assertEqual(body_label.font().pointSize(), 10)
        self.assertEqual(body_label.styleSheet(), "color: white;")
        
        body_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(body_box)
        self.assertTrue(body_box.isReadOnly())
        self.assertEqual(body_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

class TestPortWidgetIntegration(unittest.TestCase):

    def setUp(self):
        self.widget = Port_Widget()

    def test_open_ports_label_and_box(self):
        labels = self.widget.findChildren(QLabel)
        open_ports_label = next((label for label in labels if label.text() == "Open Ports"), None)
        self.assertIsNotNone(open_ports_label)
        self.assertEqual(open_ports_label.text(), "Open Ports")
        self.assertEqual(open_ports_label.font().family(), "Arial")
        self.assertEqual(open_ports_label.font().pointSize(), 10)
        self.assertEqual(open_ports_label.styleSheet(), "color: white;")
        
        open_ports_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(open_ports_box)
        self.assertTrue(open_ports_box.isReadOnly())
        self.assertEqual(open_ports_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

class TestServerWidgetIntegration(unittest.TestCase):

    def setUp(self):
        self.widget = Server_Widget()

    def test_server_type_label_and_box(self):
        server_type_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(server_type_box)
        self.assertEqual(server_type_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

    def test_platform_label_and_box(self):
        platform_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(platform_box)
        self.assertEqual(platform_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

    def test_services_label_and_box(self):
        services_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(services_box)
        self.assertEqual(services_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

    def test_version_label_and_box(self):
        version_box = self.widget.findChild(QTextEdit)
        self.assertIsNotNone(version_box)
        self.assertEqual(version_box.styleSheet(), "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;")

class TestWebEnumerationToolIntegration(unittest.TestCase):
    def setUp(self):
        self.form = WebEnumerationTool()

    def test_initial_UI_state(self):
        # Test the initial state of the UI components
        self.assertEqual(self.form.url_input.text(), "")
        self.assertEqual(self.form.text_widget.text(), "")
        self.assertEqual(self.form.tab_widget.currentIndex(), 0)
        self.assertEqual(self.form.tab_widget.tabText(self.form.tab_widget.currentIndex()), "Dashboard")

    def test_enumerate_button_click_without_url(self):
        # Click the Enumerate button without entering a URL
        QTest.mouseClick(self.form.enumerate_button, Qt.LeftButton)
        self.assertEqual(self.form.text_widget.text(), "Enumerating Dashboard...")

    def test_enumerate_button_click_with_invalid_url(self):
        # Enter an invalid URL and click the Enumerate button
        self.form.url_input.setText("invalid_url")
        QTest.mouseClick(self.form.enumerate_button, Qt.LeftButton)
        self.assertEqual(self.form.text_widget.text(), "Enumerating Dashboard...")

    def test_save_button_click_on_dashboard(self):
        # Click the Save button while on the Dashboard tab
        QTest.mouseClick(self.form.save_button, Qt.LeftButton)
        # Assuming a QFileDialog pops up, we can't test its content directly here, but we can check if the text widget remains unchanged
        self.assertEqual(self.form.text_widget.text(), "")


# if __name__ == "__main__":
#     unittest.main()