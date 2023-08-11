from imports import *
import validators
from database import DatabaseManager

class WebEnumerationTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        
        self.enumeration_thread = None

        # Dictionary mapping tab text to label text
        self.tab_label_text = {
            "Dashboard": "Welcome to the Web_Enumerator",
            "Page_info": "",
            "Links": "",
            "DNS & Subdomain": "",
            "Port_Scanning": "",
            "Server_Info": ""
        }

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Enumeration Tool')
        self.setGeometry(100, 100, 800, 600)

        # Apply dark theme
        self.set_dark_theme()

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create a QHBoxLayout for the URL input and Enumerate button
        url_layout = QHBoxLayout()

        # Create the URL input box
        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("color: black")
        url_layout.addWidget(self.url_input)

        # Create the Enumerate button
        self.enumerate_button = QPushButton("Enumerate")
        self.enumerate_button.setStyleSheet("color: black")
        self.enumerate_button.clicked.connect(self.handle_enumerate)
        url_layout.addWidget(self.enumerate_button)

        # Add the URL input and Enumerate button layout to the main layout
        layout.addLayout(url_layout)

        # Create a QVBoxLayout for the navbar
        navbar_layout = QVBoxLayout()

        # Create the QTabWidget for the navbar
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.tab_widget.addTab(DashboardWidget(), "Dashboard")
        self.tab_widget.addTab(Page_info_Widget(), "Page_info")
        self.tab_widget.addTab(Links_Widget(), "Links")
        self.tab_widget.addTab(DNS_SD_Widget(), "DNS & Subdomain")
        self.tab_widget.addTab(Port_Widget(), "Port_Scanning")
        self.tab_widget.addTab(Server_Widget(), "Server_Info")
        self.tab_widget.currentChanged.connect(self.update_current_page)

        navbar_layout.addWidget(self.tab_widget)

        # Add the navbar layout to the main layout
        layout.addLayout(navbar_layout)

        # Create a QHBoxLayout for the text widget
        text_layout = QHBoxLayout()
        layout.addLayout(text_layout)

        # Create the text widget
        self.text_widget = QLabel()
        self.text_widget.setFont(QFont("Arial", 24, QFont.Bold))
        self.text_widget.setStyleSheet("color: white")
        text_layout.addWidget(self.text_widget)

        # Create a QHBoxLayout for the Save and Exit buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Create the Save button
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("color: black")
        self.save_button.clicked.connect(self.handle_save)
        button_layout.addWidget(self.save_button)

        # Create the Exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setStyleSheet("color: black")
        self.exit_button.clicked.connect(self.handle_exit)
        button_layout.addWidget(self.exit_button)

        # Show the initial page
        self.update_current_page(0)

    def update_current_page(self, index):
        current_widget = self.tab_widget.currentWidget()
        current_page = self.tab_widget.tabText(index)

        if current_page == "Dashboard":
            self.save_button.hide()
            self.url_input.hide()
            self.enumerate_button.hide()
        else:
            self.save_button.show()
            self.url_input.show()
            self.enumerate_button.show()

    def set_dark_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.setPalette(palette)

    def handle_enumerate(self):
        # Check if an enumeration is already in progress
        if self.enumeration_thread and self.enumeration_thread.isRunning():
            QMessageBox.warning(self, 'Warning', 'Enumeration is already in progress.')
            return
        
        # Handle the Enumerate button click
        current_tab_text = self.tab_widget.tabText(self.tab_widget.currentIndex())
        if current_tab_text == "Dashboard":
            # Perform enumeration for the Dashboard interface
            self.text_widget.setText("Enumerating Dashboard...")
        else:
            url = self.url_input.text()
            if not url:
                QMessageBox.warning(self, 'Warning', 'Please enter a valid URL.')
                return

            # Validate the URL
            if not validators.url(url):
                error_msg = f"Error: Invalid URL provided. Example of a valid URL: http://example.com"
                QMessageBox.warning(self, 'Warning', error_msg)
                return

            self.text_widget.setText("Enumerating...")

            self.enumeration_thread = EnumerationThread(url)
            self.enumeration_thread.signal.connect(self.handle_enumeration_result)
            self.enumeration_thread.start()

    def handle_enumeration_result(self, result):
        current_tab_text = self.tab_widget.tabText(self.tab_widget.currentIndex())
        if current_tab_text == "Page_info":
            self.handle_page_info_enumeration_result(result)
        elif current_tab_text == "Links":
            self.handle_links_enumeration_result(result)
        elif current_tab_text == "DNS & Subdomain":
            self.handle_dns_subdomain_enumeration_result(result)
        elif current_tab_text == "Port_Scanning":
            self.handle_port_scanning_enumeration_result(result)
        elif current_tab_text == "Server_Info":
            self.handle_server_info_enumeration_result(result)
        self.text_widget.setText("")  # Clear the text_widget
        
    def handle_page_info_enumeration_result(self, result):
        current_widget = self.tab_widget.currentWidget()

        page_title = result.get('page_title', '')
        meta_desc = result.get('meta_desc', '')
        body_text = result.get('body', '')

        # Set the page title and meta information in the QTextEdit widgets
        current_widget.title_box.setPlainText(page_title)
        current_widget.meta_box.setPlainText(meta_desc)

        # Set the modified body content in the QTextEdit widget
        formatted_body_text = self.format_body_content(body_text)
        current_widget.body_box.setPlainText(formatted_body_text)

        # Set the scrollbar to the top position
        current_widget.body_box.verticalScrollBar().setValue(0)

        # Enable word wrap
        current_widget.body_box.setLineWrapMode(QTextEdit.WidgetWidth)

        # Set read-only mode for title and meta widgets
        current_widget.title_box.setReadOnly(True)
        current_widget.meta_box.setReadOnly(True)

        # Set stylesheet for title and meta widgets
        title_style = "background-color: black; color: white; border: 1px solid white; " \
                      "padding: 5px; border-radius: 7px; font-weight: bold;"
        meta_style = "background-color: black; color: white; border: 1px solid white; " \
                     "padding: 5px; border-radius: 7px;"

        current_widget.title_box.setStyleSheet(title_style)
        current_widget.meta_box.setStyleSheet(meta_style)

        # Set stylesheet for body widget
        body_style = "background-color: black; color: white; border: 1px solid white; " \
                     "padding: 5px; border-radius: 7px; font-family: monospace;"
        current_widget.body_box.setStyleSheet(body_style)

        # Insert data into the database
        domain = self.url_input.text()
        url_id = self.db_manager.insert_page_info('', page_title, meta_desc, body_text)
        self.db_manager.insert_link(url_id, domain)


    def format_body_content(self, body_text):
        soup = BeautifulSoup(body_text, 'html.parser')
        formatted_body = self.format_soup(soup)
        return formatted_body

    def format_soup(self, soup, level=0):
        indent_size = 4
        indent = ' ' * (level * indent_size)
        result = ''

        for element in soup.children:
            if element.name:
                tag_name = element.name
                tag_text = element.get_text(strip=True)

                if element.attrs:
                    attrs = ' '.join([f'{attr}="{value}"' for attr, value in element.attrs.items()])
                    tag_start = f'{indent}<{tag_name} {attrs}>'
                else:
                    tag_start = f'{indent}<{tag_name}>'

                tag_end = f'{indent}</{tag_name}>'

                result += f'{tag_start}\n'
                if tag_text:
                    result += f'{indent}{" " * indent_size}{tag_text}\n'
                result += self.format_soup(element, level + 1)
                result += f'{tag_end}\n'
            else:
                tag_text = str(element).strip()
                if tag_text:
                    result += f'{indent}{tag_text}\n'

        return result

    def handle_links_enumeration_result(self, result):
        try:
            links = result.get('links', [])
            links = [link for link in links if link is not None]
            links_text = '\n'.join(links)
            if links_text:
                self.tab_widget.currentWidget().links_box.setText(links_text)
                # Insert links into the database
                domain = self.url_input.text()
                for link in links:
                    self.db_manager.insert_link(domain, link)  # Insert each link
            else:
                self.tab_widget.currentWidget().links_box.setText("No links found.")
        except Exception as e:
            # Log the error or display an error message
            print(f"Error in handle_links_enumeration_result: {str(e)}")
            self.tab_widget.currentWidget().links_box.setText("Error occurred while handling links enumeration result.")



    def handle_dns_subdomain_enumeration_result(self, result):
        domain_text = '\n'.join(result.get('dns_records', []))
        self.tab_widget.currentWidget().domain_box.setText(domain_text)

        subdomain_text = '\n'.join(result.get('subdomains', []))
        self.tab_widget.currentWidget().subdomain_box.setText(subdomain_text)

        # Insert data into the database
        domain = self.url_input.text()
        self.db_manager.insert_dns_subdomain(domain, domain_text, subdomain_text)

    def handle_port_scanning_enumeration_result(self, result):
        ports = result.get('ports', [])
        domain = self.url_input.text()
        url_id = self.db_manager.insert_page_info(domain, '', '', '')
        for port in ports:
            self.db_manager.insert_port(url_id, port)

        ports_text = '\n'.join(str(port) for port in ports)
        self.tab_widget.currentWidget().open_ports_box.setText(ports_text)


    def handle_server_info_enumeration_result(self, result):
        server_type_text = ' '.join(result.get('server', [])).replace(' ', '')
        self.tab_widget.currentWidget().server_type_box.setPlainText(server_type_text)

        platform_text = result.get('platform', '')
        self.tab_widget.currentWidget().platform_box.setPlainText(platform_text)

        services_text = ' '.join(result.get('services', [])).replace(' ', '')
        self.tab_widget.currentWidget().services_box.setPlainText(services_text)

        version_text = result.get('version', '')
        self.tab_widget.currentWidget().version_box.setPlainText(version_text)

        # Disable read-only mode for server type, platform, services, and version boxes
        self.tab_widget.currentWidget().server_type_box.setReadOnly(False)
        self.tab_widget.currentWidget().platform_box.setReadOnly(False)
        self.tab_widget.currentWidget().services_box.setReadOnly(False)
        self.tab_widget.currentWidget().version_box.setReadOnly(False)

        # Enable word wrap for server type, platform, services, and version boxes
        self.tab_widget.currentWidget().server_type_box.setLineWrapMode(QTextEdit.WidgetWidth)
        self.tab_widget.currentWidget().platform_box.setLineWrapMode(QTextEdit.WidgetWidth)
        self.tab_widget.currentWidget().services_box.setLineWrapMode(QTextEdit.WidgetWidth)
        self.tab_widget.currentWidget().version_box.setLineWrapMode(QTextEdit.WidgetWidth)

        # Set the stylesheet for server type, platform, services, and version boxes
        style_sheet = "background-color: black; color: white; border: 1px solid white; " \
                    "padding: 5px; border-radius: 7px; font-family: monospace;"
        self.tab_widget.currentWidget().server_type_box.setStyleSheet(style_sheet)
        self.tab_widget.currentWidget().platform_box.setStyleSheet(style_sheet)
        self.tab_widget.currentWidget().services_box.setStyleSheet(style_sheet)
        self.tab_widget.currentWidget().version_box.setStyleSheet(style_sheet)

        # Insert data into the database
        domain = self.url_input.text()
        self.db_manager.insert_server_info(domain, server_type_text, platform_text, services_text, version_text)

    def handle_save(self):
        current_tab_text = self.tab_widget.tabText(self.tab_widget.currentIndex())
        if current_tab_text == "Dashboard":
            return

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)",
                                                options=options)
        if file_name:
            current_widget = self.tab_widget.currentWidget()
            title = self.tab_widget.tabText(self.tab_widget.currentIndex())
            title_text = self.tab_label_text.get(title, '')

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(f"{title}\n{title_text}\n\n")

                if isinstance(current_widget, Page_info_Widget):
                    if current_widget.title_box.isVisible():
                        title_text = current_widget.title_box.toPlainText()
                        file.write(f"Page Title:\n{title_text}\n\n")

                    if current_widget.meta_box.isVisible():
                        meta_text = current_widget.meta_box.toPlainText()
                        file.write(f"Meta:\n{meta_text}\n\n")

                    if current_widget.body_box.isVisible():
                        body_text = current_widget.body_box.toPlainText()
                        file.write(f"Body:\n{body_text}\n\n")

                elif isinstance(current_widget, Links_Widget):
                    if current_widget.links_box.isVisible():
                        links_text = current_widget.links_box.toPlainText()
                        file.write(f"Links:\n{links_text}\n\n")

                elif isinstance(current_widget, DNS_SD_Widget):
                    if current_widget.domain_box.isVisible():
                        domain_text = current_widget.domain_box.toPlainText()
                        file.write(f"Domain:\n{domain_text}\n\n")

                    if current_widget.subdomain_box.isVisible():
                        subdomain_text = current_widget.subdomain_box.toPlainText()
                        file.write(f"Subdomain:\n{subdomain_text}\n\n")

                elif isinstance(current_widget, Port_Widget):
                    if current_widget.open_ports_box.isVisible():
                        open_ports_text = current_widget.open_ports_box.toPlainText()
                        file.write(f"Open Ports:\n{open_ports_text}\n\n")

                elif isinstance(current_widget, Server_Widget):
                    if current_widget.server_type_box.isVisible():
                        server_type_text = current_widget.server_type_box.toPlainText()
                        file.write(f"Server Type:\n{server_type_text}\n\n")

                    if current_widget.platform_box.isVisible():
                        platform_text = current_widget.platform_box.toPlainText()
                        file.write(f"Platform:\n{platform_text}\n\n")

                    if current_widget.services_box.isVisible():
                        services_text = current_widget.services_box.toPlainText()
                        file.write(f"Services:\n{services_text}\n\n")

                    if current_widget.version_box.isVisible():
                        version_text = current_widget.version_box.toPlainText()
                        file.write(f"Version:\n{version_text}\n\n")

    def handle_exit(self):
        # Stop the enumeration thread if it's running
        if self.enumeration_thread and self.enumeration_thread.isRunning():
            self.enumeration_thread.quit()
            self.enumeration_thread.wait()

        sys.exit()
