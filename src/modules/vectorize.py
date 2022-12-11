import math
import pandas as pd

def tf_idf_pd_serise(documents: pd.Series) -> pd.Series:
  """Calculate the tf-idf scores for all words in all documents.

  Args:
      documents (pd.Series): The list of documents.

  Returns:
      pd.Series: The tf-idf scores for all words in all documents.
  """
  return documents.apply(lambda tokens: [_tf_idf_core(word, tokens, documents) for word in tokens])

def tf_idf(documents: list[list[str]]) -> list[list[float]]:
  """Calculate the tf-idf scores for all words in all documents.

  Args:
      documents (list[list[str]]): The list of documents.

  Returns:
      list[list[float]]: The tf-idf scores for all words in all documents.
  """
  return [[_tf_idf_core(word, tokens, documents) for word in tokens] for tokens in documents]

def _tf_idf_core(word: str, tokens: list[str], documents: list[list[str]]) -> float:
  """Calculate the tf-idf score for a word in a document.

  Args:
      word (str): The word to calculate the tf-idf score for.
      tokens (list[str]): The list of tokens in the document.

  Returns:
      float: The tf-idf score for the word in the document.
  """
  tf = tokens.count(word) / len(tokens)
  idf = math.log(len(documents) / sum([1 for doc in documents if word in doc]))
  return tf * idf


def serise_to_BoW_dataframe(documents: pd.Series, scores: pd.Series, column_prefix = "") -> pd.DataFrame:
  """Convert the tf-idf scores for all words in all documents to a bag of words.

  Args:
      documents (pd.Series): The list of documents.
      scores (pd.Series): The tf-idf scores for all words in all documents.
  Both documents and scores must be the same length.

  Returns:
      pd.DataFrame: The bag of words.
  """
  # first get a list of all the unique words
  unique_words = set()
  for tokens in documents:
    for token in tokens:
      unique_words.add(column_prefix + token)
  unique_words = list(unique_words)
  # then create a dataframe with the words as columns, 
  df = pd.DataFrame(columns=unique_words)
  # then fill the dataframe with the scores
  for i, tokens in enumerate(documents):
    for j, token in enumerate(tokens):
      df.at[i, column_prefix + token] = scores[i][j]
  # then fill the rest of the dataframe with zeros
  df = df.fillna(0)
  return df