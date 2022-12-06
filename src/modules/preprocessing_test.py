# run from the project root directory
import unittest
from unittest import TestCase
import pandas as pd
from preprocessing import preprocessing_df, _core_preprocessing_and_tokenizing

class TestTfIdf(TestCase):
  def test_df(self):
    # run this file from the project root directory
    df = pd.read_csv('data/authors_dataset.csv')
    reduced_dataset = preprocessing_df(df)
    for row in reduced_dataset["comments"]:
      if row != []:
        # print(row)
        return

  def test_some_tokenization(self):
    examples = [
      "Monster of a weekly project done 😅",
      "[other] when the customer wants the color to be \"\"clearer\"\"",
      "IMPORTANT USER UPDATE - Adobe is Giving Away The Creative Cloud For Free Due to Corona Virus"
    ]
    for example in examples:
      print(_core_preprocessing_and_tokenizing(example))

if __name__ == '__main__':
  print(__package__)
  unittest.main()