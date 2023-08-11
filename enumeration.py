import socket
from urllib.parse import urljoin

import dns.resolver
import platform
import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal
import validators


class EnumerationThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, url):
        QThread.__init__(self)
        self.url = url
        self.results = {'links': [], 'subdomains': [], 'ports': [], 'page_title': '',
                        'meta_desc': '', 'dns_records': [], 'server': '', 'platform': '',
                        'services': [], 'version': '', 'body': ''}

    def run(self):
        try:
            # Validate the URL
            if not validators.url(self.url):
                error_msg = "Error: Invalid URL provided. Example of a valid URL: http://example.com"
                self.signal.emit({'error': error_msg})
                return

            # Perform the enumeration here
            results = self.results

            # Extract links
            try:
                self.session = requests.Session()
                response = self.session.get(self.url, timeout=5)
            except requests.exceptions.RequestException as e:
                self.signal.emit({'error': f"Error: Failed to connect to {self.url}.\n{str(e)}\n"})
                return
            finally:
                self.session.close()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract server type
            if 'server' in response.headers:
                results['server'] = response.headers['server']
            else:
                results['server'] = "Server cannot be enumerated."

            # Extract page title
            page_title = soup.title.string if soup.title else 'No title found'
            results['page_title'] = page_title

            # Extract meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            results['meta_desc'] = meta_desc['content'] if meta_desc else 'No meta description found'

            # Extract links
            links = soup.find_all('a')
            for link in links:
                results['links'].append(link.get('href'))

            # Subdomain enumeration
            subdomains = ['www', 'mail', 'ftp', 'webmail', 'admin']
            domain = self.url.split('//')[-1].split('/')[0]
            for subdomain in subdomains:
                full_url = f"http://{subdomain}.{domain}"
                try:
                    self.session = requests.Session()
                    self.session.get(full_url, timeout=3)
                    results['subdomains'].append(full_url)
                except requests.exceptions.RequestException:
                    pass
                finally:
                    self.session.close()

            # DNS enumeration
            try:
                answers = dns.resolver.resolve(domain, 'A')
                for rdata in answers:
                    results['dns_records'].append(f"A record: {rdata.address}")
            except dns.resolver.NoAnswer:
                results['dns_records'].append('No A records found')
            except Exception as e:
                results['dns_records'].append(str(e))

            # Simple port scanning
            target = domain.split(':')[0]
            well_known_ports = [80, 443, 21, 22, 23, 25, 53, 67, 110, 143]  # Well-known ports
            for port in well_known_ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.1)
                result = s.connect_ex((target, port))
                if result == 0:
                    results['ports'].append(port)
                s.close()

            # Perform directory and file enumeration
            self.enumerate_directories_and_files(self.url, results)

            # Get platform information
            results['platform'] = platform.platform()

            # Service and version enumeration
            services, version = self.enumerate_services_and_version(self.url)
            if not services:
                services.append("Services" + "\xa0" + "cannot" + "\xa0" + "be" + "\xa0" + "enumerated.")

            if not version:
                version = "Version cannot be enumerated."
            results['services'] = services
            results['version'] = version

            # Web page body
            results['body'] = response.text

            # Handle empty results
            if not results['links']:
                results['links'].append('No links found')

            if not results['subdomains']:
                results['subdomains'].append('No subdomains found')

            if not results['ports']:
                results['ports'].append('No open ports found')

            self.signal.emit(results)
        except Exception as e:
            self.signal.emit({'error': str(e)})

    def enumerate_directories_and_files(self, url, results):
        try:
            self.session = requests.Session()
            response = self.session.get(url)
            if response.status_code == 200:
                html = response.text
                base_url = response.url
                items = self.extract_directories_and_files(html, base_url)
                if items:
                    for item in items:
                        results['links'].append(item)
        except requests.exceptions.RequestException as e:
            pass
        finally:
            self.session.close()

    def extract_directories_and_files(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')

        files = []
        directories = []

        for link in soup.find_all('a'):
            item = link.get('href')
            if not item:
                continue

            if item == '../':
                continue

            item = item.strip()
            absolute_url = urljoin(base_url, item)

            if item.endswith('/'):
                directories.append(absolute_url)
            else:
                files.append(absolute_url)

        return sorted(directories) + sorted(files)

    def enumerate_services_and_version(self, url):
        services = []
        version = ''

        try:
            self.session = requests.Session()
            response = self.session.get(url)
            if 'server' in response.headers:
                server_header = response.headers['server']
                server_info = server_header.split('/')
                if len(server_info) > 1:
                    services.append(server_info[0])
                    version = server_info[1]
        except requests.exceptions.RequestException:
            pass
        finally:
            self.session.close()

        return services, version
