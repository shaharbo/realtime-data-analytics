import unittest
from DbUtils import process_message
from test.MockDb import MockDb


class TestDbUtils(unittest.TestCase):
    def setUp(self):
        self.db = MockDb()

    def test_1_wrong_file_format(self):
        message = {'path': "../invoices/invoices_2010.json", 'format': "test", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertFalse(result)

    def test_2_missing_arguments(self):
        message = {'path': "../invoices/invoices_2010.json"}
        result = process_message(message, self.db)
        self.assertFalse(result)

    def test_3_no_such_file(self):
        message = {'path': "../invoices/invoices.json", 'format': "json", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertFalse(result)

    def test_4_load_json(self):
        message = {'path': "../invoices/invoices_2010.json", 'format': "json", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertTrue(result)

    def test_5_load_csv(self):
        message = {'path': "../invoices/invoices_2009.csv", 'format': "csv", 'loadTo': 'test'}
        result = process_message(message, self.db)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

