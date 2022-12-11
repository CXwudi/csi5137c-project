# run from the project root directory
from vectorize import tf_idf, tf_idf_pd_serise, serise_to_BoW_dataframe
import unittest
from unittest import TestCase
import pandas as pd
class TestTfIdf(TestCase):
  def test_normal(self):
    documents = pd.Series([
      ["this", "is", "a", "test"],
      ["this", "is", "another", "test"],
      ["and", "yet", "another", "one"],
      ["so", "we", "have", "four", "documents"],
      ["yeah", "yeah", "so", "yeah"]
    ])
    scores = tf_idf_pd_serise(documents)
    # print(scores)
  
  def test_bow(self):
    documents = pd.Series([
      ["this", "is", "a", "test"],
      ["this", "is", "another", "test"],
      ["and", "yet", "another", "one"],
      ["so", "we", "have", "four", "documents"],
      ["yeah", "yeah", "so", "yeah"]
    ])
    scores = tf_idf_pd_serise(documents)
    bow = serise_to_BoW_dataframe(documents, scores, "test_")
    print(bow)


if __name__ == '__main__':
  print(__package__)
  unittest.main()