from calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance
from Statistics.ZScore import zscore
from CSVReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/statsData.csv').data
        super().__init__()

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def med(self, a):
        self.result = median(a)
        return self.result

    def mod(self, a):
        self.result = mode(a)
        return self.result

    def stddev(self, a):
        self.result = standard_deviation(a)
        return self.result

    def variance(self, a):
        self.result = variance(a)
        return self.result

    def z_score(self, a):
        self.result = zscore(a)
        return self.result


