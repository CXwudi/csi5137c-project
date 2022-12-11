# run from the project root directory
import unittest
from unittest import TestCase
import pandas as pd
from preprocessing import preprocessing_df, _core_preprocessing_and_tokenizing, proprocessing_text

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
      "Adobe Premiere youtuber starterpack.",
      float("nan"),
      "Monster of a weekly project done 🤷‍♀️",
      "[other] when the customer wants the color to be \"\"clearer\"\"",
      "IMPORTANT USER UPDATE - Adobe is Giving Away The Creative Cloud For Free Due to Corona Virus",
      "The eps are only 13minutes each- it should'nt be too hard to check for this. The bad color is my camera in a dark room, not the show.https://preview.redd.it/e1a4az4tibu31.jpg?width=4032&format=pjpg&auto=webp&s=01f64223b7e728910f2d8a48409cbcf1c848d110"
    ]
    for example in examples:
      print(example)
      print(_core_preprocessing_and_tokenizing(example))
      # return

  def test_some_tokenization2(self):
    example_dataset = pd.DataFrame({
      "title": ["Just me?"],
      "selftext": ["deep dark fantacy"],
      "comments": [["oh yeah, I love it", "it's so good"]]
    })
    print(example_dataset)
    # preprocessed_dataset = proprocessing_text(example_dataset)
    # print(preprocessed_dataset)

if __name__ == '__main__':
  print(__package__)
  unittest.main()