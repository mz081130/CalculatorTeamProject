import unittest

from CSVReader.CsvReader import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/addition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_class('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )


if __name__ == '__main__':
    unittest.main()