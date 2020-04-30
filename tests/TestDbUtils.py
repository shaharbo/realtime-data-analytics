import unittest
from DbUtils import process_message
from DbHandler import dbHandler

class testdbutils(unittest.TestCase):
    def setUp(self):
        self.db = dbHandler.getInstance()

    def test_wrong_file_format(self):
        message = {'path': "../invoices/invoices_2010.json", 'format': "test", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertFalse(result)

    def test_missing_arguments(self):
        message = {'path': "../invoices/invoices_2010.json"}
        result = process_message(message, self.db)
        self.assertFalse(result)

    def test_no_such_file(self):
        message = {'path': "../invoices/invoices.json", 'format': "json", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertFalse(result)

    def test_load_json(self):
        message = {'path': "../invoices/invoices_2010.json", 'format': "json", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertTrue(result)
    #
    # def test_load_csv(self):
    #     message = {'path': "/invoices/invoices_2009.csv", 'format': "csv", 'loadTo': 'test'}
    #     result = process_message(message, self.db)
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

