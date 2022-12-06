# run from the project root directory
import unittest
from unittest import TestCase
import pandas as pd
from preprocessing import preprocessing_df

class TestTfIdf(TestCase):
  def test_df(self):
    # run this file from the project root directory
    df = pd.read_csv('data/authors_dataset.csv')
    preprocessing_df(df)

if __name__ == '__main__':
  print(__package__)
  unittest.main()