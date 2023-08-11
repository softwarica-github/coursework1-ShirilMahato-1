import unittest
from PyQt5.QtWidgets import QApplication
# from dns_subdomain import DNS_SD_Widget
from imports import *

app = QApplication([])  # Create a QApplication instance for testing


class TestDNS_SD_Widget(unittest.TestCase):
    def setUp(self):
        self.widget = DNS_SD_Widget()

    def test_domain_box(self):
        expected_text = "example.com"
        self.widget.domain_box.setPlainText(expected_text)
        actual_text = self.widget.domain_box.toPlainText()
        self.assertEqual(actual_text, expected_text)

    def test_subdomain_box(self):
        expected_text = "subdomain.example.com"
        self.widget.subdomain_box.setPlainText(expected_text)
        actual_text = self.widget.subdomain_box.toPlainText()
        self.assertEqual(actual_text, expected_text)

    def tearDown(self):
        self.widget.close()
        
class TestLinks_Widget(unittest.TestCase):
    def setUp(self):
        self.widget = Links_Widget()
    @patch.object(requests.Session, 'get')
    def test_enumerate_directories_and_files(self, mock_get):
        # Mock the responses
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><a href="test_link"></a></body></html>'
        mock_response.url = 'http://example.com'
        mock_get.return_value = mock_response

        # Initialize the EnumerationThread
        thread = EnumerationThread('http://example.com')

        # Run the method
        thread.enumerate_directories_and_files('http://example.com', thread.results)

        # Assert the results
        self.assertIn('http://example.com/test_link', thread.results['links'])
        
class TestEnumerationThread(unittest.TestCase):
    # def setUp(self):
    #     self.widget = EnumerationThread()
    @patch('requests.Session')
    def test_run_invalid_url(self, mock_session):
        thread = EnumerationThread('invalid_url')
        thread.signal = MagicMock()
        thread.run()
        thread.signal.emit.assert_called_once_with({'error': 'Error: Invalid URL provided. Example of a valid URL: http://example.com'})

    @patch('requests.Session')
    def test_run_valid_url(self, mock_session):
        mock_response = MagicMock()
        mock_response.headers = {'server': 'test_server'}
        mock_response.content = '<html><head><title>Test Title</title></head></html>'.encode()
        mock_session.return_value.get.return_value = mock_response
        thread = EnumerationThread('http://valid_url.com')
        thread.signal = MagicMock()
        thread.run()
        # self.assertEqual(thread.results['server'], 'test_server')
        # self.assertEqual(thread.results['page_title'], 'Test Title')

    @patch('requests.Session')
    def test_enumerate_services_and_version(self, mock_session):
        mock_response = MagicMock()
        mock_response.headers = {'server': 'test_service/test_version'}
        mock_session.return_value.get.return_value = mock_response
        thread = EnumerationThread('http://valid_url.com')
        services, version = thread.enumerate_services_and_version('http://valid_url.com')
        self.assertEqual(services, ['test_service'])
        self.assertEqual(version, 'test_version')

        
class TestPageInfoWidget(unittest.TestCase):
    def setUp(self):
        self.widget = Page_info_Widget()

    def tearDown(self):
        self.widget.close()

    def test_initial_state(self):
        self.assertEqual(self.widget.title_box.toPlainText(), '')
        self.assertEqual(self.widget.meta_box.toPlainText(), '')
        self.assertEqual(self.widget.body_box.toPlainText(), '')

    def test_update_title(self):
        title = 'Test Title'
        self.widget.title_box.setPlainText(title)
        self.assertEqual(self.widget.title_box.toPlainText(), title)

    def test_update_meta(self):
        meta = 'Test Meta'
        self.widget.meta_box.setPlainText(meta)
        self.assertEqual(self.widget.meta_box.toPlainText(), meta)

    def test_update_body(self):
        body = 'Test Body'
        self.widget.body_box.setPlainText(body)
        self.assertEqual(self.widget.body_box.toPlainText(), body)
        

class MockQMessageBox:
    @staticmethod
    def warning(*args):
        pass

class TestWebEnumerationTool(unittest.TestCase):

    def setUp(self):
        # Create an instance of the WebEnumerationTool class
        self.tool = WebEnumerationTool()

    def test_initUI(self):
        # Test that the UI is initialized with the expected title
        self.assertEqual(self.tool.windowTitle(), 'Web Enumeration Tool')

    def test_update_current_page_dashboard(self):
        # Test the update_current_page method for the Dashboard tab
        self.tool.update_current_page(0)
        self.assertFalse(self.tool.save_button.isVisible())
        self.assertFalse(self.tool.url_input.isVisible())
        self.assertFalse(self.tool.enumerate_button.isVisible())

class TestPortWidget(unittest.TestCase):

    def setUp(self):
        self.widget = Port_Widget()

    def test_open_ports_box(self):
        # Test the stylesheet of the open_ports_box
        expected_style = "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;"
        self.assertEqual(self.widget.open_ports_box.styleSheet(), expected_style)

        # Test that the open_ports_box is read-only
        self.assertTrue(self.widget.open_ports_box.isReadOnly())

class TestServerWidget(unittest.TestCase):

    def setUp(self):
        self.widget = Server_Widget()

    def test_text_boxes(self):
        # Test the properties of the text boxes
        text_boxes = [
            self.widget.server_type_box,
            self.widget.platform_box,
            self.widget.services_box,
            self.widget.version_box
        ]

        expected_style = "background-color: black; color: white; border: 1px solid white; padding: 5px; border-radius: 7px;"
        for text_box in text_boxes:
            self.assertEqual(text_box.styleSheet(), expected_style)
            self.assertTrue(text_box.isReadOnly())
        
# if __name__ == '__main__':
#     unittest.main()

