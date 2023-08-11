from imports import *
import sqlite3
import unittest
from unit_test import*
from int_test import*

# Create the database file if it doesn't exist
conn = sqlite3.connect('web_enumeration.db')
conn.close()


if __name__ == '__main__':
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Run the unittests
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDNS_SD_Widget))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLinks_Widget))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestEnumerationThread))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestPageInfoWidget))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestPortWidget))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestServerWidget))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestWebEnumerationTool))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDashboardWidgetIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDNSSDWidgetIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestEnumerationThreadIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLinksWidgetIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestPageInfoWidgetIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestPortWidgetIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestServerWidgetIntegration))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestWebEnumerationToolIntegration))

    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)

    if test_result.wasSuccessful():
        window = WebEnumerationTool()
        window.show()
        sys.exit(app.exec_())
