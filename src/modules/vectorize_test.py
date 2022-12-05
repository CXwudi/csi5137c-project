from vectorize import tf_idf
import unittest
from unittest import TestCase

class TestTfIdf(TestCase):
  def test_normal(self):
    documents = [
      ["this", "is", "a", "test"],
      ["this", "is", "another", "test"],
      ["and", "yet", "another", "one"],
      ["so", "we", "have", "four", "documents"],
    ]
    scores = tf_idf(documents)
    print(scores)

if __name__ == '__main__':
  print(__package__)
  unittest.main()