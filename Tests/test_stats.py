import unittest
from Statistics.Statistics import Statistics
from CSVReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statobj = Statistics('Tests/Data/statsData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statobj, Statistics)

    def test_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/statsData.csv').data
        answer = CsvReader('Tests/Data/answers.csv').data
        dataset = []
        for row in test_data:
            a = int(row['Value 1'])
            dataset.append(a)
        for column in answer:
            expect_result = float((column['Mean']))
        self.assertEqual(self.statobj.mean(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)

    def test_Median_calculator(self):
        test_data = CsvReader('Tests/Data/statsData.csv').data
        answer = CsvReader('Tests/Data/answers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            expect_result = float((column['Median']))
        self.assertEqual(self.statobj.med(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)

    def test_Mode_calculator(self):
        test_data = CsvReader('Tests/Data/statsData.csv').data
        answer = CsvReader('Tests/Data/answers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            expect_result = float((column['Mode']))
        self.assertEqual(self.statobj.mod(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)

    def test_Standard_Deviation_calculator(self):
        test_data = CsvReader('Tests/Data/statsData.csv').data
        answer = CsvReader('Tests/Data/answers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            expect_result = float((column['StanDeviation']))
        self.assertEqual(self.statobj.stddev(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)

    def test_Variance_calculator(self):
        test_data = CsvReader('Tests/Data/statsData.csv').data
        answer = CsvReader('Tests/Data/answers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            expect_result = float((column['Variance']))
        self.assertEqual(self.statobj.variance(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)

    def test_z_score_calculator(self):
        test_data = CsvReader('Tests/Data/statsData.csv').data
        data_answer = CsvReader('Tests/Data/Zscore.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        data_answer1 = []
        for row in data_answer:
            z = float(row["Result"])
            data_answer1.append(z)
        self.assertEqual(self.statobj.z_score(dataset), data_answer1)
        self.assertEqual(self.statobj.result, data_answer1)


if __name__ == '__main__':
    unittest.main()
