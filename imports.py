import sys
import os
import socket
import platform
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from urllib.parse import urlparse
import dns.resolver
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QTextEdit, QVBoxLayout, QWidget, QFormLayout, QSizePolicy,
    QFileDialog, QMessageBox, QHBoxLayout, QTabWidget
)
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from io import StringIO
import requests

from enumeration import EnumerationThread
from dashboard import DashboardWidget
from dns_subdomain import DNS_SD_Widget
from links import Links_Widget
from page_info import Page_info_Widget
from ports import Port_Widget
from server import Server_Widget

from webenumeration import WebEnumerationTool

import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from webtest import TestEnumerationThread, MockResponse
import validators

import sqlite3
from database import DatabaseManager